from nltk.stem import SnowballStemmer
import re

# Task 1
text = 'Ёлка Это обычная тестовая строка, которая содержит знаки припинания такие как: , .:?. ' + \
       'Кроме того данный пример содержит информацию о номерах телефонов +7-901-000-00-00, 8(918)3213412 и ' + \
       'адресах г. Санкт-Петербург, ул. Советская, д. 1294124, кв. 1., город Тест, улица Тестовая, дом 1, квартира 2,' + \
       'и эмотиконах :(, :=), :), Xd,XD, <3, =3,:3, 8-), B-) '


def find_pattern(str_example):
    pattern = r"((город|гор|г)\.?\s?[а-яА-Я\- ]+,\s?(ул|улица)\.?\s?[а-яА-Яa\- ]+,\s?(д|дом)\.?\s?\d+,\s?(кв|квартира)\.?\s?\d+" + \
              r"|((\:|\-|\:=|;)(\)|\())|((<|=|\:)3)|((8|B)\-\))" + \
              r"|[а-яА-ЯёЁa-zA-Z]+|[.,!?;\:])" + \
              r"|(\+?\d)(\(\d{3}\)|\-\d{3}\-|\d{3})\d{3}(\d{4}|(\-\d{2}){2})|(\d+)"

    res = re.finditer(pattern, str_example)
    return [i.group() for i in res]


data = find_pattern(text)
print('============')
print('Task 1')
print(data)
print('============\n\n')

# Task 2
snowball = SnowballStemmer(language="russian")
text_2 = "Хорошие программисты пишут хороший код"

print('============')
print('Task 2')
print(text_2)
print([snowball.stem(val) for val in text_2.split()])
print('============\n\n')

# Task 3
import pandas as pd
import pymorphy2

morph = pymorphy2.MorphAnalyzer(lang='ru')
dataframe = pd.read_csv("Task1/word2lemma.csv", sep='\t', header=0)

worlds = dataframe['word']
nf = dataframe['nf']

arr = [(worlds[i], morph.parse(worlds[i])[0].normal_form, nf[i]) for i in range(len(dataframe['word'])) if
       morph.parse(worlds[i])[0].normal_form.lower() != nf[i].lower()]
with open(r'Task1\data.txt', 'w', encoding='utf-8') as f:
    for el in arr:
        f.write(el[0] + "\t" + el[1] + "\t" + el[2] + '\n')

# morph = pymorphy2.MorphAnalyzer(lang='ru')
print('============')
print('Task 3')
print('3хместная' + ' - ' + morph.parse('3хместная')[0].normal_form + ' - ' + '3хместный')  # 3хместный ПРИЛОГАТЕЛЬНОЕ
print('созданья' + ' - ' + morph.parse('созданья')[0].normal_form + ' - ' + 'создание')  # создание СУЩЕСТВИТЕЛЬНОЕ
print('созерцал' + ' - ' + morph.parse('созерцал')[0].normal_form + ' - ' + 'созерцать')  # созерцать ГЛАГОЛ

print('========Омонимы=======')
print('сокогоны' + ' - ' + morph.parse('сокогоны')[0].normal_form + ' - ' + 'сокогонный')  # сокогоны ПРИЛАГАТЕЛЬНОЕ
print('соколов' + ' - ' + morph.parse('соколов')[0].normal_form + ' - ' + 'сокол')  # соколов существительное
print('сокращающий' + ' - ' + morph.parse('сокращающий')[
    0].normal_form + ' - ' + 'сокращающий')  # сокращающий ПРИЛОГАТЕЛЬНОЕ

print('печь' + ' - ' + morph.parse('печь')[0].normal_form + ' - ' + 'печь')  # печь
print('мука' + ' - ' + morph.parse('мука')[0].normal_form + ' - ' + 'мука')  # мука
print('село' + ' - ' + morph.parse('село')[0].normal_form + ' - ' + 'село')  # мука
print('============\n\n')

# Task_4
import csv

with open('File/Kuryshev.tsv', 'wt', encoding='utf-8') as out_file:
    tsv_writer = csv.writer(out_file, delimiter='\t')
    for el in data:
        tsv_writer.writerow([el, snowball.stem(el), morph.parse(el)[0].normal_form])
