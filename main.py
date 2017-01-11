from bicycles import Bicycle, Customers, Shop

bikes = [       
Bicycle("speed demon", 8, 100, 4),
Bicycle("tarantula", 10, 350, 6),
Bicycle("wheelie", 9, 260, 7),
Bicycle("delta", 12, 700, 2),
Bicycle("trooper", 11, 880, 9),
Bicycle("mud buster", 15, 550, 12),
Bicycle("trainwreck", 20, 5000, 4),
]

shop_1 = Shop("Super Bikes", 20)

customers = [
Customers("John", 200),
Customers("Sarah", 500),
Customers("Don", 1000),
]

# Markup the bike cost by 20%
for bike in bikes:
    bike.cost = int(bike.cost * 1.2)

budget_bikes = {}
profit = 0
for customer in customers:
    print("Welcome to {}!!! See our inventory list below:".format(shop_1.name))
    for bike in bikes:
        print("${} - {} - qty:{}".format(bike.cost, bike.name, bike.quantity))
    print("\n{} can purchase any of these bikes with a ${} budget:".format(customer.name, customer.fund))
    for bike in bikes:
        if bike.cost <= customer.fund:
            print("${} - {} - {} lbs".format(bike.cost, bike.name,bike.weight))
            budget_bikes[bike.name] = bike.cost
    prompt = input("Please specify the name of the bike {} will buy: ".format(customer.name))
    if prompt in budget_bikes:
        bicycle_fund = customer.fund - budget_bikes[prompt]
        profit += budget_bikes[prompt]
        print("{} has bought the bike for ${} and has ${} remaining in their bicycle fund".format(customer.name, budget_bikes[prompt], bicycle_fund))
        print("The bike shop currently has made ${} profit\n".format(profit))
        for bike in bikes:
            if prompt in bike.name:
                bike.quantity -= 1
    else:
        print("No bike was specified, {} chose not to purchase a bicycle today".format(customer.name))

print ("Below is a final inventory count:")    
for bike in bikes:
        print("${} - {} - qty:{}".format(bike.cost, bike.name, bike.quantity))
