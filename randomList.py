import random

low = -10
high = 20
listLen = 20

result = []

for i in range(listLen):
    result.append(random.randrange(low,high))

print result

