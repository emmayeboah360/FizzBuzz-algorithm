def fizzBuzz():
    request = int(input("Enter a number: "))
    # if the number is divisible by 3 and divisible by 5
    if request % 3 == 0 and request % 5 == 0:
        # it should return fizzbuzz
        return "FizzBuzz"

    # if it is divisible by 3
    if request % 3 == 0:
        return "Fizz"

    # if it is divisible by 5
    if request % 5 == 0:
        return "Buzz"
# if all the above do not work out
    else:
        return request


print(fizzBuzz())
