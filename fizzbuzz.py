def fizzbuzz(number):
    if number % 5 == 0 and number % 3 == 0:
        return 'fizzbuzz'
    if number % 3 == 0:
        return 'fizz'
    if number % 5 == 0:
        return 'buzz'
    else:
        return number