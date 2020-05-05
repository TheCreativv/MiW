#zad 2 Format textu
#zad 2 a
class Data(object):
    def __repr__(self):
        return 'cass'
print('{0!r} {0!a}'.format(Data()))

#zad 2 b //padding
print('{:>10}'.format('test'))

#zad 3 c // Truncating
print('{:.5}'.format('Monty Pythons Flying Circus'))

#zad 3 d // numbers
print('{:f}'.format(3.141592653689793))

#zad 3 e // padding numbers
print('{:06.2f}'.format(3.141592653589793))
