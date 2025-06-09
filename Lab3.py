from os import name


def lab3():
  print("Hello from lab3")
lab3()

def lab3(theme):
   print(theme+" lesson")
lab3("lambda")
lab3("function")
lab3("objects")

def lab3(theme, lesson):
  print(theme + " " + lesson)

lab3("lambda", "class")

def lab3(*topics):
  print("The list of topics is  " + topics[2])

lab3("Lambda", "Functions", "Objects")

def lab3(**topics):
  print("The topic is  " + topics["lesson"])

lab3(topics = "Function", lesson = "class")

def lab3(subjects):
  for x in subjects:
    print(x)

topics = ["Lambda", "Functions", "Objects"]

lab3(topics)

def lab3(x):
  return 5 * x

print(lab3(3))
print(lab3(5))
print(lab3(9))

def lab3():
  pass

def lab3(x, /):
  print(x)

lab3(3)

def lab3(x):
  print(x)

lab3(x = 3)

def lab3(*, x):
  print(x)

lab3(x = 3)

def lab3(a, b, /, *, c, d):
  print(a + b + c + d)

lab3(5, 6, c = 7, d = 8)

def lab_recursion(k):
  if(k > 0):
    result = k + lab_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Lab Results:")
lab_recursion(6)

x = lambda a : a + 10
print(x(5))

x = lambda a, b : a * b
print(x(5, 6))

x = lambda a, b, c : a + b + c
print(x(23, 23, 2))

def lab3(n):
  return lambda a : a * n

def lab3(n):
  return lambda a : a * n

mydoubler = lab3(2)

print(mydoubler(23))

def lab3(n):
  return lambda a : a * n

mytripler = lab3(3)

print(mytripler(23))

def lab3(n):
  return lambda a : a * n

mydoubler = lab3(2)
mytripler = lab3(3)

print(mydoubler(23))
print(mytripler(23))

class lab3:
  x=23

o1 = lab3()
print(o1.x)

class lab:
  def __init__(name,number, topic):
    name.number = number
    name.topic = topic

o1 = lab(3, "Objects")

print(o1.number)
print(o1.topic)

class lab:
  def __init__(name,number, topic):
    name.number = number
    name.topic = topic

o1 = lab(3, "Objects")

print(o1)

class lab:
  def __init__(name,number, topic):
    name.number = number
    name.topic = topic

  def __str__(name):
    return f"{name.number}({name.topic})"
  
o1 = lab(3, "Objects")

print(o1)

o1.number=23

del o1.number

del o1

class lab:
  pass

class lab:
  def __init__(name,number, topic):
    name.number = number
    name.topic = topic

  def printname(name):
    print(name.number, name.topic)

x = lab(3, "Objects")
x.printname()

class pp(lab):
  pass

x=pp(4,"lambda")
x.printname()

class pp(lab):
  def __init__(name, number, topic):
    super().__init__(number, topic)
    name.semestr = "summer" 
  x=pp("Objects","summer")
  
class pp(lab):
  def __init__(name, number, topic):
    super().__init__(number, topic)
    name.semestr = "summer" 
  def welcome(pp):
    print("Welcome to lab number ", name.number,"topic is", name.topic ,"on",name.semestr ,"semestr")

    
