marks = [5, 4 ,3,5,2,4,5,3,2,5,4,3,5,2,4]
counts = {}
c = 0
mark_ = 0
summ = 0
for mark in marks:
    if mark in counts:
        counts[mark] += 1
    else:
        counts[mark] = 1
print(counts)
for mark,i in counts.items():
    if i > c:
        c = i
        mark_ = mark
print(f'Частая оценка: {c}')
for s in counts.values():
    summ += s
print(f'Сумма: {summ}')