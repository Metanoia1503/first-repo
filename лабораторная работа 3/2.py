# TODO Напишите функцию find_common_participants
def find_common_participants(participants_first_group, participants_second_group, a = ","):
    first = participants_first_group.split(a)
    second = participants_second_group.split(a)
    common_participants = list(set(first) & set(second))
    return sorted(common_participants)

# TODO Провеьте работу функции с разделителем отличным от запятой
