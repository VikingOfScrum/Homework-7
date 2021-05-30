
def checkNumber(i):
    if i % 3 == 0 and i % 5 == 0:
        return("FizzBuzz")
    elif i % 3 == 0:
        return("Fizz")
    elif i % 5 == 0:
        return("Buzz")
    else:
        return(i)

def main():
    for integer in range(100):
        print(checkNumber(integer))

if __name__ == '__main__':
    main()