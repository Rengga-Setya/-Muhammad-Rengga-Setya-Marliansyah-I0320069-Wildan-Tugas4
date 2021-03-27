#4 adalah 100 dalam biner dan 11 adalah 1011
a = 4
b = 11
c = 0
print('Biner = ',format(a,'08b'))

#4 | 11
c = a | b
print("a | b = ",c,', biner =',format(c,'08b'))

#4 >> 11
c = a >> b
print("a >> b = ",c,', biner =',format(c,'08b'))

#4 ^ 11
print("a ^ b = ",c,', biner =',format(c,'08b'))

#~4
c = ~a
print("~a = ",c,', biner =',format(c,'08b'))

#11 & 4
c = a & b
print("a & b = ",c,', biner =',format(c,'08b'))
