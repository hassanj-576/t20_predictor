import requests
from bs4 import BeautifulSoup


def get_scores() -> []:
    score_list = []
    site = requests.get("https://www.espncricinfo.com/").text
    soup = BeautifulSoup(site)
    featured_score_card = soup.find("div", {"class": "featured-scoreboard"})
    scored_card_containers = featured_score_card.find_all("div", {"class", "scorecard-container"})
    for score_card_container in scored_card_containers:
        status = score_card_container.find("div", {"class": "status"}).text
        description = score_card_container.find("div", {"class": "description"}).text
        if status == "live" and "t20" in description.lower():
            teams = score_card_container.find_all("div", {"class": "team"})
            second_team = teams[1]
            first_team = teams[0]
            first_team_name = first_team.find("div", {"class", "name-detail"}).text
            second_team_name = second_team.find("div", {"class", "name-detail"}).text
            print(f"Match Between {first_team_name} and {second_team_name}")
            second_team_score_detail = second_team.find("div", {"class", "score-detail"})
            if second_team_score_detail:
                print("Second Inning")
                target = first_team.find("span", {"class", "score"}).text.split("/")[0]
                runs = int(second_team.find("span", {"class", "score"}).text.split("/")[0])
                runs_left = int(target) - int(second_team.find("span", {"class", "score"}).text.split("/")[0])
                wickets = second_team.find("span", {"class", "score"}).text.split("/")[1]
                over = int(
                    second_team.find("span", {"class", "score-info"}).text.split("/")[0].split(".")[0].replace("(", ""))
                try:
                    balls = int(second_team.find("span", {"class", "score-info"}).text.split("/")[0].split(".")[1])
                except Exception as e:
                    print("Exception getting balls : ", e)
                    balls = 0
                balls_left = 120 - ((over * 6) + balls)

                print("Target :", target)
                print("Runs : ", runs)
                print("Runs Left : ", runs_left)
                print("Wickets :", wickets)
                print("Over: ", over)
                print("balls: ", balls)
                print("balls left :", balls_left)
                score_list.append(
                    {
                        "target": target,
                        "over": over,
                        "balls": balls,
                        "wickets": wickets,
                        "runs": runs,
                        "balls_left": balls_left,
                        "runs_left": runs_left,
                        "first_team": first_team_name,
                        "second_team": second_team_name
                    }
                )
    return score_list
