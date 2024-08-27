# WRITE YOUR SOLUTION HERE:
class WeatherStation:
  def __init__(self, name: str):
      self._name = name
      self._observations = []

  def add_observation(self, observation: str):
      self._observations.append(observation)

  def latest_observation(self) -> str:
      if self._observations:
          return self._observations[-1]
      return ""

  def number_of_observations(self) -> int:
      return len(self._observations)

  def __str__(self) -> str:
      return f"{self._name}, {self.number_of_observations()} observations"

# Example usage
station = WeatherStation("Houston")
station.add_observation("Rain 10mm")
station.add_observation("Sunny")
print(station.latest_observation())

station.add_observation("Thunderstorm")
print(station.latest_observation())

print(station.number_of_observations())
print(station)

    

