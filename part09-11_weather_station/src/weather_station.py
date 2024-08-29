# WRITE YOUR SOLUTION HERE:
class WeatherStation:
  def __init__(self, name: str):
      self.__name = name
      self.__observations = []

  def add_observation(self, observation: str):
      self.__observations.append(observation)

  def latest_observation(self) -> str:
      if self.__observations:
          return self.__observations[-1]
      return ""

  def number_of_observations(self) -> int:
      return len(self.__observations)

  def __str__(self) -> str:
      return f"{self.__name}, {self.number_of_observations()} observations"

# Example usage
# station = WeatherStation("Houston")
# station.add_observation("Rain 10mm")
# station.add_observation("Sunny")
# print(station.latest_observation())  # Output: Sunny

# station.add_observation("Thunderstorm")
# print(station.latest_observation())  # Output: Thunderstorm

# print(station.number_of_observations())  # Output: 3
# print(station)  # Output: Houston, 3 observations

    

