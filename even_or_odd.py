# WAP to give number is even or odd

num = int(input("Enter a number : ")) #by default iput function OP is string type so convert it in int
if num%2 == 0: #if num is div by 2 and get remainder as 0 means its even
      print(f"{num} is EVEN !!")
else: #if not give remainder 0 means odd
    print(f"{num} is OOD !!")