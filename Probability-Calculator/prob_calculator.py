import copy
import random
# Consider using the modules imported above.

class Hat:

  def __init__(self, **kwargs):
    self.contents = []

    for key, value in kwargs.items():
      self.contents += value * [key]  
    

  def draw(self, number):
    try:
      balls = random.sample(self.contents, number)
    except:
      balls = copy.deepcopy(self.contents)

    for ball in balls:
      self.contents.remove(ball)
    
    return balls


def experiment(hat, expected_balls, num_balls_drawn, num_experiments):
  
  count = 0

  for i in range(num_experiments):
    hat_copy = copy.deepcopy(hat)
    balls_drawn = hat_copy.draw(num_balls_drawn)

    exball_list = []

    for key, val in expected_balls.items():
      exball_list += val * [key]

    if contains_balls(exball_list, balls_drawn):
      count += 1
 
  probability = count/num_experiments
  return probability


def contains_balls(expected_balls, actual_balls):
  for ball in expected_balls:
    if ball in actual_balls:
      actual_balls.remove(ball)
    else:
      return False
  return True 
