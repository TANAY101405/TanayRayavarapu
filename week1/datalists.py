# Datalists hack task -------------------------------
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

# Datalist to print using the three loops - for - while - recursion

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
  print("\t", "Birthday: ", end="")
  print(InfoDbLoop[n]["Birthday"])
  print("\t", "Siblings: ", end="")  # \t is a tab indent, end="" make sure no return occurs
  print(InfoDbLoop[n]["Siblings"])
  print("\t", "Hobbies: ", end="")
  print(", ".join(InfoDbLoop[n]["Hobbies"]))  # join allows printing a string list with separator
  print()


# Dataloops hack task ------------------------------------

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

def main():
  print("For Loop")
  for_loop()
  print("While loop")
  while_loop(0)
  print("Recursion")
  recursive_loop(0)


