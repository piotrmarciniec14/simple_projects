a = input('podaj liczbe binarna')
list_of_bytes = []
dec_number = 0
position = 0
for byte in str(a):
    list_of_bytes.append(byte)
list_of_bytes.reverse()
for i in list_of_bytes:
    dec_number += int(i) * (2 ** position)
    position += 1
print(f'liczba {a} zapisana dziesietnie to {dec_number}')