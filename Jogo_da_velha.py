#Jogo da Velha Vesrion 0.0.1
#Create by Gabriel dos Santos de Luna Silva

#This is the table where the players will play
tabela = [[-3,-3,-3,-3,-3],
          [-3,-3,-3,-3,-3],
          [-3,-3,-3,-3,-3],
          [-3,-3,-3,-3,-3],
          [-3,-3,-3,-3,-3]]

#This is selection of players, here they can put your name or usurname
player_one = input("Player one choose your name: ")
player_two = input("Player two choose your name: ")

#Just the player one can choose your simbol, in the future i want put a random system for this
while True:
	choose = int(input(f"{player_one} choose your simbol\n1 - choose X\n0 - chosse O"))
	if choose == 1:
		player = {1:player_one,0:player_two}
		break
	elif choose == 0:
		player = {0:player_one,1:player_two}
		break
	else:
		print("Chosse a valid number")

#this is one only control for the two players
control = {'1':(3,1),'2':(3,2),'3':(3,3),'4':(2,1),'5':(2,2),
		   '6':(2,3),'7':(1,1),'8':(1,2),'9':(1,3)}

# one player at a time
time = True

Symbol = {1:"X",0:"O",-3:" "}

for rodada in range(9):
	
	if time == True:
		while True:
			n=int(input(f"{player[1]} Escolha uma posição\n7 8 9\n4 5 6\n1 2 3"))
			condition = control[str(n)]
			if tabela[condition[0]][condition[1]] == -3:
				tabela[condition[0]][condition[1]] = 1
				time = False
				break
			else:
				print("Escolha outra posição")
	else:
		while True:
			n=int(input(f"{player[0]} Escolha uma posição\n7 8 9\n4 5 6\n1 2 3"))
			condition = control[str(n)]
			if tabela[condition[0]][condition[1]] == -3:
				tabela[condition[0]][condition[1]] = 0
				time = True
				break
			else:
				print("Escolha outra posição")

	# this calculate the points at players
	tabela[0][0] = tabela[3][3]+tabela[2][2]+tabela[1][1]
	tabela[0][1] = tabela[3][1]+tabela[2][1]+tabela[1][1]
	tabela[0][2] = tabela[3][2]+tabela[2][2]+tabela[1][2]
	tabela[0][3] = tabela[3][3]+tabela[2][3]+tabela[1][3]
	tabela[0][4] = tabela[3][1]+tabela[2][2]+tabela[1][3]
	tabela[1][4] = tabela[1][1]+tabela[1][2]+tabela[1][3]
	tabela[2][4] = tabela[2][1]+tabela[2][2]+tabela[2][3]
	tabela[3][4] = tabela[3][1]+tabela[3][2]+tabela[3][3]
	
	#print the table on the screen
	print(f'{Symbol[tabela[1][1]]}|{Symbol[tabela[1][2]]}|{Symbol[tabela[1][3]]}')
	print('------')
	print(f'{Symbol[tabela[2][1]]}|{Symbol[tabela[2][2]]}|{Symbol[tabela[2][3]]}')
	print('------')
	print(f'{Symbol[tabela[3][1]]}|{Symbol[tabela[3][2]]}|{Symbol[tabela[3][3]]}')
	print(f'{rodada}')
	#Choose who win!
	if 3 in tabela[0] or tabela[1][4] == 3 or tabela[2][4] == 3 or tabela[3][4] == 3:
		print(f'{player[1]} venceu!')
		break
	if 0 in tabela[0] or tabela[1][4] == 3 or tabela[2][4] == 3 or tabela[3][4] == 3:
		print(f'{player[0]} venceu!')
		break
	if i == 8:
		print("Velha")
