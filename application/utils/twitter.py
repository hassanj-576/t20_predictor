import tweepy

from application.config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET


def tweet_prediction(score_dict, team_1_prediction, team_2_prediction):
    auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    api = tweepy.API(auth)
    team1 = score_dict.get("first_team")
    team2 = score_dict.get("second_team")
    target = score_dict.get("target")
    runs = score_dict.get("runs")
    wickets = score_dict.get("wickets")
    over = score_dict.get("over")
    ball = score_dict.get("balls")

    tweet_text = f"""T20 Between {team1} and {team2}
Target by {team1} : {target}
Runs Scored by {team2} : {runs} for {wickets}  in {over}.{ball} overs
Win Prediction : {team1} : {team_1_prediction} %  | {team2} :  {team_2_prediction}%
Bot by @hj576
@thePSLt20
#T20 #PSL20201, #Prediction #MachineLearning

"""
    api.update_status(tweet_text)
