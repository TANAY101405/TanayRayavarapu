class factorial:
  def __call__(self, num):
    final = 1
    for i in range(1, num + 1):
      final = final * i
    return final

factorial = factorial()
number = input("Number to find factorial of: ")
number = int(number)
print("Factorial of ", number, "is",   factorial(number))

# Hack 3


# Hack 4
