import random

money = 100
num = random.randint(1, 10)

#Write your game of chance functions here
def coinflip(guess, bet):
	flip = random.randint(1,2)
	g_val = guess.upper()

	while not (g_val == "HEADS" or g_val == "TAILS"):
		g_val = input("Heads or Tails:").upper()

	while not bet.isdigit():
		bet = input("Enter your bet:")


	if ((g_val == "HEADS") and (flip == 1)) or ((g_val == "TAILS") and (flip == 2)):
		print("The flip was " + g_val + ", you won!\n")
		return bet
	elif (g_val == "HEADS" and flip == 2):
		print("The flip was TAILS, you lost.\n")
		return bet * -1
	elif (g_val == "TAILS" and flip == 1):
		print("The flip was HEADS, you lost.\n")
		return bet * -1

def cho_han(guess, bet):
	die1 = random.randint(1,6)
	die2 = random.randint(1,6)
	g_val = guess.upper()

	while not (g_val == "ODD" or g_val == "EVEN"):
		g_val = input("Odd or Even:").upper()

	while not bet.isdigit():
		bet = input("Enter your bet:")

	is_even = (die1 + die2) % 2 == 0

	if (is_even and g_val == "EVEN"):
		print("The sum of the die were " + g_val + ", you won!\n")
		return bet
	elif (not is_even and g_val == "ODD"):
		print("The sum of the die were " + g_val + ", you won!\n")
		return bet
	elif (not is_even and g_val == "EVEN"):
		print("The sum of the die were ODD, you lost!\n")
		return bet * -1
	elif (is_even and g_val == "ODD"):
		print("The sum of the die were EVEN, you lost!\n")
		return bet * -1

def card_game(p1_bet, p2_bet):
	deck = list(range(1,52))

	while not p1_bet.isdigit():
		p1_bet = input("Player 1 enter your bet:")

	while not p2_bet.isdigit():
		p2_bet = input("Player 2 enter your bet:")

	p1_card = deck[random.randint(0,len(deck)-1)]%13
	deck.remove(p1_card)

	p2_card = deck[random.randint(0,len(deck)-1)]%13

	if p1_card == 0 or p1_card == 1:
		p1_card += 13

	if p2_card == 0 or p2_card == 1:
		p2_card += 13

	#ace 2 3 4 5 6 7 8 9 10 jack queen king
	#1   2 3 4 5 6 7 8 9 10 jack queen 0

	print("Player 1 drew: " + str(p1_card) + ", Player 2 drew: " + str(p2_card) + ".")
	if p1_card > p2_card:
		print("Player 1 wins $" + str(p1_bet) + ".")
	elif p1_card < p2_card:
		print("Player 2 wins $" + str(p2_bet) + ".")
	else:
		print("Tie! Both players earn $0.")


def roulette(guess,bet):
	while not (guess.upper() == "ODD" or guess.upper() == "EVEN"):
		guess = input("Odd or Even:")

	while not bet.isdigit():
		bet = input("Invalid bet. Enter your bet:")

	answers = list(range(0,36))
	answers.append(00)

	ball_roll = random.randint(0,len())

#Call your game of chance functions
answer = list(range(1,10))
print(answer, len(answer))

decision = input("Play Coin Flip? (Y/N)").upper()
while decision == "Y":
	coinflip(input("Heads or Tails:"), input("Enter your bet:"))
	decision = input("Keep playing? (Y/N)").upper()

decision = input("Play Cho Han? (Y/N)").upper()
while decision == "Y":
	cho_han(input("Odd or Even:"), input("Enter your bet:"))
	decision = input("Keep playing? (Y/N)").upper()

decision = input("Play Card Game? (Y/N)").upper()
while decision == "Y":
	card_game(input("Player 1 - Enter your bet:"),input("Player 2 - Enter your bet:"))
	decision = input("Keep playing? (Y/N)").upper()

print("Thanks for playing!")

