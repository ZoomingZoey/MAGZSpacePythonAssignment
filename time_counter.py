
class TimeCounter:
  def __init__(self):
    self.seconds = 0
    self.minutes = 0
    self.hours = 0
    self.days = 0
    self.weeks = 0
    self.months = 0
    self.years = 0

  def increment(self):
    if self.seconds > 59: # 60 seconds
      self.minutes += 1
      self.seconds = 0
    
    if self.minutes > 59: # 60 minutes
      self.hours += 1
      self.minutes = 0

    if self.hours > 23: # 24 hours
      self.days += 1
      self.hours = 0

    if self.days > 6: # 7 days
      self.weeks += 1
      self.days = 0

    if self.weeks > 3: # 4 weeks
      self.months += 1
      self.weeks = 0

    if self.months > 11: # 12 months
      self.years += 1
      self.months = 0

    self.seconds += 1

  def reset(self):
    self.seconds = 0
    self.minutes = 0
    self.hours = 0
    self.days = 0
    self.weeks = 0
    self.months = 0
    self.years = 0

  def print(self):
    print(f'{self.years} years, {self.months} months, {self.weeks} weeks, {self.days} days, {self.hours} hours, {self.minutes} minutes, {self.seconds} seconds')

  def calculate_from_seconds(self, seconds):
    self.reset()
    count = 0
    while count < seconds:
      self.increment()
      count += 1

    return f'{self.years} years, {self.months} months, {self.weeks} weeks, {self.days} days, {self.hours} hours, {self.minutes} minutes, {self.seconds} seconds'
  


    

    


  

    