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

    # load_data to make an object using json data
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
        return filter(lambda player: player.name.lower() == name.lower(), self.players)
        # return [player for player in self.players if player.name.lower() == name.lower()]
        # above is another way, same result

    def list_teams(self):
        return sorted(set(map(lambda player: player.team, self.players)))
        # using set-map because we only want to return unique team name sort by alphabethic, no need to return player

    def list_countries(self):
        return sorted(set(map(lambda player: player.nationality, self.players)))
        # using set-map because we only want to return unique country name sort by alphabethic, no need to return player

    def players_in_team(self, team):
        return filter(lambda player: player.team == team.upper(), self.players)
        # return [player for player in self.players if player.team == team.upper()]
        # above is another way, same result

    def players_from_countries(self, country):
        return sorted(filter(lambda player: player.nationality == country.upper(), self.players), key=lambda player: player.points(), reverse=True)
        # return sorted([player for player in self.players if player.nationality == country.upper()], key=lambda player: player.points(), reverse= True)
        # above is another way, same result

    def most_points(self, amount):
        highest_point = sorted(self.players, key=lambda player: (player.points(), player.goals), reverse=True)
        return highest_point[:amount]

    def most_goals(self, shown):
        highest_goals = sorted(self.players, key=lambda player: (player.goals, -player.games), reverse=True)
        return highest_goals[:shown]

class NHLStatsApp:
    def __init__(self):
        # self.NHLStats = NHLStats()
        pass

    def help(self):
        print("commands:\n0 quit\n1 search for player\n2 teams\n3 countries\n4 players in team\n5 players from country\n6 most points\n7 most goals")

    def execute(self):
        filename = input("file name: ")
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
                team_player = nhl_stats.players_in_team(team)
                for p in team_player:
                    print(p)
            elif command == "5":
                country = input("country: ")
                print()
                by_country = nhl_stats.players_from_countries(country)
                for p in by_country:
                    print(p)
            elif command == "6":
                amount = int(input("how many: "))
                print()
                most_points = nhl_stats.most_points(amount)
                for p in most_points:
                    print(p)
            elif command == "7":
                shown = int(input("how many: "))
                print()
                most_goals = nhl_stats.most_goals(shown)
                for p in most_goals:
                    print(p)
            else:
                print("command invalid!")

# Run The Application
application = NHLStatsApp()
application.execute()
        