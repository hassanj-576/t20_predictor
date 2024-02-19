import tweepy

from config import CONSUMER_KEY, CONSUMER_SECRET, ACCESS_TOKEN, ACCESS_TOKEN_SECRET


def tweet_winner_prediction(score_dict, team_1_prediction, team_2_prediction):
    # auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    # auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    # api = tweepy.API(auth)
    team1 = score_dict.get("team_1_name")
    team2 = score_dict.get("team_2_name")
    target = score_dict.get("team_1_runs")
    runs = score_dict.get("team_2_runs")
    wickets = score_dict.get("team_2_wickets")
    over = score_dict.get("team_2_overs")
    ball = score_dict.get("team_2_balls")

    tweet_text = f"""T20 Between {team1} and {team2}
Target by {team1} : {target}
Runs Scored by {team2} : {runs} for {wickets}  in {over}.{ball} overs
Win Prediction : {team1} : {team_1_prediction} %  | {team2} :  {team_2_prediction}%
Bot by @hj576
@thePSLt20
#T20 #PSL9, #{team1}vs{team2} #Prediction #MachineLearning 

"""
    print(tweet_text)
    # api.update_status(tweet_text)

def tweet_score_prediction(score_dict, score_prediction):
    # auth = tweepy.OAuthHandler(CONSUMER_KEY, CONSUMER_SECRET)
    # auth.set_access_token(ACCESS_TOKEN, ACCESS_TOKEN_SECRET)
    # api = tweepy.API(auth)
    team1 = score_dict.get("team_1_name")
    team2 = score_dict.get("team_2_name")
    team_1_runs = score_dict.get("team_1_runs")
    wickets = score_dict.get("team_1_wickets")
    over = score_dict.get("team_1_overs")
    ball = score_dict.get("team_1_balls")

    tweet_text = f"""T20 Between {team1} and {team2}
Runs Scored by {team1} : {team_1_runs} for {wickets}  in {over}.{ball} overs
Total Run Prediction : {team1} : {score_prediction} 
Bot by @hj576
@thePSLt20
#T20 #PSL9, #{team1}vs{team2} #Prediction #MachineLearning 

"""
    print(tweet_text)
    # api.update_status(tweet_text)