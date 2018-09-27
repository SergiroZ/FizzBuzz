#
# Напишите программу, которая выводит на экран числа от 1 до 100.
# При этом вместо чисел, кратных трем, программа должна выводить слово «Fizz»,
# а вместо чисел, кратных пяти — слово «Buzz».
# Если число кратно и 3, и 5, то программа должна выводить слово «FizzBuzz»

print("******* 1 *******")
for x in range(1, 101):
    if x % 3 and x % 5 == 0:
        print("FizBiz")
    elif x % 3 == 0:
        print("Fiz")
    elif x % 5 == 0:
        print("Biz")
    else:
        print("x=", x)
print("***************\n")

print("******* 2 *******")


def main():
    i = 0
    value = ''
    while i < 100:
        i += 1
        if i % 15 == 0:
            value = 'FizzBuzz'
        elif i % 3 == 0:
            value = 'Fizz'
        elif i % 5 == 0:
            value = 'Buzz'
        else:
            value = str(i)
        print(value)
    return 0;


main()
print("***************\n")

print("******* 3 *******")
print([['FizzBuzz', 'Fizz', 'Buzz'][
           max(enumerate([not num % 15, not num % 3, not num % 5]),
               key=lambda v: v[1])[0]]
       if sum([not num % 15, not num % 3, not num % 5])
       else num for num in range(1, 101)])
print("***************\n")

print("******* 4 *******")
print(list(map(lambda _: ('Fizz' * (not _ % 5) + 'Buzz' * (not _ % 3)) or _, range(1, 101))))
print("***************\n")

print("******* 5 *******")
for number in range(1, 101):
    print((number, 'Fizz', 'Buzz', 'FizzBuzz')[(not number % 3) + (not number % 5) * 2])
print("***************\n")

print("******* 6 *******")
print(list((not x % 3) * 'Fizz' + (not x % 5) * 'Buzz' or x for x in range(1, 101)))
print("***************\n")

print("******* 7 *******")
print([(not x % 3) * 'Fizz' + (not x % 5) * 'Buzz' or x for x in range(1, 101)])
print("***************")
