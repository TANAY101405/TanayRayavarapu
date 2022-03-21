import time
ans = True
while ans:
  print("""
    Repl Main Menu:
    1. Week 0
    2. Week 1
    3. Exit/Quit
    """)
  mm = input("Select which week challenge: ")
  if mm == "1":
      print("""
      Repl Menu:
      1. Ship Pattern
      2. Build a Christmas Tree
      3. Number Swap
      4. Matrix Numberpad
      5. Exit/Quit
      """)
      ans = input("What would you like to do? ")
  # WEEK 1 TASKS ---------------------------------------------
      def ocean_print():
        # print ocean
        print(ANSI_CLEAR_SCREEN, ANSI_HOME_CURSOR)
        print("\n\n\n\n")
        print(OCEAN_COLOR + "  " * 35)
      # print ship with colors and leading spaces
      def ship_print(position):
          print(ANSI_HOME_CURSOR)
          print(RESET_COLOR)
          sp = " " * position
          print(sp + "    |\   ")
          print(sp + "    |/   ")
          print(SHIP_COLOR, end="")
          print(sp + "\__ |__/ ")
          print(sp + " \____/  ")
          print(RESET_COLOR)
      # ship function, iterface into this file
      def ship():
          # only need to print ocean once
          ocean_print()
          # loop control variables
          start = 0  # start at zero
          distance = 60  # how many times to repeat
          step = 2  # count by 2
          # loop purpose is to animate ship sailing
          for position in range(start, distance, step):
              ship_print(position)  # call to function with parameter
              time.sleep(.1)
          # Generating Pole Shape
      def poleShape(n):
        for i in range(n):
            for j in range(n-1):
                print(' ', end=' ')
            print('* * *')
      def triangleShape(n):
        for i in range(n):
            for j in range(n-i):
                print(' ', end=' ')
            for k in range(2*i+1):
                print('*',end=' ')
            print()
      # Boat animation
      if ans == "1":
        ANSI_CLEAR_SCREEN = u"\u001B[2J"
        ANSI_HOME_CURSOR = u"\u001B[0;0H\u001B[2"
        OCEAN_COLOR = u"\u001B[44m\u001B[2D"
        SHIP_COLOR = u"\u001B[32m\u001B[2D"
        RESET_COLOR = u"\u001B[0m\u001B[2D"
        ship()
      # Christmas Tree
      elif ans == "2":
      # Input and Function Call
        row = int(input('Enter number of rows: '))
        triangleShape(row)
        triangleShape(row)
        poleShape(row)
      # Number Swapper
      elif ans == "3":
        num1 = float(input("Choose first number: "))
        num2 = float(input("Choose second number: "))
        holder = num1
        num1 = num2
        num2 = holder
        print("After swap...")
        print("number 1: " + str(num1))
        print("number 2: " + str(num2))
      # Matrix Numberpad
      elif ans == "4":
        matrix = []
        for i  in range (1):
          matrix.append([])
          for j in range (1,4):
            matrix [i].append(j)
        matrix2 = []
        for i in range (1):
          matrix2.append([])
          for k in range (4,7):
            matrix2 [i].append(k)
        matrix3 = []
        for i in range (1):
          matrix3.append ([])
          for g in range (7,10):
            matrix3 [i].append(g)
        print(matrix)
        print(matrix2)
        print(matrix3)
        def print_matrix1(matrix):
          print("lol")
          for i in range(len(matrix)):
            for j in range(len(matrix[i])):
              print(matrix[i][j], end=" ")
            print()
      else:
        ans = False
        print("See you later!")
  # END OF WEEK 1 TASKS --------------------------------
  # WEEK 2 TASKS ---------------------------------------------
  if mm == "2":
    print("""
      Repl Menu:
      1. InfoDB Lists
      2. InfoDB Loops
      3. Fibonacci
      4. Exit/Quit
      """)
    ans = input("What would you like to do? ")
    # InfoDB lists
    if ans == "1":
      def print_data(n):
        print(InfoDb[n]["Name"])  # print name
        print("\t", "Birth: ", end="")
        print(InfoDb[n]["Birth"])
        print("\t", "Siblings: ", end="")  # \t is a tab indent, end="" make sure no return occurs
        print(InfoDb[n]["Siblings"])
        print("\t", "Hobbies: ", end="")
        print(", ".join(InfoDb[n]["Hobbies"]))  # join allows printing a string list with separator
        print()
      # Creating Database
      InfoDb = []
      InfoDb.append({
                     "Name": "Tanay Rayavarapu",
                     "Birthday": "October 14",
                     "Siblings": "Yes",
                     "Hobbies":["Reading", "Swimming", "Driving", "Taekwondo"]
                    })
      InfoDb.append({
                     "Name": "Rishi Peddakama",
                     "Birthday": "April 2",
                     "Siblings": "Yes",
                     "Hobbies":["Coding", "Math", "Science", "Reading"]
                    })
      InfoDb.append({
                     "Name": "Noah Jeng",
                     "Birthday": "February 14",
                     "Siblings": "Yes",
                     "Hobbies":["Soccer", "Driving", "Listening to Music", "Gaming"]
                    })
      InfoDb.append({
                     "Name": "Arnav Palkiwala",
                     "Birthday": "November 17",
                     "Siblings": "No",
                     "Hobbies":["Tennis", "Travels", "Basketball", "Codes"]
                    })
      for i in range(len(InfoDb)):
        print_data(i)
    if ans == "2":
      InfoDbLoop = []
      InfoDbLoop.append({
                     "Name": "Tanay Rayavarapu",
                     "Birthday": "October 14",
                     "Siblings": "Yes",
                     "Hobbies":["Reading", "Swimming", "Driving", "Taekwondo"]
                    })
      InfoDbLoop.append({
                     "Name": "Rishi Peddakama",
                     "Birthday": "April 2",
                     "Siblings": "Yes",
                     "Hobbies":["Coding", "Math", "Science", "Reading"]
                    })
      InfoDbLoop.append({
                     "Name": "Noah Jeng",
                     "Birthday": "February 14",
                     "Siblings": "Yes",
                     "Hobbies":["Soccer", "Driving", "Listening to Music", "Gaming"]
                    })
      InfoDbLoop.append({
                     "Name": "Arnav Palkiwala",
                     "Birthday": "November 17",
                     "Siblings": "No",
                     "Hobbies":["Tennis", "Travels", "Basketball", "Codes"]
                    })
      def print_data(n):
        print(InfoDbLoop[n]["Name"])  # print name
        print("\t", "Sport: ", end="")
        print(InfoDbLoop[n]["Sport"])
        print("\t", "Age: ", end="")  # \t is a tab indent, end="" make sure no return occurs
        print(InfoDbLoop[n]["Age"])
        print("\t", "Hobbies: ", end="")
        print(", ".join(InfoDbLoop[n]["Hobbies"]))  # join allows printing a string list with separator
        print()
      # For Loop
      def for_loop():
        for n in range(len(InfoDbLoop)):
          print_data(n)
      # While Loop
      # while loop contains an initial n and an index incrementing statement (n += 1)
      def while_loop(n):
        while n < len(InfoDbLoop):
          print_data(n)
          n += 1
        return
      # Recursion
      # recursion simulates loop incrementing on each call (n + 1) until exit condition is met
      def recursive_loop(n):
        if n < len(InfoDbLoop):
          print_data(n)
          recursive_loop(n + 1)
        return # exit condition
      print("For Loop Print")
      for_loop()
      print("While Loop Print")
      while_loop(0)
      print("Recursion")
      recursive_loop(0)
    # Fibonacci
    if ans == "3":
      try:
        num = int(input("enter a number for fibonacci:"))
        assert num > 0
        n1, n2 = 0, 1
        print("Fibonacci Series:", n1, n2, end=" ")
        for int in range(2, num):
          n3 = n1 + n2
          n1 = n2
          n2 = n3
          print(n3, end=" ")
        print()
      except AssertionError :
        print("input positive value")
    # Breakout
    else:
      ans = False
      print("See you later!")
  # END OF WEEK 2 TASKS --------------------------------
  # Main Menu Breakout
  else:
      ans = False
      print("See you later!")