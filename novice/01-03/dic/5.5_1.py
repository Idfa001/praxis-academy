tel = {'jack': 4098, 'sape': 4139}
tel['guido'] = 4127

print()
print (tel['jack'])

print()
print(tel)

print()
del tel['sape']
tel['irv'] = 4127
list(tel)
print(tel)

print()
print ('guido' in tel)
print ('jack' not in tel)


