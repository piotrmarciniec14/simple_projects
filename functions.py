def bubble_sorting(list):
    for j in range(0, len(list)):
        previous = list[0]
        position = 0
        for i in list:
            if i >= previous:
                previous = i
            else:
                number_to_move = list.pop(position)
                list.insert(position - 1, number_to_move)
            position += 1
    return list


def binary_to_decimal(a):
    list_of_bytes = []
    dec_number = 0
    position = 0
    for byte in str(a):
        list_of_bytes.append(byte)
    list_of_bytes.reverse()
    for i in list_of_bytes:
        dec_number += int(i) * (2 ** position)
        position += 1
    return dec_number


def odd_or_even(a):
    if int(a)%2 == 0:
        is_even = True
    else:
        is_even = False
    return is_even    
        

