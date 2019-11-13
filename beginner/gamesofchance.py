import random

money = 100
num = random.randint(1, 10)

#Write your game of chance functions here
def coinflip(guess, bet, money):
	flip = random.randint(1,2)
	g_val = guess.upper()

	while not (g_val == "HEADS" or g_val == "TAILS"):
		g_val = input("Invalid guess. Heads or Tails:").upper()

	while not (bet.isdigit() and int(bet) <= money):
		bet = input("Invalid bet. Enter your bet:")

	if ((g_val == "HEADS") and (flip == 1)) or ((g_val == "TAILS") and (flip == 2)):
		print("The flip was " + g_val + ", you won!\n")
		flag = 0
	elif (g_val == "HEADS" and flip == 2):
		print("The flip was TAILS, you lost.\n")
		flag = 1
	elif (g_val == "TAILS" and flip == 1):
		print("The flip was HEADS, you lost.\n")
		flag = 1

	if flag:
		print("You earned -" + str(bet) +".")
		return int(bet) * -1
	else:
		print("You earned " + str(bet) + ".")
		return int(bet)

def cho_han(guess, bet, money):
	die1 = random.randint(1,6)
	die2 = random.randint(1,6)
	g_val = guess.upper()

	while not (g_val == "ODD" or g_val == "EVEN"):
		g_val = input("Invalid guess. Odd or Even:").upper()

	while not (bet.isdigit() and int(bet) <= money):
		bet = input("Invalid bet. Enter your bet:")

	is_even = (die1 + die2) % 2 == 0

	if (is_even and g_val == "EVEN") or (not is_even and g_val == "ODD"):
		print("The sum of the die were " + g_val + ", you won!\n")
		flag = 0
	# elif (not is_even and g_val == "ODD"):
	# 	print("The sum of the die were " + g_val + ", you won!\n")
	elif (not is_even and g_val == "EVEN"):
		print("The sum of the die were ODD, you lost!\n")
		flag = 1
	elif (is_even and g_val == "ODD"):
		print("The sum of the die were EVEN, you lost!\n")
		flag = 1

	if flag:
		print("You earned -" + str(bet) + ".")
		return int(bet) * -1
	else:
		print("You earned " + str(bet) + ".")
		return int(bet)

def card_game(p1_bet, p2_bet):
	deck = list(range(1,52))

	while not p1_bet.isdigit():
		p1_bet = input("Invalid bet. Player 1 enter your bet:")

	while not p2_bet.isdigit():
		p2_bet = input("Invalid bet. Player 2 enter your bet:")

	p1_card = deck[random.randint(0,len(deck))]%13
	deck.remove(p1_card)

	p2_card = deck[random.randint(0,len(deck))]%13

	if p1_card == 0 or p1_card == 1:
		p1_card += 13

	if p2_card == 0 or p2_card == 1:
		p2_card += 13

	#ace 2 3 4 5 6 7 8 9 10 jack queen king
	#1   2 3 4 5 6 7 8 9 10 11   12    0

	print("Player 1 drew: " + str(p1_card) + ", Player 2 drew: " + str(p2_card) + ".")
	if p1_card > p2_card:
		print("Player 1 wins $" + str(p1_bet) + ".")
	elif p1_card < p2_card:
		print("Player 2 wins $" + str(p2_bet) + ".")
	else:
		print("Tie! Both players earn $0.")


def roulette(guess,bet, money):
	while not (guess.upper() == "ODD" or guess.upper() == "EVEN" or guess.isdigit()):
		guess = input("Invalid guess. Odd, Even, or Number:")

	while not bet.isdigit():
		bet = input("Invalid bet. Enter your bet:")

	answers = list(range(0,36))
	answers.append("00")

	ball_roll = answers[random.randint(0,len(answers))]

	if guess.upper() == "EVEN":
		if ball_roll % 2 == 0 and ball_roll != 0 and ball_roll != "00":
			flag = (0, 0, 1)
		else:
			flag = (1, 1, 1)
	elif guess.upper() == "ODD":
		if ball_roll % 2 == 1 and ball_roll != 0 and ball_roll != "00":
			flag = (0, 1, 1)
		else:
			flag = (1, 0, 1)
	elif guess.isdigit():
		if guess == str(ball_roll):
			flag = (1, 2, 35)
		else:
			flag = (1, 2, 35)

	print("BALL ROLL:", ball_roll)
	if flag[0] == 0:
		if flag[1] == 0:
			print("The roll was EVEN, you won $" + str(flag[2]*int(bet)) + ".")
		elif flag[1] == 1:
			print("The roll was ODD, you won $" + str(flag[2]*int(bet)) + ".")
		elif flag[1] == 2:
			print("The ball landed on your bet. You won $" + str(flag[2]*int(bet)) + ".")
		return flag[2]*int(bet)
	elif flag[0] == 1:
		if flag[1] == 0:
			print("The roll was EVEN, you lost $" + bet + ".")
		elif flag[1] == 1:
			print("The roll was ODD, you lost $" + bet + ".")
		elif flag[1] == 2:
			print("The roll was not " + guess + ", you lost $" + bet + ".")
		return int(bet) * -1

#Call your game of chance functions
money = 10
print("Current Money = " + str(money))

decision = input("Play Coin Flip? (Y/N)").upper()
while decision == "Y" and money > 0:
	money += coinflip(input("Heads or Tails:"), input("Enter your bet:"), money)
	print("\n")
	print("Current Money = " + str(money))
	decision = input("Keep playing? (Y/N)").upper()
	print("\n")

decision = input("Play Cho Han? (Y/N)").upper()
while decision == "Y" and money > 0:
	money += cho_han(input("Odd or Even:"), input("Enter your bet:"), money)
	print("\n")
	print("Current Money = " + str(money))
	decision = input("Keep playing? (Y/N)").upper()
	print("\n")

decision = input("Play Card Game? (Y/N)").upper()
while decision == "Y":
	card_game(input("Player 1 - Enter your bet:"),input("Player 2 - Enter your bet:"))
	decision = input("Keep playing? (Y/N)").upper()
	print("\n")

decision = input("Play Roulette? (Y/N)").upper()
while decision == "Y" and money > 0:
	money += roulette(input("Odd, Even, or Number:"),input("Enter your bet:"), money)
	print("\n")
	print("Current Money = " + str(money))
	decision = input("Keep playing? (Y/N)").upper()
	print("\n")


print("\nYour money after playing:", money)
print("Thanks for playing!")

