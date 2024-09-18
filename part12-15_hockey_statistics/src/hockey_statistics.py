# Write your solution here
import json
import re

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
        return f"{self.name:<22}{self.team:<5}{self.goals:>3} + {self.assists:>2} = {self.points():>3}"

class NHLStats:
    def __init__(self, filename):
        self.players = self.load_data(filename)

    def load_data(self, filename):
        try:
            with open(filename, 'r') as file:
                data = json.load(file)
                return [Player(**player) for player in data]
        except FileNotFoundError:
            raise FileNotFoundError("The file was not found")
        except json.JSONDecodeError:
            print("Error decoding JSON.")
            return None

    def search_player(self, name):
        return [player for player in self.players if player.name.lower() == name.lower()]

    def list_teams(self):
        return sorted(set(map(lambda player: player.team, self.players)))

    def list_countries(self):
        return sorted(set(map(lambda player: player.nationality, self.players)))

    def list_players_in_team(self, team):
        return [player for player in self.players if player.team == team.upper()]





class NHLStatsApp:
    def __init__(self):
        # self.NHLStats = NHLStats()
        pass

    def help(self):
        print("commands:\n0 quit\n1 search for player\n2 teams\n3 countries\n4 players in team\n5 players from country\n6 most points\n7 most goals")

    def execute(self):
        filename = "partial.json"
        nhl_stats = NHLStats(filename)
        print(f"read the data of {len(nhl_stats.players)} players\n")
        self.help()

        while True:
            command = input("\ncommand: ")
            if command == "0":
                break
            elif command == "1":
                name = input("name: ")
                print()
                players = nhl_stats.search_player(name)
                for p in players:
                    print(p)
            elif command == "2":
                teams = nhl_stats.list_teams()
                for t in teams:
                    print(t)
            elif command == "3":
                countries = nhl_stats.list_countries()
                for c in countries:
                    print(c)
            elif command == "4":
                team = input("team: ")
                print()
                team_player = nhl_stats.list_players_in_team(team)
                for p in team_player:
                    print(p)
            elif command == "5":
                pass
            elif command == "6":
                pass
            elif command == "7":
                pass
            else:
                print("command invalid!")

application = NHLStatsApp()
application.execute()
        