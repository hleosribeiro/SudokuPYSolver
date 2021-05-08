#Sudoku 2.0
#TODO
#Fazer o algoritmo de resolução em si
#Fazer a GUI
import numpy, os
import pygame
import pygame_gui

def main():
	size = (900,900)
	paperColor = pygame.Color("#e0d3af")
	black = pygame.Color("#000000")
	screen = pygame.display.set_mode(size)
	background = pygame.Surface(size)
	pygame.font.init()
	default_font = pygame.font.get_default_font()
	font_renderer = pygame.font.Font(default_font, 50)


	#loop until the user clicks the close button
	done = False
	#manage how fast the screen updates
	clock = pygame.time.Clock()
	#Main loop
	while done == False:
		#event processing
		for event in pygame.event.get(): 
			if event.type == pygame.QUIT: 
				done = True

		#game logic
		solve(screen)
		#game drawing
		# pygame.draw.line(screen, black, (0,0), size)	
		pygame.display.update()

		#limit 20 fps
		#clock.tick()



def solve(screen):
# def main():	

	board = init_board()
	# get board inputs
	
	#set immutable board

	solved = False

	board[0].value = 5
	board[1].value = 3
	board[4].value = 7
	board[9].value = 6
	board[12].value = 1
	board[13].value = 9
	board[14].value = 5
	board[19].value = 9
	board[20].value = 8
	board[25].value = 6
	board[27].value = 8
	board[31].value = 6
	board[35].value = 3
	board[36].value = 4
	board[39].value = 8
	board[41].value = 3
	board[44].value = 1
	board[55].value = 6
	board[60].value = 2
	board[61].value = 8
	board[66].value = 4
	board[67].value = 1
	board[68].value = 9
	board[71].value = 5
	board[76].value = 8
	board[79].value = 7
	board[80].value = 9


	immutable = []
	for i in range(81):
		if board[i].value != 0:
			immutable.append(i)
			draw_board(screen, board)


	current_position = 0	
	direction = 1
	#print(immutable)
	while not solved:
		os.system('clear')
		if current_position < 0:
			direction = 1

		#print("current_position: "+str(current_position))
		#print_board(board)		

		
		if current_position not in immutable:
			#print("entreiaa")
			good_guess = False
			out_of_guesses = False
			while not (good_guess or out_of_guesses):	
				#print("entrei")
				board[current_position].value += 1
				draw_board(screen, board)
				direction = 1
				
				if board[current_position].value == 10:
					out_of_guesses = True
					board[current_position].value = 0
					draw_board(screen, board)
					direction = -1
					#print("aloalo")
					current_position += direction
				
				elif check_validity(board):
					if current_position == 80:
						solved = True
					#print("meupal")
					current_position += direction
					good_guess = True


		else:
			#if not last position, continue
			if current_position == 80:
				solved = True
			else:
				#print("vsfcara")
				current_position += direction	


def draw_board(screen, board):
	size = (900,900)
	paperColor = pygame.Color("#e0d3af")
	black = pygame.Color("#000000")
	screen = pygame.display.set_mode(size)
	background = pygame.Surface(size)
	pygame.font.init()
	default_font = pygame.font.get_default_font()
	font_renderer = pygame.font.Font(default_font, 50)

	#preparing window
	background.fill(paperColor)
	screen.blit(background, (0, 0))

	#draws lines
	for i in range(81):	
		pygame.draw.rect(screen, black, [(i % 9)*100, (int(numpy.floor(i / 9)))*100, 100, 100], 5)
	
	#draw numbers
	for i in range(81):
		if(board[i].value != 10):
			label = font_renderer.render(str(board[i].value), 1, (0,0,0))		
			screen.blit(label, ((i % 9)*100+36, int(numpy.floor(i/9))*100+25))
	pygame.display.update()


def check_validity(board):
	#for each of the lines, columns and boxes construct a list with all the elements that are different than None
	#then check for repeats
	#checklines
	lines_verification = True

	for i in range(9):
		lines = []
		for j in range(81):
			if board[j].line == i and board[j].value != 0:
				lines.append(board[j].value)
		if any(lines.count(element) > 1 for element in lines):
			lines_verification = False

	

	#checkcolumns	
	columns_verification = True

	for i in range(9):
		columns = []
		for j in range(81):
			if board[j].column == i and board[j].value != 0:
				columns.append(board[j].value)
		if any(columns.count(element) > 1 for element in columns):
			columns_verification = False

	#checkboxes	
	boxes_verification = True

	for i in range(9):
		boxes = []
		for j in range(81):
			if board[j].box == i  and board[j].value != 0:
				boxes.append(board[j].value)
		if any(boxes.count(element) > 1 for element in boxes):
			boxes_verification = False

	return (lines_verification and columns_verification and boxes_verification)







def init_board():
	class board_state:
		def __init__(self, position, column, line, box, value):
			self.position = position
			self.column = column
			self.box = box
			self.line = line
			self.value = value


	board = []
	
	for i in range(81):

		value = 0
		position = i		
		line =  int(numpy.floor(i / 9))
		column = (i) % 9
		
		if column <= 2:			
			if line <= 2:
				box = 0
			elif line <= 5:
				box = 3
			else:
				box = 6
		
		
		elif column <= 5:
			if line <= 2:
				box = 1
			elif line <= 5:
				box = 4
			else:
				box = 7
		
		else:
			if line <= 2:
				box = 2
			elif line <= 5:
				box = 5
			else:
				box = 8		

		board.append(board_state(position, column, line, box, value))

	return board

if __name__ == "__main__":
	main()

