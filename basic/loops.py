
"""
x=0
while x<5:
    print("Not there Yet, x=" + str(x))
    x=x+1
print("x=" + str(x))

#for loop
for x in range(5):
    print(x)

values = [ 23, 52, 59, 37, 48 ]
sum = 0
length = 0
for value in values:
    sum += value
    length += 1

print("Total sum: " + str(sum) + " - Average: " + str(sum/length))
"""

product=1
for n in range(1,10):
    product=product*n
print(product)

def to_celcius(x):
    return (x-32)*5/9
for i in range(0,101,10):
    print(i, to_celcius(i))

for left in range(7):
    for right in range(left,7):
        print("[" + str(left) + "|" + str(right) + "]", end =" ")
    print()

teams =['Bangladesh', 'Brazil', 'Argentina', 'Germany']
for home in teams:
    for away in teams:
        if home != away:
            print(home + " vs " + away)
print("I am reading")
print("I am reading")
print("I am reading")
print("I am reading")
print("I am reading")
print("I am reading")
print("I am reading")
print("I am reading")
print("I am reading")
print("I am reading")