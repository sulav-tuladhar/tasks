## Find & Replace in text file
f = open("hello.txt", "r")
line = f.read()
print(line)
print(line.replace("Hello", "Hi"))

## Calculate Word Frequency in a text file
f = open("hello.txt", "r")
line = f.read()
list = line.split()
countDist = {}
for item in list:
    if item in countDist:
        countDist[item] += 1
    else:
        countDist[item] = 1
print(countDist)
    
## Merge Two Text Files Line by line
with open('fruits.txt', 'r+') as fruit_file:
   fruit_lines = fruit_file.readlines()
   
with open('hello.txt', 'r+') as greeting_file:
    greeting_lines = greeting_file.readlines()
    
with open('joinedFile.txt', 'w') as joined_file:
    for index, item in enumerate(fruit_lines):
        joined_file.write(item.strip() + " " + greeting_lines[index].strip() + "\n")
        # print('item is >> ', item.strip() + " " + greeting_lines[index].strip())
    


