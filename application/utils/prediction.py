import pandas as pd


def get_prediction(score, model):
    current = {
        "wickets": score.get("wickets"),
        "balls_left": score.get("balls_left"),
        "runs_left": score.get("runs_left")
    }
    current_df = pd.DataFrame(current, index=[0])
    return model.predict_proba(current_df)
