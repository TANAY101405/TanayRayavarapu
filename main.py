from week0 import ship, matrix, swap, tree
from week1 import datalists, fibonacci
from week2 import factorial, math, palindrome, numberguesser, testgame, testgame1

#import functions from each week folder

# ------------------------------------------------

border = "=" * 25
banner = f"\n{border}\nChoose one of the options: \n{border}"

#define each menu type (weeks 0-2) and the main menu
def menu():
    title = "Tanay Rayavarapu's Menu" + banner
    buildMenu(title, main_menu)
   
  
def numbersmenu():
    title = "Function Submenu" + banner
    buildMenu(title, numbers_menu)

def datamenu():
  title = "Function Submenu" + banner
  buildMenu(title, data_menu)

def visualmenu():
  title = "Function Submenu" + banner
  buildMenu(title, visual_menu)

def gamesmenu():
  title = "Function Submenu" + banner
  buildMenu(title, games_menu)
  
  
# ------------------------------------------------

#define submenus with each .py file
main_menu = [
    ["Math and Numbers", numbersmenu],
    ["Data and Words", datamenu],
    ["Visuals", visualmenu],
    ["Mini-Games", gamesmenu]
]

numbers_menu = [
    ["Fibonacci", fibonacci.fibonacci],
    ["Swap", swap.swap],
    ["Number Pad", matrix.matrix],
    ["Oop GCD", math.gcdcall],
    ["Oop Factorial", factorial.factorialcall]    
]

data_menu = [
    ["Datalists", datalists.main],
    ["Palindrome", palindrome.palindromecall],
]

visual_menu = [
    ["Tree", tree.tree],
    ["Ship", ship.ship],
]

games_menu = [
    ["Number Guesser", numberguesser.guesser],
    ["Calculator", testgame.domath],
    ["RockPaperScissors", testgame1.game],
]

# ------------------------------------------------

def buildMenu(banner, options):
    # header for menu
    print(banner)
    # build a dictionary from options
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op

    # print menu or dictionary
    for key, value in prompts.items():
        print(key, '->', value[0])

    # get user choice
    choice = input("Type your choice> ")

    # validate choice and run
    # execute selection
    # convert to number
    try:
        choice = int(choice)
        if choice == 0:
            # stop
            return
        try:
            # try as function
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:  # try as playground style
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
            # end function try
        # end prompts try
    except ValueError:
        # not a number error
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        # traps all other errors
        print(f"Invalid choice: {choice}")
    # end validation try

    buildMenu(banner, options)  # recursion, start menu over again
if __name__ == "__main__":
    menu()
