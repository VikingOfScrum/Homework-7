#Simple Program check if a year is a leap year or not
def isLeapYear(inputYear):
    inputYear = int(inputYear)
    if inputYear %100 == 0:
        return("is not a Leap Year")
    elif inputYear %4 == 0:
        return("is a Leap Year")
    else:
        return("is not a Leap Year")

def main():

    for year in range(1804, 2400):
        print(isLeapYear(year))

if __name__ == '__main__':
    main()