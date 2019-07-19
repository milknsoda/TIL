student = {
    'a1': {
        '순번': '01',
        '이름': '김성훈'
    },
    'a2': {
        '순번': '02',
        '이름': '김은정'
    }
}
# 1
# with open('a.csv', 'w', encoding='utf-8') as f:
#     f.write('number, name\n')
#     for number, name in student.items():
#         f.write(f'{number}, {name}\n')

# 2
import csv
# with open('b.csv', 'w', encoding='utf-8') as f:
#     csv_writer = csv.writer(f)
#     for item in student.items():
#         csv_writer.writerow(item)

student2 = [
    {
        '순번': '01',
        '이름': '김성훈'
    },
    {
        '순번': '02',
        '이름': '김은정'
    }
]
# 3-1
with open('b.csv', 'w', encoding='utf-8') as f:
    fieldnames = ['순번', '이름'] # 여기만 변경하면서 사용?
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    for item in student.values(): # 딕셔너리 만든 것 반복
        csv_writer.writerow(item)
# 3-2
with open('c.csv', 'w', encoding='utf-8') as f:
    fieldnames = ['순번', '이름'] # 여기만 변경하면서 사용?
    csv_writer = csv.DictWriter(f, fieldnames=fieldnames)
    csv_writer.writeheader()
    for item in student2: # 리스트 안에 딕셔너리
        csv_writer.writerow(item)