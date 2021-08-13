list = [21, -4, 234, 102, 493, 129, 12, -4, 14, 9, 12, 95, 65, 12, -21, 0, 123, 135, 7]
for j in range(0, len(list)):
    previous = list[0]
    position = 0
    for i in list:
        if i >= previous:
            previous = i
        else:
            number_to_move = list.pop(position)
            list.insert(position-1, number_to_move)
        position += 1
print(list)
