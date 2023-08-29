import random
from game_data import data
from art import logo
from art import vs
import os
clear = lambda: os.system('clear')

score = 0
end_of_game = False
while end_of_game == False:
  profile_1 = int (random.randint(0,49))
  profile_2 = int (random.randint(0,49))
  profile1 = data[profile_1]
  profile2 = data[profile_2]
  
  print (logo)
  print ("Compare A : " + profile1["name"] + ", "+ profile1["description"] + ", "+profile1["country"])
  
  print (vs)
  
  print ("Against B : " + profile2["name"] + ", "+ profile2["description"] + ", "+profile2["country"])
  
  guess = input ("Who has more followers? Type 'A' or 'B': ").lower()
  
  follow_1 = int ( profile1["follower_count"])
  follow_2 = int ( profile2["follower_count"])

  clear()
  if follow_1 > follow_2:
    if guess == "a":
      score += 1
      print (f"You are right ! Your score is {score}")
    else:
      print ( f"You are wrong ! Your score is {score}")
      end_of_game = True
  else:
    if guess == "b":
      score +=1
      print (f"You are right ! Your score is {score}")
    else:
      print ( f"You are wrong ! Your score is {score}")
      end_of_game = True
  
