#map

def square(number):
    return number**2

def splicer(string):
    if len(string) %2 == 0:
        return 'even'
    else:
        return string[0]

my_nums = [1,2,3,4,5]
names = ['andy', 'pandy', 'boobies']

for item in map(square, my_nums):
    print(item)

list(map(square, my_nums))
list(map(splicer, names))


## filter works with boolean
def check_even(num):
    return num %2 ==0

mynums = [1,2,3,4,5,6]

for n in filter(check_even, mynums):
    print n

#lambdas

square = lambda num:  num **2
print(square(5))

print(list(map(lambda num: num**2, mynums)))

