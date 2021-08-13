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
