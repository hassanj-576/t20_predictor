import requests
from bs4 import BeautifulSoup


def get_scores() -> []:
    score_list = []
    site = requests.get("https://www.espncricinfo.com/",  headers={'Cache-Control': 'no-cache',"Pragma": "no-cache","Expires": "0"}).text
    soup = BeautifulSoup(site)
    featured_score_card = soup.find("div", {"class": "slick-track"})
    scored_card_containers = featured_score_card.find_all("div", {"class", "slick-slide"})
    for sc in scored_card_containers:
        stuff = sc.find("div", {"class": "ds-flex ds-justify-between ds-items-center"})
        if stuff:
            score_card = sc.find("div", {"class": "ds-flex ds-flex-col ds-mb-2 ds-mt-1 ds-space-y-1"})
            if "t20" in stuff.text.lower() and "live" in stuff.text.lower() and "psl" in stuff.text.lower():
                return_data ={
                    "team_1_name" : None,
                    "team_1_runs": None,
                    "team_1_overs": None,
                    "team_1_balls": None,
                    "team_1_wickets": None,
                    "team_2_name": None,
                    "team_2_runs": None,
                    "team_2_overs": None,
                    "team_2_balls": None,
                    "team_2_wickets": None,

                }
                if score_card:
                    team_scores = score_card.find_all("div", {"class", "ci-team-score"})
                    team_1_line = team_scores[0]
                    team_2_line = team_scores[1]

                    team_1_divs = team_1_line.find_all("div")
                    team_2_divs = team_2_line.find_all("div")
                    team_1_name = team_1_divs[0].text
                    team_2_name = team_2_divs[0].text
                    return_data["team_1_name"] = team_1_name
                    return_data["team_2_name"] = team_2_name
                    team_1_score = None
                    team_2_score = None
                    if len(team_1_divs) > 1:
                        team_1_score = team_1_divs[1].text
                    if len(team_2_divs) > 1:
                        team_2_score = team_2_divs[1].text
                    if team_1_score:
                        print(f"{team_1_name} SCORE")
                        team_1_overs = 20
                        team_1_balls = 0
                        if "(" in team_1_score and ")" in team_1_score:
                            team_1_over_and_balls = team_1_score.split(" ")[0].replace("(", "").split("/")[0].split(".")
                            team_1_overs = team_1_over_and_balls[0]
                            if len(team_1_over_and_balls) > 1:
                                team_1_balls = team_1_over_and_balls[1]
                        return_data["team_1_overs"] = team_1_overs
                        return_data["team_1_balls"] = team_1_balls
                        team_1_runs = team_1_score.split(" ")[-1].split("/")[0]
                        if "/" not in team_1_score:
                            team_1_wickets = 10
                        else:
                            team_1_wickets = team_1_score.split(" ")[-1].split("/")[1]
                        return_data["team_1_runs"] = team_1_runs
                        return_data["team_1_wickets"] = team_1_wickets
                    if team_2_score:
                        if "(" in team_2_score and ")" in team_2_score:
                            team_2_over_and_balls = team_2_score.split(" ")[0].replace("(", "").split("/")[0].split(".")
                            team_2_overs = team_2_over_and_balls[0]
                            if len(team_2_over_and_balls) > 1:
                                team_2_balls = team_2_over_and_balls[1]
                            else:
                                team_2_balls = 0
                            return_data["team_2_overs"] = team_2_overs
                            return_data["team_2_balls"] = team_2_balls
                            team_2_runs = team_2_score.split(" ")[-1].split("/")[0]
                            team_2_wickets = team_2_score.split(" ")[-1].split("/")[1]
                            return_data["team_2_runs"] = team_2_runs
                            return_data["team_2_wickets"] = team_2_wickets
                score_list.append(return_data)


    return score_list
