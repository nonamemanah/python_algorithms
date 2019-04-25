"""
Задание: 1. Пользователь вводит данные о количестве предприятий, их наименования и прибыль за 4 квартала
        (т.е. 4 отдельных числа) для каждого предприятия..
        Программа должна определить среднюю прибыль (за год для всех предприятий) и вывести наименования предприятий,
        чья прибыль выше среднего и отдельно вывести наименования предприятий, чья прибыль ниже среднего.
Автор: Чантурия Д. Г.
"""
import collections

Comapny = collections.namedtuple('Company', {'name', 'first_quarter', 'second_quarter', 'third_quarter',
                                             'fourth_quarter', 'summary', 'average'})

companies = []

companies_count = int(input('Введите количество предприятий: '))

for i in range(companies_count):
    name = input('Наименование предприятия: ')
    print('Введите придыль предприятия за четыре квартала.')
    first_quarter = float(input('Первый квартал: '))
    second_quarter = float(input('Второй квартал: '))
    third_quarter = float(input('Третий квартал: '))
    fourth_quarter = float(input('Четвертый квартал: '))
    summary = first_quarter + second_quarter + third_quarter + fourth_quarter
    average = summary / 4
    item = Comapny(name, first_quarter, second_quarter, third_quarter, fourth_quarter, summary, average)
    companies.append(item)
    print('-' * 10)

all_companies_sum = 0
for company in companies:
    all_companies_sum += company.summary

all_companies_average = all_companies_sum / companies_count
print(f'Среднюя прибыль за год для всех предприятий: {all_companies_average}')

more = []
less = []

for company in companies:
    if company.summary >= all_companies_average:
        more.append(company)
    else:
        less.append(company)

print('-' * 10)
print('Компании с прибылью выше среднего:')
for company in more:
    print(f'компания: {company.name}. Прибыль: {company.summary}')

print('Компании с прибылью меньше среднего:')
for company in less:
    print(f'компания: {company.name}. Прибыль: {company.summary}')
