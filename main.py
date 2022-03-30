from week0 import ship, matrix, swap, tree
from week1 import datalists, fibonacci
from week2 import factorial, math, palindrome

# ------------------------------------------------

border = "=" * 25
banner = f"\n{border}\nChoose one of the options: \n{border}"

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
  
# ------------------------------------------------

main_menu = [
    ["Math and Numbers", numbersmenu],
    ["Data and Words", datamenu],
    ["Visuals", visualmenu]
]

numbers_menu = [
    ["Fibonacci", fibonacci.fibonacci],
    ["Swap", swap.swap],
    ["Number Pad", matrix.matrix],
    ["Imperative GCD", math.findgcd],
    ["Oop GCD", math.gcdcall],
    ["Oop Factorial", factorial.factorial]    
]

data_menu = [
    ["Datalists", datalists.main],
    ["Palindrome", palindrome.P],
]

visual_menu = [
    ["Tree", tree.tree],
    ["Ship", ship.ship],
]

# ------------------------------------------------

def buildMenu(banner, options):
    print(banner)
    prompts = {0: ["Exit", None]}
    for op in options:
        index = len(prompts)
        prompts[index] = op
    for key, value in prompts.items():
        print(key, '->', value[0])
    choice = input("Type your choice> ")
    try:
        choice = int(choice)
        if choice == 0:
            return
        try:
            action = prompts.get(choice)[1]
            action()
        except TypeError:
            try:
                exec(open(action).read())
            except FileNotFoundError:
                print(f"File not found!: {action}")
    except ValueError:
        print(f"Not a number: {choice}")
    except UnboundLocalError:
        print(f"Invalid choice: {choice}")
    buildMenu(banner, options)
if __name__ == "__main__":
    menu()
