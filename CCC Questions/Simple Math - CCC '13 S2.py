w = int(input())
n = int(input())

cars = [0,0,0]
counter = 0
for i in range(n):
    cars.append(int(input()))
    if sum(cars) > w:
        break
    else:
        cars.pop(0)
        counter += 1
print(counter)