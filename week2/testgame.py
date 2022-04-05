def domath():
  operation = input("What operation do you want? ")
  num1 =  float(input("What is the first number?"))
  num2 = float(input("What is the second number?"))
  
  
  def multiply():
    return num1*num2
  
  def division():
    return num1/num2
  
  def addition():
    return num1+num2
  
  def subtraction():
    return num1-num2
  
  if operation=="*":
    answer = multiply()
    print(answer)
  
  elif operation=="/":
    answer = division()
    print(answer)
  
  elif operation=="+":
    answer = addition()
    print(answer)
  
  elif operation=="-":
    answer = subtraction()
    print(answer)
  
  
  
