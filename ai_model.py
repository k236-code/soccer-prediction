from flask import Flask, jsonify, request

# Create a Flask application instance
app = Flask(__name__)

@app.route('/')
def home():
    return "Welcome to the Soccer Prediction API!"

@app.route("/predict", methods=["GET"])
def predict():
    team_score = float(request.args.get("team_score", 0))
    team2_score = float(request.args.get("team2_score", 0))
    team_strength = float(request.args.get("team_strength", 0))
    team2_strength = float(request.args.get("team2_strength", 0))

    # Example AI model logic for prediction
    prediction = "Team 1 Win" if team_score + team_strength > team2_score + team2_strength else "Team 2 Win"
    
    return jsonify({"prediction": prediction})

@app.route('/predictions', methods=['GET'])
def get_predictions():
    # Prediction data with win probabilities and odds
    predictions = [
        {
            "team1": "Team A", 
            "team2": "Team B", 
            "prediction": "Team A Wins",
            "team1_logo": "https://example.com/team_a_logo.png", 
            "team2_logo": "https://example.com/team_b_logo.png",
            "date": "2025-04-05", 
            "time": "18:00",
            "win_probability_team1": 0.75, 
            "win_probability_team2": 0.25,
            "odds_team1": 1.4, 
            "odds_team2": 2.8
        },
        {
            "team1": "Team C", 
            "team2": "Team D", 
            "prediction": "Draw",
            "team1_logo": "https://example.com/team_c_logo.png", 
            "team2_logo": "https://example.com/team_d_logo.png",
            "date": "2025-04-06", 
            "time": "20:00",
            "win_probability_team1": 0.3, 
            "win_probability_team2": 0.3,
            "odds_team1": 3.5, 
            "odds_team2": 3.5
        }
    ]
    return jsonify(predictions)

if __name__ == "__main__":
    app.run(port=5002, debug=True)









