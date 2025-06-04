a = 2323
b = 23

if b > a:
  print("b is greater than a")
else:
  print("b is not greater than a")

print(bool("Programming"))
print(bool(23))

x = "Programming"
y = 15
print(bool(x))
print(bool(y))

bool("")
bool(())

class pp():
  def __len__(self):
    return 0

lab = pp()
print(bool(lab))

def lab() :
  return True

print(lab())

def lab() :
  return True

if lab():
  print("YES!")
else:
  print("NO!")

x = 23
print(isinstance(x, int))

print(90+23/23-44*1)

thislist = ["KBTU","PP2","Programming"]
print(len(thislist))

mylist = ["KBTU","PP2","Programming"]
print(type(mylist))

thislist = list(("KBTU","PP2","Programming"))
print(thislist)

thislist = ["KBTU","PP2","Programming","Calculus","Python","C""Java"]
print(thislist[2:5])

thislist = ["KBTU","PP2","Programming","Calculus","Python","C""Java"]
print(thislist[:4])

thislist = ["apple", "banana", "cherry"]
thislist[1] = "b"
print(thislist)

thislist = ["KBTU","PP2","Programming"]
thislist.insert(2, "w")
print(thislist)

thislist = ["KBTU","PP2","Programming"]
thislist.append("o")
print(thislist)

thislist = ["KBTU","PP2","Programming"]
thislist.insert(1, "o")
print(thislist)

thislist = ["KBTU","PP2","Programming"]
chem = ["H", "CO2", "CH4"]
thislist.extend(chem)
print(thislist)

thislist = ["KBTU","PP2","Programming"]
thislist.pop(1)
print(thislist)

thislist = ["KBTU","PP2","Programming"]
del thislist[0]
print(thislist)

thislist = ["KBTU","PP2","Programming"]
del thislist

thislist = ["KBTU","PP2","Programming"]
thislist.clear()
print(thislist)

thislist = ["KBTU","PP2","Programming"]
for x in thislist:
  print(x)

  thislist = ["KBTU","PP2","Programming"]
for i in range(len(thislist)):
  print(thislist[i])

  thislist = ["KBTU","PP2","Programming","Calculus","Python","C""Java"]
i = 0
while i < len(thislist):
  print(thislist[i])
  i = i + 1

  list1 = ["a", "b", "c"]
list2 = [1, 2, 3]

list3 = list1 + list2
print(list3)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

for x in list2:
  list1.append(x)

print(list1)

list1 = ["a", "b" , "c"]
list2 = [1, 2, 3]

list1.extend(list2)
print(list1)

thisdict = {
  "PP": "Kbtu",
  "ITM": "Student",
  "year": 2025
}

a = 255
b = 23
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

a = 255
b = 23
print("A") if a > b else print("B")

a = 255
b = 23
c = 50
if a > b and c > a:
  print("Both conditions are True")

a = 255
b = 23
c=50
if a > b or a > c:
  print("At least one of the conditions is True")

a = 255
b = 23
if not a > b:
  print("a is NOT greater than b")
  
x = 41
if x > 10:
  print("Above ten,")
  if x > 20:
    print("and also above 20!")
  else:
    print("but not above 20.")

a = 255
b = 23
if b > a:
  pass

day = 3
match day:
  case 1:
    print("Mon")
  case 2:
    print("Tues")
  case 3:
    print("Wednes")
  case 4:
    print("Thurs")
  case 5:
    print("Fri")
  case 6:
    print("Satur")
  case 7:
    print("Sun")

day = 2
match day:
  case 6:
    print("Saturday")
  case 7:
    print(" Sunday")
  case _:
    print("Looking forward to the Weekend")

day = 5
match day:
  case 1 | 2 | 3 | 4 | 5:
    print("Today is a weekday")
  case 6 | 7:
    print("I love weekends!")

month = 5
day = 4
match day:
  case 1 | 2 | 3 | 4 | 5 if month == 4:
    print("A weekday in April")
  case 1 | 2 | 3 | 4 | 5 if month == 5:
    print("A weekday in May")
  case _:
    print("No match")

i = 1
while i < 23:
  print(i)
  i += 1

i = 1
while i < 23:
  print(i)
  if i == 4:
    break
  i += 1

i = 0
while i < 23:
  i += 1
  if i == 3:
    continue
  print(i)

i = 1
while i < 23:
  print(i)
  i += 1
else:
  print("i is less than 23")

uni = ["KBTU","PP2","Programming"]
for x in uni:
  print(x)

for x in "KBTU":
  print(x)

uni = ["KBTU","PP2","Programming"]
for x in uni:
  print(x)
  if x == "PP2":
    break

uni = ["KBTU","PP2","Programming"]
for x in uni:
  if x == "PP2":
    break
    print(x)

uni = ["KBTU","PP2","Programming"]
for x in uni:
  if x == "PP2":
    continue
    print(x)

for x in range(23):
  print(x)

for x in range(20, 23):
  print(x)

for x in range(20, 30, 23):
  print(x)

for x in range(20,23):
  print(x)
else:
  print("thats all")

for x in range(7):
  if x == 3: break
  print(x)
else:
  print("Thats all")

me = ["Ulykpanova", "Dilnaz", "ITM"]
uni = ["KBTU","PP2","Summer"]

for x in me:
  for y in uni:
    print(x, y)

for x in [0, 1, 2]:
  pass

