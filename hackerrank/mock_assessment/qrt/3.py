fruit = ['banana', 'apple']
price = [100, 200]

zipped = [(fruit, price) for fruit, price in zip(fruit, price) if 99 < price < 101]
print(zipped)
print(sorted(zipped, key=lambda x: x[1], reverse=True))
