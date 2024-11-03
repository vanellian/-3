# TODO Напишите функцию find_common_participants
def find_common_participants(str1, str2, raz = ','):
    set_ = set(str1.split(raz))
    set2 = set_.intersection(str2.split(raz))
    str3 = list(set2)
    return str3

participants_first_group = "Иванов|Петров|Сидоров"
participants_second_group = "Петров|Сидоров|Смирнов"

print(find_common_participants(participants_first_group, participants_second_group, '|'))

# TODO Провеьте работу функции с разделителем отличным от запятой
