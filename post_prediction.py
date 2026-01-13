import requests
import os

API_KEY = os.getenv("33f0f0f7-1e75-4743-855b-0333ecb9812f")

def get_prediction():
    url = f"https://api.cricketdata.org/v1/currentMatches?apikey={API_KEY}"

    response = requests.get(url)
    data = response.json()

    matches = data.get("data", [])

    for match in matches:
        status = match.get("status", "").lower()

        if "live" in status:
            team1 = match["teams"][0]
            team2 = match["teams"][1]

            return (
                f"🏏 LIVE MATCH ALERT!\n\n"
                f"🔥 {team1} vs {team2}\n\n"
                f"📊 Prediction:\n"
                f"👉 {team1} slightly ahead\n\n"
                f"⚠️ Play responsibly"
            )

    return None
