# 1. file names will be run by exec(open("filename.py").read())
# 2. function references will be executed directly file.function()
# imports from other .py files
from week0 import ship
from week1 import datalists

# Main Menu
main_menu = [
    ["Factorial", "week2/factorial.py"],
    ["Palindrome", "week2/palindrome.py"],
    ["Math Functions", "week2/math.py"]
]
# Submenu list of [Prompt, Action]
# Works similarly to main_menu
sub_menu = [
    ["Fibonacci", "week1/fibonacci.py"],
    ["Datalists", datalists.main],
    ["Swap", "week0/swap.py"],
    ["Tree", "week0/tree.py"],
    ["Ship", ship.ship],
    ["Keypad", "week0/keypad.py"]
]
border = "=" * 25
banner = f"\n{border}\nChoose one of the options: \n{border}"
def menuc():
    title = "Class Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Submenu", submenuc])
    m = questy.Menu(title, menu_list)
    m.menu()
def submenuc():
    title = "Class Submenu" + banner
    m = questy.Menu(title, sub_menu)
    m.menu()
def menu():
    title = "Tanay Rayavarapu's Menu" + banner
    menu_list = main_menu.copy()
    menu_list.append(["Previous Tasks", submenu])
    buildMenu(title, menu_list)
def submenu():
    title = "Function Submenu" + banner
    buildMenu(title, sub_menu)
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
