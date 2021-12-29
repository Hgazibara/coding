import collections

shoes = int(input())
shoe_sizes = map(int, input().split())
customers = int(input())

shoes_inventory = collections.Counter(shoe_sizes)
income = 0

for i in range(customers):
    shoe_size, price = map(int, input().split())
    
    if shoe_size not in shoes_inventory:
        continue
        
    shoes_inventory[shoe_size] -= 1
    income += price
    
    if shoes_inventory[shoe_size] == 0:
        shoes_inventory.pop(shoe_size)

print(income)
