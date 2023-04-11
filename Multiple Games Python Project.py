import os
import mysql.connector
import pygame
import time
import random
import sys
#Setting up of options of all the games the user can play
choice=int(input("Which game would you like to play\n 1)Tic Tac Toe\n 2)Snake\n 3)Hangman\n"))
if choice==1:
    #Setting the board

    theBoard = {'1': ' ' , '2': ' ' , '3': ' ' ,
            '4': ' ' , '5': ' ' , '6': ' ' ,
            '7': ' ' , '8': ' ' , '9': ' ' }
    a1=input("Enter your name for picking X")
    a2=input("Enter your name for picking O")
    board_keys = []
    print("Places of Box")
    print('1' + '|' + '2' + '|' + '3')
    print('-+-+-')
    print('4' + '|' + '5' + '|' + '6')
    print('-+-+-')
    print('7' + '|' + '8' + '|' + '9')

    for key in theBoard:
        board_keys.append(key)



    def printBoard(board):
        print(board['1'] + '|' + board['2'] + '|' + board['3'])
        print('-+-+-')
        print(board['4'] + '|' + board['5'] + '|' + board['6'])
        print('-+-+-')
        print(board['7'] + '|' + board['8'] + '|' + board['9'])
        
    #Setting up the game
    def game():

        turn = 'X'
        count = 0

        #Movement around the board
        for i in range(10):
            printBoard(theBoard)
            print("It's your turn," + turn + ".Move to which place?")

            move = input()        

            if theBoard[move] == ' ':
                theBoard[move] = turn
                count += 1
            else:
                print("That place is already filled.\nMove to which place?")
                continue

           
            if count >= 5:
                if theBoard['1'] == theBoard['2'] == theBoard['3'] != ' ': 
                    printBoard(theBoard)
                    print("Game Over")                
                    if turn=='X':
                        print(a1+"\twon")
                    else:
                        print(a2+"\twon")
                    break
                elif theBoard['4'] == theBoard['5'] == theBoard['6'] != ' ': 
                    printBoard(theBoard)
                    print("Game Over")                
                    if turn=='X':
                        print(a1+"\twon")
                    else:
                        print(a2+"\twon")
                    break
                elif theBoard['7'] == theBoard['8'] == theBoard['9'] != ' ': 
                    printBoard(theBoard)
                    print("Game Over")                
                    if turn=='X':
                        print(a1+"\twon")
                    else:
                        print(a2+"\twon")
                    break
                elif theBoard['1'] == theBoard['4'] == theBoard['7'] != ' ': 
                    printBoard(theBoard)
                    print("Game Over")                
                    if turn=='X':
                        print(a1+"\twon")
                    else:
                        print(a2+"\twon")
                    break
                elif theBoard['2'] == theBoard['5'] == theBoard['8'] != ' ':
                    printBoard(theBoard)
                    print("Game Over")                
                    if turn=='X':
                        print(a1+"\twon")
                    else:
                        print(a2+"\twon")
                    break
                elif theBoard['3'] == theBoard['6'] == theBoard['9'] != ' ': 
                    printBoard(theBoard)
                    print("Game Over")                
                    if turn=='X':
                        print(a1+"\twon")
                    else:
                        print(a2+"\twon")
                    break 
                elif theBoard['3'] == theBoard['5'] == theBoard['7'] != ' ': 
                    printBoard(theBoard)
                    print("Game Over")                
                    if turn=='X':
                        print(a1+"\twon")
                    else:
                        print(a2+"\twon")
                    break
                elif theBoard['1'] == theBoard['5'] == theBoard['9'] != ' ': 
                    printBoard(theBoard)
                    print("Game Over")                
                    if turn=='X':
                        print(a1+"\twon")
                    else:
                        print(a2+"\twon")
                    break 

            if count == 9:
                print("Game Over")                
                print("It's a Tie!!")

            if turn =='X':
                turn = 'O'
            else:
                turn = 'X'        
        
        restart = input("Do want to play Again?(y/n)")
        if restart == "y" or restart == "Y":  
            for key in board_keys:
                theBoard[key] = " "
            #Calling the tic tac toe game
            game()

    if __name__ == "__main__":
        game()
elif choice==2:
    pygame.init()
     
    white = (255, 255, 255)
    yellow = (255, 255, 102)
    black = (0, 0, 0)
    red = (213, 50, 80)
    green = (0, 255, 0)
    blue = (50, 153, 213)
    #Setting up the window resolution
    dis_width = 600
    dis_height = 400
     
    dis = pygame.display.set_mode((dis_width, dis_height))
    pygame.display.set_caption('Snake Game')
     
    clock = pygame.time.Clock()
    #Movement of snake
    snake_block = 10
    snake_speed = 15
     
    font_style = pygame.font.SysFont("algerian", 25)
    score_font = pygame.font.SysFont("comicsansms", 35)
     
     
    def Your_score(score):
        value = score_font.render("Your Score: " + str(score), True, yellow)
        dis.blit(value, [0, 0])
     
     
     
    def our_snake(snake_block, snake_list):
        for x in snake_list:
            pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])
     
     
    def message(msg, color):
        mesg = font_style.render(msg, True, color)
        dis.blit(mesg, [dis_width / 6, dis_height / 3])
     
     
    def gameLoop():
        game_over = False
        game_close = False
     
        x1 = dis_width / 2
        y1 = dis_height / 2
     
        x1_change = 0
        y1_change = 0
        #Setting up the snake
        snake_List = []
        Length_of_snake = 1
     
        foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
        foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
     
        while not game_over:
     
            while game_close == True:
                dis.fill(blue)
                message("You Lost! Press C-Play Again or Q-Quit", red)
                Your_score(Length_of_snake - 1)
                pygame.display.update()
     
                for event in pygame.event.get():
                    if event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_q:
                            game_over = True
                            game_close = False
                        if event.key == pygame.K_c:
                            gameLoop()
     
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    game_over = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        x1_change = -snake_block
                        y1_change = 0
                    elif event.key == pygame.K_RIGHT:
                        x1_change = snake_block
                        y1_change = 0
                    elif event.key == pygame.K_UP:
                        y1_change = -snake_block
                        x1_change = 0
                    elif event.key == pygame.K_DOWN:
                        y1_change = snake_block
                        x1_change = 0
     
            if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
                game_close = True
            x1 += x1_change
            y1 += y1_change
            dis.fill(blue)
            pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])
            snake_Head = []
            snake_Head.append(x1)
            snake_Head.append(y1)
            snake_List.append(snake_Head)
            if len(snake_List) > Length_of_snake:
                del snake_List[0]
     
            for x in snake_List[:-1]:
                if x == snake_Head:
                    game_close = True
     
            our_snake(snake_block, snake_List)
            Your_score(Length_of_snake - 1)
     
            pygame.display.update()
     
            if x1 == foodx and y1 == foody:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                Length_of_snake += 1
     
            clock.tick(snake_speed)
        

        x=str(input("enter your name:"))
        y=int(input("Enter your score:"))
        #Connecting python to mysql
        def Table(Name,Score):
            try:
                connection = mysql.connector.connect(host='localhost',
                                                     database='games',
                                                     user='root',
                                                     password='jasperanirudh')
                cursor=connection.cursor()
                mySql_insert_query = """INSERT INTO high_score(Name,Score) 
                                        VALUES (%s, %s) """

                recordTuple = (Name,Score)
                cursor.execute(mySql_insert_query, recordTuple)
                connection.commit()
                print("Record set")
            except mysql.connector.Error as error:
                print("Failed to insert into MySQL table {}".format(error))
            finally:
                if (connection.is_connected()):
                    cursor.close()
                    connection.close()
                    print("MySQL connection is closed")
        Table(x,y)
        pygame.quit()
        quit()
    #Calling the snake game
    gameLoop()
elif choice==3:
    wordList =['zero','one','two','three','four','five','six','seven','eight','nine']

    guess_word = []
    # lets randomize single word from the list
    secretWord = random.choice(wordList)
    length_word = len(secretWord)
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    letter_storage = []


    #Setting up the greeting
    def beginning():
        print("Hello Mate!\n")

        while True:
            name = input("Please enter Your name\n").strip()

            if name == '':
                print("You can't do that! No blank lines")
            else:
                break

    beginning()


    #Starting the hangman
    def newFunc():
        print("Well, that's perfect moment to play some Hangman!\n")

        while True:
            gameChoice = input("Would You?\n").upper()

            if gameChoice == "YES" or gameChoice == "Y":
                break
            elif gameChoice == "NO" or gameChoice == "N":
                sys.exit("That's a shame! Have a nice day")
            else:
                print("Please Answer only Yes or No")
                continue

    newFunc()



    def change():
        # printing blanks for each letter in secret word

        for character in secretWord:
            guess_word.append("-")

        print("Ok, so the word You need to guess has", length_word, "characters")

        print("Be aware that You can enter only 1 letter from a-z\n\n")

        print(guess_word)



    def guessing():
        guess_taken = 1

        while guess_taken < 10:


            guess = input("Pick a letter\n").lower()
            #checking input
            if not guess in alphabet: 
                print("Enter a letter from a-z alphabet")
            #checking if letter has been already used
            elif guess in letter_storage: 
                print("You have already guessed that letter!")
            else: 

                letter_storage.append(guess)
                if guess in secretWord:
                    print("You guessed correctly!")
                    for x in range(0, length_word): 
                        if secretWord[x] == guess:
                            guess_word[x] = guess
                            print(guess_word)

                    if not '-' in guess_word:
                        print("You won!")
                        break
                else:
                    print("The letter is not in the word. Try Again!")
                    guess_taken += 1
                    if guess_taken == 10:
                        print(" Sorry Mate, You lost :<! The secret word was",         secretWord)

    #calling the functions
    change()
    guessing()

    print("Game Over!")
else:
    quit()



