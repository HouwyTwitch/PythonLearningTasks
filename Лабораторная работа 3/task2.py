# TODO Напишите функцию find_common_participants

def find_common_participants(s1, s2, delim=','):
    l1, l2 = s1.split(delim), s2.split(delim)
    return sorted(list(set(l1) & set(l2)))


participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

# TODO Провеьте работу функции с разделителем отличным от запятой

print(find_common_participants(participants_first_group, participants_second_group, '|'))