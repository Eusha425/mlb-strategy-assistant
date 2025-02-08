
<div align="center">


# ⚾ Baseball Strategy Assistant

<p align="center">
  <img src="https://img.shields.io/badge/Status-In%20Development-yellow">
  <img src="https://img.shields.io/badge/License-MIT-blue.svg">
  <img src="https://img.shields.io/badge/Python-3.9%2B-blue">
  <img src="https://img.shields.io/badge/Streamlit-1.28.0-blue">
  <img src="https://img.shields.io/badge/MLB%20API-1.1-blue">
  <img src="https://img.shields.io/badge/Gemini%20API-1.0-blue">
</p>
 

*An AI-powered tool that explains baseball pitch strategies in real-time using MLB data and Google's Gemini API.*

[Features](#-features) •
[Installation](#-installation) •
[Usage](#-usage) •
[Project Structure](#-project-structure) •
[Contributing](#-contributing)


---
</div>

## 📋 Overview

The **Baseball Strategy Assistant** is a real-time AI tool that analyzes MLB game data and provides casual fans with fun, easy-to-understand explanations of pitch strategies. Built with Python, Streamlit, and Google's Gemini API, it transforms complex baseball tactics into relatable analogies.

---

## 🚀 Features

- **Real-Time Insights**: Fetches live game data from MLB's API.  
- **AI-Powered Analysis**: Uses Gemini to generate casual, fun explanations.  
- **Interactive UI**: Built with Streamlit for a clean, user-friendly experience.  
- **Multilingual Support**: Gemini can explain strategies in multiple languages.  
- **Historical Data**: Works with past games for demo purposes.  

---

## 🛠️ Prerequisites

- Python 3.9+  
- Google Gemini API Key ([Get it here](https://ai.google.dev/))  
- MLB API Access (Public, no key required)  

---

## 🚀 Installation & Setup

1. **Clone the repository**  
   ```bash
   git clone https://github.com/Eusha425/baseball-strategy-assistant.git
   cd baseball-strategy-assistant
   ```

2. **Set up a virtual environment**  
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**  
   Create a `.env` file in the root directory:  
   ```env
   GEMINI_API_KEY=your_api_key_here
   ```

---

## 📊 Usage

1. **Run the app locally**  
   ```bash
   streamlit run main.py
   ```

2. **View the app**  
   Open your browser and navigate to `http://localhost:8501`.  

3. **Interact with the app**  
   - The app automatically fetches live game data.  
   - If no live games are available, it uses historical data for demonstration.  
   - View real-time pitch insights with fun analogies!  

---

## 📁 Project Structure

```
baseball-strategy-assistant/
├── main.py                # Streamlit app entry point
├── mlb_client/            # MLB API interactions
│   └── __init__.py
├── gemini_client/         # Gemini API integration
│   └── __init__.py
├── date_utils/            # Date-related utilities
│   └── __init__.py
├── .env                   # Environment variables
├── requirements.txt       # Python dependencies
└── README.md              # Project documentation
```

---

## 📈 Performance

- **Latency**:  
  - MLB API: ~200ms  
  - Gemini API: ~500ms  
- **Supported Games**:  
  - Live MLB games (when available)  
  - Historical games (fallback)  

---

## 🤝 Contributing

We welcome contributions! Here’s how you can help:  
1. **Report Bugs**: Open an issue with detailed steps to reproduce.  
2. **Suggest Features**: Share your ideas for new features or improvements.  
3. **Submit Pull Requests**: Follow our [Contributing Guidelines](CONTRIBUTING.md).  

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## ✨ Acknowledgments

- **MLB API**: For providing free access to live game data.  
- **Google Gemini**: For enabling AI-powered insights.  
- **Streamlit**: For making web app development simple and fast.  

