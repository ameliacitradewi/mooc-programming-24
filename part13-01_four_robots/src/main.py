
# The exercises in this part of the course have no automated tests, as the results as visually verified.
# The tests grant points automatically as you submit your solution to the server, no matter what your implementation.
# Only submit your solution when you are ready, and your solution matches the exercise description.
# The exercises may not have automatic tests, but the course staff will still see your solution.
# If your solution clearly does not match the exercise description, you may lose the points granted for the exercises in this part.

# WRITE YOUR SOLUTION HERE:

import json
import re

# Player class to hold individual player data
class Player:
    def __init__(self, name, nationality, assists, goals, penalties, team, games):
        self.name = name
        self.nationality = nationality
        self.assists = assists
        self.goals = goals
        self.penalties = penalties
        self.team = team
        self.games = games

    def points(self):
        return self.goals + self.assists

    def __str__(self):
        # Formatted output as per requirements
        return f"{self.name:<22}{self.team:<5}{self.goals:>3} + {self.assists:>2} = {self.points():>3}"

# Team class to handle team-related queries
class Team:
    @staticmethod
    def list_teams(players):
        teams = sorted(set(player.team for player in players))
        return teams

# Country class to handle country-related queries
class Country:
    @staticmethod
    def list_countries(players):
        countries = sorted(set(player.nationality for player in players))
        return countries

# NHLStats class to handle the main functionality
class NHLStats:
    def __init__(self, filename):
        self.players = self.load_data(filename)
    
    def load_data(self, filename):
        with open(filename, 'r') as file:
            data = json.load(file)
            return [Player(**player) for player in data]

    def search_player(self, name):
        regex = re.compile(name, re.IGNORECASE)
        result = [player for player in self.players if regex.search(player.name)]
        return result

    def list_teams(self):
        return Team.list_teams(self.players)

    def list_countries(self):
        return Country.list_countries(self.players)

    def players_in_team(self, team):
        return [player for player in self.players if player.team == team]

    def players_from_country(self, country):
        return [player for player in self.players if player.nationality == country]

    def most_points(self):
        return max(self.players, key=lambda p: p.points())

    def most_goals(self):
        return max(self.players, key=lambda p: p.goals)

# Main function to run the interactive application
def main():
    filename = input("file name: ")
    nhl_stats = NHLStats(filename)
    print(f"read the data of {len(nhl_stats.players)} players\n")
    print("commands:\n0 quit\n1 search for player\n2 teams\n3 countries\n4 players in team\n5 players from country\n6 most points\n7 most goals")

    while True:
        command = input("\ncommand: ")

        if command == "0":
            break
        elif command == "1":
            name = input("name: ")
            players = nhl_stats.search_player(name)
            for player in players:
                print()
                print(player)
        elif command == "2":
            teams = nhl_stats.list_teams()
            for team in teams:
                print(team)
        elif command == "3":
            countries = nhl_stats.list_countries()
            for country in countries:
                print(country)
        elif command == "4":
            team = input("team: ")
            players = nhl_stats.players_in_team(team)
            for player in players:
                print(player)
        elif command == "5":
            country = input("country: ")
            players = nhl_stats.players_from_country(country)
            for player in players:
                print(player)
        elif command == "6":
            player = nhl_stats.most_points()
            print(player)
        elif command == "7":
            player = nhl_stats.most_goals()
            print(player)
        else:
            print("Invalid command!")

if __name__ == "__main__":
    main()
