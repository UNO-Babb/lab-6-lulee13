#DiceRoll.py
#Name:
#Date:
#Assignment:
import random

def main():
  #Create an empty list with possible roll values
  rolls = [0,0,0,0,0,0,0,0,0,0,0,0]
  #Create two dice values ranging from 1 - 6 each
  roll = 0
  while roll <= 10000:
    roll += 1
    dice1 = random.randint(1,6)
    dice2 = random.randint(1,6)
  #find the sum total of the two dice
    diceTotal = dice1 + dice2
    rolls[diceTotal - 1] = rolls[diceTotal - 1] + 1
  #print statictics for dice rolls
  print("Dice Totals:")
  spot = 0
  for i in rolls:
    print (str(spot + 1) + ":", rolls[spot], "(" + str(round((rolls[spot]/roll*100), 1)) + "%)") #parentheses gore
    spot += 1


if __name__ == '__main__':
  main()
