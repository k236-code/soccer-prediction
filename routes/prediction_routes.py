from flask import Blueprint, jsonify

prediction_bp = Blueprint("prediction_bp", __name__)

@prediction_bp.route("/predictions", methods=["GET"])
def get_predictions():
    predictions = [
        {
            "team1": "Team A",
            "team2": "Team B",
            "prediction": "Team A Wins",
            "date": "2025-04-05",
            "time": "18:00",
            "team1_logo": "https://example.com/team_a_logo.png",
            "team2_logo": "https://example.com/team_b_logo.png",
            "win_probability_team1": 0.75,
            "win_probability_team2": 0.25,
            "odds_team1": 1.4,
            "odds_team2": 2.8
        }
    ]
    return jsonify(predictions)

