
def checkNumber(i):
    if i % 3 == 0:
        return("Fizz")

def main():
    for integer in range(100):
        checkNumber(integer)

if __name__ == '__main__':
    main()