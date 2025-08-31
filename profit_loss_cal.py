#WAP which take SP and CP from user and find P or loss, if loss print oss amount if profit print profit amout
selling_price = int(input("Enter selling price : "))
cost_price = int(input("Enter cost price : "))

if selling_price > cost_price:
    print(f"Congrats!! you earn a profit of {selling_price-cost_price} Rs.")
elif selling_price == cost_price:
    print(f"Good try!! NPNL")
else:
    print(f"Ops!! you loss {cost_price-selling_price} Rs.")
