#print to screen
print("Python is fun!")

#example of using a variables
message = "Python is fun!"
print(message)

#capitalizes name
name = "brittany cook"
print(name.title())

first_name = "brittany"
last_name = "cook"
full_name = f"{first_name} {last_name}"
print(full_name)
print(f"My name is, {full_name.title()}!")

#Manipulating Lists
states = ['California', 'New York', 'Nevada']
print(states)

print(states[0])

#change an element
states[0] = 'Texas'
print(states)

#insert an element
states.insert(0, 'Washington')
print(states)

#loops
states = ['California', 'New York', 'Nevada']
for state in states:
    print(state)
print("All states in list printed")

#dictionaires
plants = {'color': 'blue', 'height' : 10}
print(plants['color'])

def weather():
    """Find out the weather"""
    answer = input("How is the weather")
    print(answer)
weather()
