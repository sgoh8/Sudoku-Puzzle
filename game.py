
import random
class Sudoku:
    def __init__(self):
        self.numGrid = [[-1,-1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                     [-1,-1,-1,-1,-1,-1,-1,-1,-1]]
        
        self.boolGrid = [[False, False, False, False, False, False, False, False, False,],
                     [False, False, False, False, False, False, False, False, False,],
                     [False, False, False, False, False, False, False, False, False,],
                     [False, False, False, False, False, False, False, False, False,],
                     [False, False, False, False, False, False, False, False, False,],
                     [False, False, False, False, False, False, False, False, False,],
                     [False, False, False, False, False, False, False, False, False,],
                     [False, False, False, False, False, False, False, False, False,],
                     [False, False, False, False, False, False, False, False, False,]]

        self.score = 0
        
    def resetGrid(self):
        self.numGrid = [[-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1],
                        [-1,-1,-1,-1,-1,-1,-1,-1,-1]]
        
        self.boolGrid = [[False, False, False, False, False, False, False, False, False,],
                     [False, False, False, False, False, False, False, False, False,],
                     [False, False, False, False, False, False, False, False, False,],
                     [False, False, False, False, False, False, False, False, False,],
                     [False, False, False, False, False, False, False, False, False,],
                     [False, False, False, False, False, False, False, False, False,],
                     [False, False, False, False, False, False, False, False, False,],
                     [False, False, False, False, False, False, False, False, False,],
                     [False, False, False, False, False, False, False, False, False,]]

    
    def getScore(self): # gets the score variable value
        return self.score

    def printScore(self):  # Prints score variable value
        print(self.getScore())

    def incrementScore1(self):
        self.score += 1

    def printGrid(self):
        red = "\033[91m"
        blue = "\033[34m"
        reset = "\033[0m" 

        for y in range(9):
            print("----------------------------------------------")
            print("| ", end = "")
            
            for x in range(9):
                if (self.boolGrid[y][x] == True): 
                    print(blue + str(self.numGrid[y][x]) + reset + " | ", end ="")
                else:
                    print(str(self.numGrid[y][x]) + " | ", end ="")

            print("")
        print("----------------------------------------------")
        
       
    def print_boolGrid(self):
        for row in self.boolGrid:
            print("----------------------------------------------")
            print("| ", end = "")
            for element in row:
                print(str(element) + " | ", end = "")
            print("")
        print("----------------------------------------------")

   
    def randomGeneratorP1(self):
        self.resetGrid()

        choiceList = list(range(1,10))
        for y in range(3): 
            for x in range(3): 
                number = random.choice(choiceList)
                self.numGrid[y][x] = number 
                choiceList.remove(number)

        choiceList = list(range(1,10))
        for y in range(3,6): 
            for x in range(3,6): 
                number = random.choice(choiceList)
                self.numGrid[y][x] = number 
                choiceList.remove(number)
        
        choiceList = list(range(1,10))
        for y in range(6,9): 
            for x in range(6,9): 
                number = random.choice(choiceList)
                self.numGrid[y][x] = number 
                choiceList.remove(number)

        return self.randomGeneratorP2()
    

    def randomGeneratorP2(self):
        for y in range(9):
            for x in range(9):
                if self.numGrid[y][x] == -1: 
                    choiceList = list(range(1,10))

                    number = random.choice(choiceList)
                    
                    if self.checkCell(number, x, y):
                        self.numGrid[y][x] = number

                        if self.solveSudoku():
                            self.randomGeneratorP2()
                            return self.numGrid
                        
                        self.numGrid[y][x] = -1
        return False
 
        
    def cellAvailable(self): # check if there are any empty cells 
        for y in range(9):
            for x in range(9):
                if ((self.numGrid[y][x] == -1) or (self.numGrid[y][x] == 0)): 
                    return (y, x)
        return False


    def check3x3Grid(self, number, x, y): 
        if (x < 3): # determining which 3x3 x coord the cell is in
            checkX = 0
        elif (x > 5): 
            checkX = 6
        else: 
            checkX = 3
        
        if (y < 3): # determining which 3x3 y coord the cell is in
            checkY = 0
        elif (y > 5): 
            checkY = 6
        else: 
            checkY = 3

        for curX in range(checkX,checkX + 3): # checking if there are any duplication in the 3x3 cell
            for curY in range(checkY,checkY + 3): 
                if self.numGrid[curY][curX] == number: 
                    return False 
                
        return True
    

    def checkInput(self,x, y,number): # checks to see if the inputted value meets the requirements of the game
        if not number in range(1,10): 
            return False
        
        for value in self.numGrid[y]: 
            if value == number: 
                return False
        
        for row in self.numGrid: 
            if row[x] == number:
                return False 
       
        if (x < 3): # determining which 3x3 x coord the cell is in
            checkX = 0
        elif (x > 5): 
            checkX = 6
        else: 
            checkX = 3
        
        if (y < 3): # determining which 3x3 y coord the cell is in
            checkY = 0
        elif (y > 5): 
            checkY = 6
        else: 
            checkY = 3

        for curX in range(checkX,checkX + 3): #checking if there are any duplication in the 3x3 cell
            for curY in range(checkY,checkY + 3): 
                if self.numGrid[curY][curX] == number: 
                    return False 

        return True
               

    def checkFinalGrid(self): # checks the correctness of the grid when it has been filled up by user
        for y in range(9):
            for x in range(9):
                tempCell = self.numGrid[y][x]
                self.numGrid[y][x] = 0

                for value in self.numGrid[y]: 
                    if value == tempCell:
                        self.numGrid[y][x] = tempCell
                        return False
                
                for row in self.numGrid: 
                    if row[x] == tempCell:
                        self.numGrid[y][x] = tempCell
                        return False 
            
                if (x < 3): # determining which 3x3 x coord the cell is in
                    checkX = 0
                elif (x > 5): 
                    checkX = 6
                else: 
                    checkX = 3
                
                if (y < 3): # determining which 3x3 y coord the cell is in
                    checkY = 0
                elif (y > 5): 
                    checkY = 6
                else: 
                    checkY = 3

                for curX in range(checkX,checkX + 3): # checking if there are any duplication in the 3x3 cell
                    for curY in range(checkY,checkY + 3): 
                        if self.numGrid[curY][curX] == tempCell: 
                            return False 
                        
                self.numGrid[y][x] = tempCell
        return True
                
        
    def isGridFull(self): # checking to see if the grid has been 
        for y in self.numGrid: 
            for x in y: 
                if (x == 0): 
                    return False
                
        return True 
      

    def checkCell(self, number, x, y): # checks to see if a number can be fitted into a specifc space; row, col
        if ((self.numGrid[y][x] != -1) & (self.numGrid[y][x] != 0)): 
        # if self.numGrid[y][x] in range(1,10):
            return False 
        
        for value in self.numGrid[y]: # check for duplication in row 
            if value == number:
                return False 
            
        for row in self.numGrid: # check for duplication in column
            if row[x] == number:
                return False 
        
        if (x < 3): # determining which 3x3 x coord the cell is in
            checkX = 0
        elif (x > 5): 
            checkX = 6
        else: 
            checkX = 3
        
        if (y < 3): # determining which 3x3 y coord the cell is in
            checkY = 0
        elif (y > 5): 
            checkY = 6
        else: 
            checkY = 3

        for curX in range(checkX,checkX + 3): # checking if there are any duplication in the 3x3 cell
            for curY in range(checkY,checkY + 3): 
                if self.numGrid[curY][curX] == number: 
                    return False 

        return True 
    
        
    def solveSudoku(self): # solves a board using recursion
        emptyCell = self.cellAvailable()
        if not emptyCell:
            return True
        else:
            y, x = emptyCell
        
        for number in range(1,10): 
           if self.checkCell(number, x, y):
               self.numGrid[y][x] = number 

               if self.solveSudoku():
                    return self.numGrid
            
               self.numGrid[y][x] = -1
           
        return False     
    

    def generateGrid(self):
        self.randomGeneratorP1()
        self.randomGeneratorP2()

        for y in range(9): 
            for x in range(9): 
                self.boolGrid[y][x] = True 
    

    def inputNumToGrid(self, inputY, inputX, inputNum): # input the number chosen by user into the grid
        self.numGrid[inputY - 1][inputX - 1] = inputNum
        self.printGrid()

    def userInputValue(self): # validate user input and input into the grid
        import copy
        checkquit = str(input("Would you like to continue or quit the game (type continue or quit): "))
        while ((checkquit != "continue") and (checkquit != "quit")): 
            checkquit = str(input("Input is invalid. \nWould you like to continue or quit the game (type continue or quit): "))
        
        if (checkquit == "continue"): 
            inputY = int(input("Please input the row (1 - 9): "))
            while (not inputY in range (1,10)): 
                inputY = int(input("Input is not within range of 1 to 9. \nPlease input the row (1 - 9): "))
            
            inputX = int(input("Please input the column (1 - 9): "))
            while (not inputX in range (1,10)): 
                inputX = int(input("Input is not within range of 1 to 9. \nPlease input the column (1 - 9): "))
        
            while (self.boolGrid[inputY - 1][inputX - 1] == True): # prevents user from accesing the original generated grid
                print("This cell's value cannot be changed.")

                inputY = int(input("Please input the row (1 - 9): "))
                while (not inputY in range (1,10)): 
                    inputY = int(input("Input is not within range of 1 to 9. \nPlease input the row (1 - 9): "))

                inputX = int(input("Please input the column (1 - 9): "))
                while (not inputX in range (1,10)): 
                    inputX = int(input("Input is not within range of 1 to 9. \nPlease input the column (1 - 9): "))

            inputNum = int(input("Please input the value (1 - 9) for this cell [" + str(inputY) + ", " + str(inputX) + "]: "))
            while (not inputNum in range (1,10)): 
                inputNum = int(input("Input is not within range of 1 to 9. \nPlease input the value for this cell [" + str(inputY) + ", " + str(inputX) + "](1 - 9): "))

            self.inputNumToGrid(inputY, inputX, inputNum) # input the entered value to cell 

            if (self.checkUserInput(inputX, inputY, inputNum) == True): # if user input follows the regulations of the game, check whether the input is the same as the correct solution of that cell

                if (self.numGrid[inputY - 1][inputX - 1] == [inputY][inputX]):
                    self.boolGrid[inputY - 1][inputX - 1] = True 
                else: 
                    self.boolGrid[inputY - 1][inputX - 1] = False
            else: 
                    self.boolGrid[inputY - 1][inputX - 1] = False
            
        else: 
            checksave = str(input("Would you like to save your progress (type yes or no): "))
            while ((checksave != "yes") & (checksave != "no")): 
                checksave = str(input("Input is invalid. \nWould you like to save your progress (type yes or no): "))

            if (checksave == "no"): 
                print("Thank you for playing")
                quit()
            else: 
                self.saveGame()
                print('Your progress has been saved. Thank you for playing') 
                quit()


    def saveGame(self):
        saveNum = open("progressfile.txt", "w")

        grid = ""
        for y in range(9): # saves numGrid
            for x in range(9):
                if x != 8:
                    grid += str(self.numGrid[y][x]) + ","
                else:
                    grid += str(self.numGrid[y][x])
            saveNum.write(grid + "\n")
            grid = ""

        saveNum.close()

        saveBool = open("boolProgress.txt", "w")
        Bgrid = ""
        for y in range(9): # saves boolGrid
            for x in range(9):
                if x != 8:
                    Bgrid += str(self.boolGrid[y][x]) + ","
                else:
                    Bgrid += str(self.boolGrid[y][x])
            saveBool.write(Bgrid + "\n")
            Bgrid = ""

        saveBool.close()
        
    def loadGame(self):
        try: # checks to see if the txt fiiles exists
            loadNum = open("progressfile.txt", "r")
            LinesNum = loadNum.readlines()

            loadBool = open("boolProgress.txt", "r")
            LinesBool = loadBool.readlines()

        except: 
            return False
        
        else:  #the text files exists
            count = 0
            for lineNum in LinesNum: # converts numGrid back to a 2d array and the values back to an integer
                listN = lineNum.split(",")

                self.numGrid[count] = [int(x) for x in listN]
                count += 1

            loadNum.close()

            count = 0

            for lineBool in LinesBool: # converts boolGrid back to a 2d array and value back to boolean
                listB = lineBool.split(",")
                
                self.boolGrid[count] = [True if y.strip() == "True" else False for y in listB]
                count += 1

            loadBool.close()
            return True


    def checkUserInput(self, inputX, inputY, inputNum): 
        if (self.checkInput(inputX - 1,inputY - 1,inputNum) == True): # if there are no duplication, number is placed in the grid
            self.numGrid[inputY - 1][inputX - 1] = inputNum
            return True
        else: 
            return False
          

    def difficultyBoard(self, difficulty): 
        import copy
        self.generateGrid()

        numGrid_copy = copy.deepcopy(self.numGrid) 

        if difficulty == "easy": 
            cellsToRemove = random.randint(36,43)
        elif difficulty == "medium": 
            cellsToRemove = random.randint(45,54)
        elif difficulty == "hard": 
            cellsToRemove = random.randint(55,62)
        else:
            return

        for i in range(cellsToRemove):
            y = random.randint(0,8)
            x = random.randint(0,8)
            
            if (self.numGrid[y][x] != -1): 
                self.numGrid[y][x] = -1 # remove a random cell
            else: 
                i = i - 1
                continue

            workingCopy = copy.deepcopy(self.numGrid)  # make a copy of the grid with the removed cell
           
            if (self.solveSudoku() == False): # no posssible soluton with the removed cell
                self.numGrid = copy.deepcopy(workingCopy) # replaced the solved grid with the removed cell grid
                
                self.numGrid[y][x] = numGrid_copy[y][x] # assign the removed cell back to the original value
                i = i - 1
            else:
                self.numGrid = copy.deepcopy(workingCopy) # the removed cell is placed back into the grid 
          
        for y in range(9): 
            for x in range(9): 
                if (self.numGrid[y][x] == -1): # the removed cells is displayed 0 instead of -1
                    self.numGrid[y][x] = 0  
                    self.boolGrid[y][x] = False 
                else: 
                    self.boolGrid[y][x] = True # this will be the number that is displayed when generated
        
       
def main():
    import copy
    game = Sudoku()

    userInput = str(input("Would you like to load the previous saved game or play a new game? (type load or new): "))
    while ((userInput != "load") & (userInput != "new")):
        userInput = str(input("Input was invalid. \nWould you like to load the previous saved game or play a new game? (type load or new): "))
   
    if (userInput == "load"):
        if (game.loadGame() == False):
            print("Previous saved game does not exist")
            print("A new game will be generated")
            
            userDifficulty = str(input("Please choose the level of difficulty (type easy, medium or hard): "))
            while ((userDifficulty != "easy") & (userDifficulty != "medium") & (userDifficulty != "hard")):
                userDifficulty = str(input("Input was invalid. \nPlease choose the level of difficulty (type easy, medium or hard): "))
           
            game.difficultyBoard(userDifficulty)
            game.printGrid()

            while True: 
                game.userInputValue() 

                if (game.isGridFull() == True):
                    print("grid full: ")
                    print (game.isGridFull())

                    print ("checkfinalgrid: ")
                    print(game.checkFinalGrid())

                    if (game.checkFinalGrid() == True): 
                        break

            print('Game Over. Thank you for playing ')

        else: # there exist a game in the text file
            game.loadGame()
            game.printGrid()

            while True: 

                game.userInputValue() 

                if (game.isGridFull() == True):
                    print("grid full: ")
                    print (game.isGridFull())

                    print ("checkfinalgrid: ")
                    print(game.checkFinalGrid())

                    if (game.checkFinalGrid() == True): 
                        break

            print('Game Over. Thank you for playing ')
        

    else: # user wants to play a new game
        print("user choose new")
        userDifficulty = str(input("Please choose the level of difficulty (type easy, medium or hard): "))
        while ((userDifficulty != "easy") & (userDifficulty != "medium") & (userDifficulty != "hard")):
            userDifficulty = str(input("Input was invalid. \nPlease choose the level of difficulty (type easy, medium or hard): "))
        game.difficultyBoard(userDifficulty)
        game.printGrid()

        while True: 
            game.userInputValue() 

            if (game.isGridFull() == True):
                print("gri full: ")
                print (game.isGridFull())

                print ("checkfinalgri: ")
                print(game.checkFinalGrid())

                if (game.checkFinalGrid() == True): 
                    break

        print('Game Over. Thank you for playing ')


if __name__ == "__main__":
    main()

