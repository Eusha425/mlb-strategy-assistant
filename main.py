# main.py
import streamlit as st
import mlb_client
import gemini_client
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

def main():
    st.set_page_config(page_title="⚾ Baseball Strategy Assistant", layout="wide")
    st.title("⚾ Real-Time Baseball Pitch Analyzer")
    
    with st.spinner("Connecting to MLB..."):
        try:
            data = mlb_client.get_game_data()
            
            if data == 0:
                st.error("No games today! Check back later. 🏟️")
                return

            if "liveData" not in data or "plays" not in data["liveData"] or "currentPlay" not in data["liveData"]["plays"]:
                st.warning("Game hasn't started yet! Data will update when play begins. ⏳")
                return

            else:
                # Extract game data
                plays = data["liveData"]["plays"]
                current_play = plays["currentPlay"]
                latest_pitch = current_play["playEvents"][-1]
                
                # Get pitch details
                pitch_type = latest_pitch["details"]["type"]["description"]
                balls = data["liveData"]["linescore"]["balls"]
                strikes = data["liveData"]["linescore"]["strikes"]
                count = f"{balls}-{strikes}"
                
                # Get runners - using safe navigation
                offense = data["liveData"]["linescore"].get("offense", {})
                situation = offense.get("situation", {})
                runners = situation.get("description", "no runners")

                # Display game info
                st.subheader("Live Game Situation")
                cols = st.columns(3)
                cols[0].metric("Count", count)
                cols[1].metric("Runners", runners)
                cols[2].metric("Pitch Thrown", pitch_type)

                # Generate and display insight
                with st.spinner("Analyzing strategy..."):
                    insight = gemini_client.generate_insight(count, runners, pitch_type)
                    st.subheader("🤖 AI Strategy Insight")
                    st.success(f'"{insight}"')

        except Exception as e:
            st.error(f"⚡ Error: {str(e)}")
            st.info("Pro tip: Try refreshing the page when a game is active!")

if __name__ == "__main__":
    main()