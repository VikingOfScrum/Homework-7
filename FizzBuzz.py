
def checkNumber(i):
    if i % 3 == 0:
        return("Fizz")
    elif i % 5 == 0:
        return("Buzz")

def main():
    for integer in range(100):
        checkNumber(integer)

if __name__ == '__main__':
    main()