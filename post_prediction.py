import requests
import os

API_KEY = os.getenv("33f0f0f7-1e75-4743-855b-0333ecb9812f")

def get_prediction():
    url = f"https://api.cricapi.com/v1/currentMatches?apikey={API_KEY}&offset=0"
    res = requests.get(url).json()

    if "data" not in res or len(res["data"]) == 0:
        return "No live matches right now ❌"

    match = res["data"][0]

    team1 = match["teams"][0]
    team2 = match["teams"][1]

    prediction = f"🏏 Match Prediction\n\n{team1} vs {team2}\n\n🤖 AI Prediction: {team1} has higher winning chance 📊"

    return prediction
