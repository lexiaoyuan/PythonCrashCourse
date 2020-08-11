sandwich_orders = ['name1', 'pastrami', 'name2', 'pastrami', 'name3', 'pastrami']
finished_sandwiches = []

print("Pastrami is sold out")

while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')

for sandwich_order in sandwich_orders:
    print("I made your " + sandwich_order + " sandwich")
    finished_sandwiches.append(sandwich_order)

print("The sandwiches are all done:")
for finished_sandwich in finished_sandwiches:
    print(finished_sandwich)
