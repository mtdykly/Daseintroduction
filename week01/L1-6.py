import random
w = random.randint(1, 100)
x = random.randint(1, 100)
y = random.randint(1, 100)
z = random.randint(1, 100)

if w < x:
    w, x = x, w
if x < y:
    x, y = y, x
if y < z:
    y, z = z, y
if w < x:
    w, x = x, w

print(f"从大到小排序后的结果为：{w}, {x}, {y}, {z}")