#List
fruits = ["apple","banana","cherry","apple"]
print("Original:",fruits)

fruits.append("date")
print("After append :", fruits)

fruits[1] ="mulberry"
print("After modify:", fruits)

print("Iterate:")
for f in fruits:
    print("-",f)

#Tuple

point = (3,4)
print("Tuple:",point)

print("x=",point[0],"y=",point[1])

t2 = point + (5,)
print("concat:",t2)

t3 = point * 2
print("Repeat:",t3)

print("Iterate tuple:")
for coord in point:
    print(coord)

#Dictionary

person = {"name":"Alice","Age":30}
print("Original:",person)

person["Nationality"] = "Indian"
person["city"] = "chennai"
print("Updated:",person)

print("Access:",person["name"])
print("keys:",list(person.keys()))
print("Values:",list(person.values()))

print("Iterate items:")
for key,value in person.items():
    print(f"{key},{value}")

removed = person.pop("city")
print("popped city:",removed)
print("After pop:",person)


#Set`

nums ={1,2,3,2}
print("Initial(no duplicates):",nums)

nums.add(4)
print("After add:", nums)

print("Membership test: 3 in nums?", 3 in nums)

print("Iterate set:")
for n in nums:
    print (n)


#Set Operation
A = {1,2,3}
B = {2,3,4}
print("Intersection:",A&B)
print("Difference A-B:",A-B)

z= lambda x :x*2
print(z(6))

# 1. List of student name-tuples
students = [("Alice", 85), ("Bob", 92), ("Cara", 78), ("Bob", 75)]
print("All students:", students)

# 2. Use set to get unique student names
names = {name for name, _ in students}
print("Unique names:", names)

# 3. Aggregate and compute average in a dict
grades = {name: [] for name in names}
for name, score in students:
    grades[name].append(score)

avg_scores = {name: sum(scores)/len(scores) for name, scores in grades.items()}
print("Average scores:", avg_scores)

# 4. Identify top performers (average >= 85)
top_students = [name for name, avg in avg_scores.items() if avg >= 85]
print("Top students:", top_students)



# Step 1: list of people showing up in order
visitors = ["Jim", "Bob", "Alice", "Bob", "Dave", "Eve"]
print("Visitors:", visitors)

# Step 2: set to record unique voters
voted = set()
for person in visitors:
    if person in voted:
        print(f"{person} - ALREADY VOTED")
    else:
        print(f"{person} - CAST VOTE")
        voted.add(person)

print("Total voters:", len(voted))
print("Voters list:", voted)



def find_longest_string(strings):
    longest = ""
    for s in strings:
        if len(s) > len(longest):
            longest = s
    return longest

def filter_greater_than_five(nums):
    return [n for n in nums if n > 5]

def find_duplicates(values):
    seen, duplicates = set(), []
    for v in values:
        if v in seen:
            duplicates.append(v)
        else:
            seen.add(v)
    return duplicates

# Demonstration
words = ["hi", "hello", "world!"]
numbers = [1, 6, 8, 3, 4, 8]
mix = [2, 3, 2, 5, 3]

print("Longest word:", find_longest_string(words))
print("Filtered (>5):", filter_greater_than_five(numbers))
print("Duplicates in mix:", find_duplicates(mix))













class Company:
    name = "XYZ Bank"
    turnover = 5000
    revenue = 1000
    num_employees = 100

    @classmethod
    def productivity(cls):
        return cls.turnover / cls.num_employees

c = Company()
print("Productivity:", Company.productivity())



class Car:
    def __init__(self, color, model, engine_type="Petrol"):
        self.color = color
        self.model = model
        self.engine_type = engine_type

    def accelerate(self):
        print(f"{self.model} is accelerating")

class ElectricCar(Car):
    def __init__(self, color, model, battery_kwh):
        super().__init__(color, model, engine_type="Electric")
        self.battery_kwh = battery_kwh

    def charge(self):
        print(f"{self.model} is charging")

ecar = ElectricCar("Blue", "Leaf", 40)
ecar.accelerate()
ecar.charge()




