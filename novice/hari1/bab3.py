print ('Nama saya Waid')

print('___________________')
#operators +, -, * and /
print (2 +2)
print (50 - 5*6)
print ((50 - 5*6) / 4)
print (8 / 5)
print (17 / 3 )

print('___________________')
# / and //
print (17 // 3)
print (17 % 3)

print('___________________')
# ** operator
print (5 * 3 + 2)
print (5 ** 2)
print (2 ** 7)

print('___________________')
# a frickin variable
width = 20
height = 5 * 9
print (width * height)

print('___________________')
#mixed operator
print ((4 * 3.75) - 1)

print('___________________')
# (_) var
tax = 12.5 / 100
price = 100.50

print (price * tax)
_ = (price * tax)
print (price + _)
_ = (price + _)
print (round(_, 2))

print('___________________')
# freakin strings
print ('spam eggs')
print ('doesn\'t')
print ("doesn't")
print ('"Yes," they said.')
print ("\"Yes,\" they said.")
print ('"Isn\'t," they said.')

print('___________________')
print ('"Isn\'t," they said.')
print ('"Isn\'t," they said.')
s = 'First line.\nSecond line.'
s # without print(), \n is included in the output. but how d f it can freakin work and make an output 'First line.\nSecond line.'
print (s)

print('___________________')
#print('C:\some\name')
print(r'C:\some\name')

print('___________________')
print("""\
Usage: thingy [OPTIONS]
     -h                        Display this usage message           ss             aa
     -H hostname               Hostname to connect to               sa             s
     -H hostname a              Hostname to connect to db           AS             s
""")

print('___________________')
# 3 times 'un', followed by 'ium'
print (3 * 'un' + 'ium')
print ('Py' 'thon')

print('___________________')
text = ('Put several strings within parentheses'
'to have them joined together.')
print (text)

print('___________________')
prefix = 'Py'
print(prefix + ('thon'))

print('___________________')
#indexed string
word = 'Python'
print (word[0])
print (word[5])
print (word[-1])
print (word[-2])
print (word[-6])

print('___________________')
#index slicing
print (word[0:2])
print (word[2:5])
print (word[:2] + word[2:])
print (word[:4] + word[4:])
print (word[:2])
print (word[4:])
print (word[-2:])

print('___________________')
print (word[4:42])
print (word[42:])

print('___________________')
print ('J' + word[1:])
print (word[:2] + 'py')

y = 'supercalifragilisticexpialidocious'
print (len(y))

print('___________________')
squares = [1, 4, 9, 16, 25]
print (squares)
print (squares[0])
print (squares[-1])
print (squares[-3:])
print (squares[:])
print (squares + [36, 49, 64, 81, 100])

print('___________________')
cubes = [1, 8, 27, 65, 125]
cubes[3] = 64
print (cubes)  

#append
cubes.append(216)
cubes.append(7 ** 3)
print (cubes) 

#Assignment to slices 
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print (letters)
letters[2:5] = ['C', 'D', 'E']
print (letters)
letters[2:5] = []
print(letters)
letters[:] = []
print(letters)

print(' ')
letters = ['a', 'b', 'c', 'd']
print (len(letters))

a = ['a', 'b', 'c']
n = [1, 2, 3]
x = [a, n]
print (x)
print (x[0])
print (x[0][1])

print (' ')

a, b = 0, 1
while a < 10:
    print(a)
    a, b = b, a+b

print (' ')
i = 256*256
print('The value of i is', i)

print (' ')
a, b = 0, 1
while a < 1000:
    print(a, end=',')
    a, b = b, a+b
