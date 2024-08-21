# Write your solution here:
class Clock:
    def __init__(self, hours=0, minutes=0, seconds=0):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def tick(self):
        """Advance the clock by one second."""
        self.seconds += 1
        if self.seconds == 60:
            self.seconds = 0
            self.minutes += 1
            if self.minutes == 60:
                self.minutes = 0
                self.hours += 1
                if self.hours == 24:
                    self.hours = 0

    def set(self, hours, minutes):
        """Set the clock to a new time."""
        self.hours = hours
        self.minutes = minutes
        self.seconds = 0

    def __str__(self):
        """Return the time in HH:MM:SS format."""
        return f"{self.hours:02}:{self.minutes:02}:{self.seconds:02}"

# Example usage:
# clock = Clock(23, 59, 55)
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)
# clock.tick()
# print(clock)

# clock.set(12, 5)
# print(clock)