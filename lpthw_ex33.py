# Exercise 33
# While Loops

def loop_it(limit, stride):
    i = 0
    numbers = []
    while i < limit:
        print(f"At the top i is: {i}")
        numbers.append(i)

        i += stride
        print("Numbers now:", numbers)

        print(f"At the bottom i is: {i}")

    print("The numbers: ")

    for num in numbers:
        print(num)

loop_it(10, 2)
