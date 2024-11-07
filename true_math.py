from math import inf # импорт значения бесконечности из встр. библиотеки
def divide(first, second): # зададим ф-ию прин-ую 2 парам.
    if second == 0:        # если парам. равен 0
        return inf         # то, вернется зн. бесконечности
    return first / second  # если second не равен 0, то выполнится деление