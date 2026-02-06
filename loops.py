#WHILE LOOP
from variables import language

i = 1
while i < 6:
    print(i)
    i += 1  #Note: remember to increment i, or else the loop will continue forever.


print()

count = 10
while count <=15: # OR (< 16)
    print(count)
    count += 1 # Increment

print()

j = 105
while j >=100: # Consider placing the last number to be displayed
    print(j)
    j -= 1

print()


# FOR LOOP
for num in range(20, 26):
    print(num)

print()

# Use of for loop i array, list , tuple
languages = ["Pyhon", "Java", "C++", "Javascript"]

for lang in languages:
    print(lang)