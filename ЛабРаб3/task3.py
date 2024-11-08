import string
import re

# TODO  Напишите функцию count_letters
def count_letters(str_):
    freq = {}
    str1 = str_.lower().strip(string.punctuation)
    words = str1.split()
    clear = list()
    for word1 in words:
        clear.append(word1.strip(string.punctuation).replace('\n', ''))
    for word2 in words:
        clear.append(word2.strip(string.punctuation).replace(' ', ''))
    str1 = list(''.join(clear))
    for st in str1:
        if st not in freq.keys():
            freq[st] = 1
        else:
            freq[st] += 1
    return freq

# TODO Напишите функцию calculate_frequency
def calculate_frequency(freq, str_):
    str1 = str_.lower().strip(string.punctuation)
    words = str1.split()
    clear = list()
    for word1 in words:
        clear.append(word1.strip(string.punctuation).replace('\n', ''))
    for word2 in words:
        clear.append(word2.strip(string.punctuation).replace(' ', ''))
    str1 = list(''.join(clear))
    count = len(str1)
    freqe = {}
    for key, value in freq.items():
        freqe[key] = int(freq[key]) / count
    return freqe

main_str = """У лукоморья дуб зелёный;
Златая цепь на дубе том:
И днём и ночью кот учёный
Всё ходит по цепи кругом;
Идёт направо - песнь заводит,
Налево - сказку говорит.
Там чудеса: там леший бродит,
Русалка на ветвях сидит;
Там на неведомых дорожках
Следы невиданных зверей;
Избушка там на курьих ножках
Стоит без окон, без дверей;
Там лес и дол видений полны;
Там о заре прихлынут волны
На брег песчаный и пустой,
И тридцать витязей прекрасных
Чредой из вод выходят ясных,
И с ними дядька их морской;
Там королевич мимоходом
Пленяет грозного царя;
Там в облаках перед народом
Через леса, через моря
Колдун несёт богатыря;
В темнице там царевна тужит,
А бурый волк ей верно служит;
Там ступа с Бабою Ягой
Идёт, бредёт сама собой,
Там царь Кащей над златом чахнет;
Там русский дух... там Русью пахнет!
И там я был, и мёд я пил;
У моря видел дуб зелёный;
Под ним сидел, и кот учёный
Свои мне сказки говорил."""

# TODO Распечатайте в столбик букву и её частоту в тексте

fre = count_letters(main_str)
alli = calculate_frequency(fre, main_str)

for key, value in alli.items():
    print(f'{key}: {value:.2f}')