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
                tweet_prediction(score, prediction[0][0] * 100, prediction[0][1] * 100)
                print("SLEEPING NOW")
                time.sleep(sleep_time)
        except Exception as e:
            print(f"SOMETHING FAILED : {e}")
            time.sleep(sleep_time)
            continue


if __name__ == '__main__':
    main()
