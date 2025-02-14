import streamlit as st
import mlb_client
import gemini_client
from dotenv import load_dotenv
import altair as alt
import pandas as pd

# Load environment variables
load_dotenv()

def get_cached_game_data():
    """Cache the API call for performance using Streamlit's caching mechanism."""
    return mlb_client.get_game_data()

@st.cache_data(show_spinner=False)
def fetch_game_data():
    return get_cached_game_data()

def main():
    st.set_page_config(page_title="⚾ Baseball Strategy Assistant", layout="wide")
    st.title("⚾ Real-Time Baseball Pitch Analyzer")
    
    with st.spinner("Fetching game data..."):
        data = fetch_game_data()
    
    if data == 0:
        st.error("No games today! Check back later. 🏟️")
        return

    try:
        plays = data["liveData"]["plays"]
        if "currentPlay" not in plays:
            st.warning("Game hasn't started yet! Data will update when play begins. ⏳")
            return

        # Extract current play details and latest pitch information
        current_play = plays["currentPlay"]
        latest_pitch = current_play["playEvents"][-1]
        pitch_type = latest_pitch["details"]["type"]["description"]
        
        # Extract count information from the linescore
        linescore = data["liveData"]["linescore"]
        balls = linescore["balls"]
        strikes = linescore["strikes"]
        count = f"{balls}-{strikes}"
        
        # Safely retrieve runner information
        offense = linescore.get("offense", {})
        situation = offense.get("situation", {})
        runners = situation.get("description", "no runners")
        
        # Retrieve additional game info (inning and score)
        game_info = data.get("game_info", {})
        
        # Display core game metrics in three columns
        col1, col2, col3 = st.columns(3)
        col1.metric("Count", count)
        col2.metric("Runners", runners)
        col3.metric("Pitch Thrown", pitch_type)
        
        # Show additional game info in an expandable section
        with st.expander("Game Information"):
            st.write(f"Inning: {game_info.get('inning', 'N/A')}")
            st.write(f"Score: Home {game_info.get('home_score', 0)} - Away {game_info.get('away_score', 0)}")
        
        # Allow the user to select insight detail level
        insight_mode = st.radio("Select Insight Mode", options=["Quick", "Detailed"])
        extra_context = ""
        if insight_mode == "Detailed":
            extra_context = (f"\nInning: {game_info.get('inning', 'N/A')}"
                             f"\nScore: Home {game_info.get('home_score', 0)} - Away {game_info.get('away_score', 0)}")
        
        # Generate AI insight using the enhanced prompt
        with st.spinner("Generating AI Insight..."):
            insight = gemini_client.generate_insight(count, runners, pitch_type, extra_context)
        st.subheader("🤖 AI Strategy Insight")
        st.success(f'"{insight}"')
        
        # Optional: Build a pitch timeline chart if pitch event data is available
        all_plays = data["liveData"]["plays"].get("allPlays", [])
        pitch_events = [play for play in all_plays if "pitchSpeed" in play.get("details", {})]
        
        if pitch_events:
            pitch_df = pd.DataFrame([
                {
                    "timestamp": play.get("about", {}).get("timestamp"),
                    "pitchSpeed": play.get("details", {}).get("pitchSpeed"),
                    "pitchType": play.get("details", {}).get("type", {}).get("description")
                }
                for play in pitch_events
            ])
            
            if not pitch_df.empty:
                chart = alt.Chart(pitch_df).mark_circle(size=60).encode(
                    x=alt.X("timestamp:T", title="Timestamp"),
                    y=alt.Y("pitchSpeed:Q", title="Pitch Speed (MPH)"),
                    color=alt.Color("pitchType:N", title="Pitch Type"),
                    tooltip=["timestamp:T", "pitchSpeed", "pitchType"]
                ).properties(title="Pitch Timeline")
                st.altair_chart(chart, use_container_width=True)
    
    except Exception as e:
        st.error(f"Error processing game data: {e}")
        st.info("Pro tip: Try refreshing the page when a game is active!")

if __name__ == "__main__":
    main()