import time

import joblib

from utils.prediction import get_prediction, get_run_prediction
from utils.score import get_scores
from utils.twitter import tweet_winner_prediction, tweet_score_prediction
import traceback

def main():
    sleep_time = 1200
    prediction_model = joblib.load("./model/prediction_model.joblib")
    score_model = joblib.load("./model/run_predictor.joblib")
    while (True):
        try:
            score_list = get_scores()
            for score in score_list:
                if score.get("team_2_runs"):
                    # Running Winning Prediction
                    data = {
                        "wickets_left": 10 - int(score.get("team_2_wickets")),
                        "balls_left": 120 - (int(score.get("team_2_overs")) * 6 + int(score.get("team_2_balls"))),
                        "runs_left": int(score.get("team_1_runs")) - int(score.get("team_2_runs"))
                    }
                    prediction = get_prediction(data, prediction_model)

                    team_1_prediction = "{:.2f}".format(prediction[0][0] * 100)
                    team_2_prediction = "{:.2f}".format(prediction[0][1] * 100)
                    tweet_winner_prediction(score, team_1_prediction, team_2_prediction)
                else:
                    # Predicting Score
                    data = {
                        "wickets_left": 10 - int(score.get("team_1_wickets")),
                        "balls_left": 120 - (int(score.get("team_1_overs")) * 6 + int(score.get("team_1_balls"))),
                        "total_runs": int(score.get("team_1_runs"))
                    }
                    prediction = get_run_prediction(data, score_model)
                    tweet_score_prediction(score, prediction)


        except Exception as e:
            print(f"SOMETHING FAILED : {e}")
            traceback.print_exc()
            print("SLEEPING NOW")
            time.sleep(sleep_time)
            continue
        print("SLEEPING NOW")
        time.sleep(sleep_time)


if __name__ == '__main__':
    main()
