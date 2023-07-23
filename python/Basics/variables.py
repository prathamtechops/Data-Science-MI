a = 10
b = 2

print(a + b)

name = "Nidhi"

print(name.upper())
magicians = ["alice", "david", "carolina"]
for magician in magicians:
    print(magician, end=" ")

numbers = list(range(1, 6))
print(numbers)

with open("test.text", "a") as f:
    f.write("Hello World")
with open("test.text", "r") as f:
    print(f.read())
