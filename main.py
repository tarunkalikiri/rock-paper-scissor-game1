import random


def get_choices():
  player_choice = input("Enter a choice (rock,paper,scissors :)")
  options = ["rock", "paper", "scissors"]
  computer_choice = random.choice(options)
  choices = {"player": player_choice, "computer": computer_choice}
  return choices


def check_win(player, computer):
  print(f"You choose {player}, computer choose {computer}")
  if player == computer:
    return "It's a Tie!"
  elif player == "rock":
    if computer == "scissors":
      return "Rock smashes scissors! You win!"
    else:
      return "paper covers the rocks! You loose!"
  elif player == "paper":
    if computer == "rock":
      return "paper covers the rocks! You win!"
    else:
      return "Scissors cuts the paper! You loose!"
  elif player == "scissors":
    if computer == "paper":
      return "Scissors cuts paper! You win!"
    else:
      return "Rock smashes the scissors! You loose!"


choices = get_choices()
result = check_win(choices["player"], choices["computer"])
print(result)
