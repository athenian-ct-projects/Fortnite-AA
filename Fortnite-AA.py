#FORTNITE
#FORTNITE
#FORTNITE
#FORTNITE

import random

print("Welcome to Fortnite Battle Royale *Fortnite music theme now cues*")

print("which fortnite skin to you desire to be? ")
costume=input("Brite Bomber, Skull Trooper, Renegade Raider, Dark Knight, Twitch Prime Skin, or Default? ")
print("What pickaxe do you fancy")
pickaxe=input("shovel, omega, pick squeak, default, or daddy whacker? ")
print("Which back bling do you crave? ")
back_bling=input("Royale Shield, Rust Bucket, Black Shield, Red Shield, or an Alpine backpack? ")
print("Your selection " + costume + " " + pickaxe + " "+ back_bling + " is ready for use ;)")
print("Click next block to drop into the Fortnite Map")


print(costume + " where do you want to drop")
location1=input("Anarchy Acres, Greasy Grove, Pleasant Park, Lonely Lodge, Retail Row, Salty Springs, Moisty Mire, Fatal Fields, Dusty Depot")
droppers=random.randint(0,20)
print(location1 + " is a nice choice " + str(droppers) + " people have landed there")
print("Which weapon do you want?" )
weapon1=input("legendary scar, grey tactical submachine gun, the papi artale, or the rocket propeller grenade? ")

def fighting_time ():
  print("You have encountered an enemy. What do you do? ")
  enemy1=input("Team, dance, shoot at, or build? ")

  while enemy1 != "team" and enemy1 != "dance" and enemy1 != "shoot at" and  enemy1 != "build":
    enemy1=input("Team, dance, shoot at, or build? ")

  if enemy1 == 'team':
    print("epic games has banned you. NEVER TEAM AGAIN CHEATER")
    quit()
  if enemy1 == 'dance':
    print("enemy shoots at you and your dead. NEXT TIME WHEN YOU SEE AN EMEMY DONT BE DUMB")
    quit()
  if enemy1 == 'shoot at':
    print("good job you have eleminated your enemy with your " + weapon1)
  if enemy1 == 'build':
    print("good job. You have blocked their shots and have allowed time to escape from the enemy")
  if enemy1 == 'build' or 'shoot at':
    print("congratulations. You have beaten your first enemy now you may continue your match. ")


print("You are currently still in " + location1  + " where do you desire to go next?")
place1=input("Where do you desire to go to next? Retail Row, Dusty Depot, or Anarchy Acres?")
people_in_game1= random.randint(0,10)
choice1=input("there are currently " + str(people_in_game1)+ " people there. Do you still desire to go?")
if choice1 == "yes":
  location2=print("You will be transported on the next block")
if choice1 == "no":
  place2=input("Where do you desire to go to next? Retail Row, Dusty Depot, or Anarchy Acres?")
  people_in_game2= random.randint(0,10)
  choice2=input("There are currently " + str(people_in_game2)+ " people there. Do you still desire to go?")
if choice2 == "yes":
  location2=print("You will be transported on the next block")
if choice2 == "no":
  print("Too bad your going there whether you like it or not. Click the nect block to continue.")
  
def hunterer_gatherer (): 
  material1 = random.randint(150,500)
  choice3=input("Which matertial do you want? Wood, Brick, or Steel? ")
  if choice3 == "wood":
    for x in range(5):
      print("chop")
    print("you have gathered " + str(material1) + " wood")
  if choice3 == "brick":
    for x in range(5):
      print("plip plop")
    print("you have gathered " + str(material1) + " brick")
  if choice3 == "steel":
    for x in range(5):
      print("ding")
    print("you have gathered " + str(material1) + " steel")

hunterer_gatherer()

people_in_game3= random.randint (3,10)
print("There are now " + str(people_in_game3) + " left in the game.")
print("You are now in " + place1 or place2 + "What would you like to do now? ")
choice4=input("Would you like to gather more materials, or fight? ")
if choice4 == "materials":
  hunterer_gatherer()
if choice4 == "fight":
  fighting_time()


print("You are in the endgame. It is a 1v1.")
guerr_bears=(random.choice(["shooting you","building"]))
choice5=input("Your opponent is " + guerr_bears + " . What do you desire to do? Build, or shoot?")
if choice5 == "build":
  print("Nice. You are now well protected. You have earned yourself a VICTORY ROYALE!!!!!!")
if choice5 == "shoot":
  print("Your shoots are useless and they have obliterated you. Better luck next time.")
  quit()
