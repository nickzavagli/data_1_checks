# Print Hello World!
print("Hello world!")

# Create a list with several values, print one of these values.
bearlist = ["Polar", "Grizzly", "Black", "Panda"]
print(bearlist[0])

# Create a dictionary with two keys and two values. Print one of the values.
beardictionary = {"Type": "Polar", "Max Height": "9 feet 10 inches"}
print(beardictionary["Max Height"])

# Create a tuple with 4 values. Print one of them.
bear = ("Polar Bear", "Grizzly Bear", "Black Bear", "Panda Bear")
print(bear[1])

beardata = [
    {
    "type" : "Polar Bear",
    "max weight (lbs)" : 1800,
    "max height (in)" : 120,
    "max population" : 40000},
    {
    "type" : "Grizzly Bear",
    "max weight (lbs)" : 1000,
    "max height (in)" : 108,
    "max population" : 110000},
    {
    "type" : "Black Bear",    
    "max weight (lbs)" : 880,
    "max height (in)" : 72,
    "max population" : 600000},
    {
    "type" : "Panda Bear",
    "max weight (lbs)" : 250,
    "max height (in)" : 72,
    "max population" : 1864,
    }
]

print(beardata[3])