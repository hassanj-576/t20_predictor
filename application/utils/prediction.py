import pandas as pd


def get_prediction(score, model):
    current_df = pd.DataFrame(score, index=[0])
    return model.predict_proba(current_df)

def get_run_prediction(score, model):
    current_df = pd.DataFrame(score, index=[0])
    return model.predict(current_df)[0]
