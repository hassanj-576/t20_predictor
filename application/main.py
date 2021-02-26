import time

import joblib

from utils.prediction import get_prediction
from utils.score import get_scores
from utils.twitter import tweet_prediction


def main():
    sleep_time = 600
    loaded_rf = joblib.load("./model/t20_model.joblib")
    while (True):
        try:
            score_list = get_scores()
            for score in score_list:
                prediction = get_prediction(score, loaded_rf)
                team_1_prediction = "{:.2f}".format(prediction[0][0] * 100)
                team_2_prediction = "{:.2f}".format(prediction[0][1] * 100)
                tweet_prediction(score, team_1_prediction, team_2_prediction)

        except Exception as e:
            print(f"SOMETHING FAILED : {e}")
            time.sleep(sleep_time)
            continue
        print("SLEEPING NOW")
        time.sleep(sleep_time)


if __name__ == '__main__':
    main()
