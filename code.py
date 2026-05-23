import random 
ROCK = '''
 _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

PAPER = '''
   _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

SCISSORS = '''
 _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

game_images = [ROCK, PAPER , SCISSORS]
user_choice = int(input("type in 0 for rock/ 1 for paper/ 2 for scissors\n"))
comp_choice = random.randint (0,2)
print("your choice: ")
if user_choice <= 2 and user_choice >= 0 :
    print (game_images [user_choice])
print("computer choice: ")
print (game_images [comp_choice]) 
if user_choice > 3 :
    print ("invalid number")
elif comp_choice == user_choice:
    print ("ITS A DRAW!")
elif comp_choice== 0 and user_choice== 1 or \
     comp_choice== 1 and user_choice==2 or \
     comp_choice== 2 and user_choice==0 :
    print ("YOU WIN!")
else : print ("YOU LOSE!")
