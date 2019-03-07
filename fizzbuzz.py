def fizzbuzz(number):
    if divBy5(number) and divBy3(number):
        return 'fizzbuzz'
    if divBy3(number):
        return 'fizz'
    if divBy5(number):
        return 'buzz'
    else:
        return number


def divBy3(number):
    return number % 3 == 0


def divBy5(number):
    return number % 5 == 0