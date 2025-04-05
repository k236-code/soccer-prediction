from flask import Flask, jsonify
from flask_cors import CORS
import requests

app = Flask(__name__)
CORS(app, origins="http://localhost:3000")

@app.route('/')
def home():
    return "Welcome to the Soccer Prediction API"

@app.route('/predictions', methods=['GET'])
def get_predictions():
    try:
        # Only fetch matches for Premier League (PL)
        competition_code = "PL"
        url = f"https://api.football-data.org/v4/competitions/{competition_code}/matches"
        headers = {"X-Auth-Token": "7f32601f563b4553b90a61c3f98d2331"}
        
        # Print for debugging
        print(f"Making request to {url} with headers {headers}")
        
        response = requests.get(url, headers=headers)
        
        if response.status_code != 200:
            # Print the error response for debugging
            print(f"Error response: {response.status_code}")
            return jsonify({"error": f"API returned {response.status_code}"}), 500
        
        matches_data = response.json()
        print(f"Matches data: {matches_data}")  # Print the matches data for debugging
        return jsonify(matches_data.get('matches', []))

    except Exception as e:
        # Print the exception for debugging
        print(f"Error occurred: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True, port=5002)






















