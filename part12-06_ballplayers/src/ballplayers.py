class BallPlayer:
    def __init__(self, name: str, number: int, goals: int, passes: int, minutes: int):
        self.name = name
        self.number = number
        self.goals = goals
        self.passes = passes
        self.minutes = minutes

    def __str__(self):
        return (f'BallPlayer(name={self.name}, number={self.number}, '
            f'goals={self.goals}, passes={self.passes}, minutes={self.minutes})')

# Write your solution here
def most_goals(players: list):
    return max(players, key=lambda player: player.goals).name

def most_points(players: list):
    best_pointers = max(players, key=lambda player: player.goals + player.passes)
    return (best_pointers.name, best_pointers.number)

def least_minutes(players: list):
    return min(players, key=lambda player: player.minutes)

# Example Case
if __name__ == "__main__":
    player1 = BallPlayer("Archie Bonkers", 13, 5, 12, 46)
    player2 = BallPlayer("Speedy Tickets", 7, 2, 26, 55)
    player3 = BallPlayer("Cruella De Hill", 9, 1, 32, 26)
    player4 = BallPlayer("Devilled Tasmanian", 12, 1, 11, 41)
    player5 = BallPlayer("Donald Quack", 4, 3, 9, 12)
    
    team = [player1, player2, player3, player4, player5]
    print(most_goals(team)) # output: Archie Bonkers
    print(most_points(team)) # output ('Cruella De Hill', 9)
    print(least_minutes(team)) # output BallPlayer(name=Donald Quack, number=4, goals=3, assists=9, minutes=12)