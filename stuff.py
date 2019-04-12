#my_stuff = { 'key1': 123, 'key2': 'value2', 'key3':{'123': [1,2,'grabMe']} }
#print(my_stuff['key3']['123'][2])

#booleans

#tuples - list but immutable
t = (1,2,3)
print(t[2])

#sets
x = set()
x.add(1)
x.add(2)
print(x)

s='django'
print(s[0], s[-1], s[:4], s[1:4], s[-2:], s[::-1])

l = [3,7,[1,4,'hello']]

l[2][2] = 'goodbye'
print(l)

d1 = {'simple_key': 'hello'}
d2 = {'k1':{'k2': 'hello'}}
d3 = {'k1':[{'nest_key': ['this is deep', ['hello']]}] }
print(d1['simple_key'], d2['k1']['k2'], d3['k1'][0]['nest_key'][1][0])

list = [1,1,1,1,1,2,2,2,2,3,3,3,3]
r = set(list)
print(r)

age = 4
name = 'Sammy'
print("Hello my name is {a} and i am {b} years old".format(a=age, b=name))
