

"""     warsal operation """
numbers = [1, 2, 3, 4, 2 ,33, 44,224,-1,2,22]

while (n := len(numbers)) > 0:
	print(n)
	print(numbers)
	print(numbers.pop())



numbers = [1, 2, 3, 4, 5]
if n :=len(numbers) >0:
	print(n)




while n := len(numbers) > 0:
	print(n)
	#print(numbers)
	print(numbers.pop())

number = [1,2,3,4,5,56,33,0, -2,2]
if (n := len(number) ) >0 :
    print(n)




sample_data = [
    {"userId": 1,  "name": "", "completed": False},
    {"userId": 1, "name": "", "completed": False},
    {"userId": 1,  "name": "ravan", "completed": True}
]
 


for i in sample_data:
    if name := i.get("name" ,""):
        print(name)

print(1111)
for i in sample_data:
    if (name := i.get("name" ,"")) == "ravan":
        print(name)




food = []
food1= list()

while (inp := input("enter food")) != "quit":
    print(inp)
    food.append(inp)
    food1.append(inp)


print(food)
print(food1)

