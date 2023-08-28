offers = [input() for _ in range(int(input()))]
garden = [input() for _ in range(int(input()))]

values = {}
for val, products in (offer[1::].split(' = ') for offer in offers):
    for product in products:
        values[product] = int(val)

worth = 0
for line in garden:
    worth += sum(map(lambda k: values.get(k, 0), line))

print(f"${worth:,.0f}")
