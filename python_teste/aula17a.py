num = [2, 5, 6, 1]
num[2] = 3
num.append(7)
num.sort(reverse=True)
num.insert(2, 0)
num.pop(2)
num.remove(2)
print(num)
print(f'Essa lista tem {len(num)} elementos.')