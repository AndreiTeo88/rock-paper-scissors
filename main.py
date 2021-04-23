import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

# 0 = rock 1 = paper 2 = scissors
# Rock wins against scissors. Scissors win against paper. Paper wins against rock.

player = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors \n"))
computer = random.randint(0, 2)
game = [rock, paper, scissors]

if player >= 3 or player < 0:
  print("Invalid number")
else:
  print(f"{game[player]} \n Computer chose: \n {game[computer]}")

  if player == 0 and computer == 2:
    print("You win!")
  elif player == 2 and computer == 1:
    print("You win!")
  elif player == 1 and computer == 0:
    print("You win!")
  elif player == computer:
    print("It's a draw.")
  else:
    print("You lost!")

