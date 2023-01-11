""" Lesson 01 """
# Задача 2

#some_list = []
#for _ in range(5):
#    x = int(input())
#    some_list.append(x)
#maxx = some_list
#print(max(some_list))

#for el in some_list:
#    if el > maxx:
#        maxx = el
#print(maxx)


""" Lesson 02 """
#HomeWork 6

#day = int(input())
#if 1 <= day <= 5:
#    print('рабочий')
#else:
#    print('выходной')

#HomeWork 7
# #
# for x in [0, 1]:
#     for y in [0, 1]:
#         for z in [0, 1]:
#             print(f'{x} {y} {z} -> {not(x or y or z) == (not x and not y and not z)}')

""" Lesson 03 """

#work20
# a = input().split()
# num = input()
# for i in a:
#     if num in i:
#         print('yes')
#         break
# else:
#     print('no')

#work21
# a = input().split()
# find_str = input()
# count = 0
# for i in range(len(a)):
#     if a[i] == find_str:
#         count += 1
#         if count == 2:
#             print(i)
#             break
# else:
#     print(-1)

""" Lesson 03 """

# with open('input.txt', 'r', encoding='utf-8') as file:
    # text = file.read()            # вариант 1
    # for sym in text:
    #     print(sym.strip())

    # while True:                     # вариант 2
    #     line = file.readline()
    #     if not line:
    #         break
    #     print(line.strip())

# with open('input_w.txt', 'w', encoding='utf-8') as file:
#     for i in range(0, 100):
#         file.write(str(i) + '\n')

# Задача 27
with open('input.txt', 'r', encoding='utf-8') as file:
    line = file.read().split()
    maxx = int(line[0])
    minn = int(line[0])
    for el in line:
        if int(el) > maxx:
            maxx = int(el)
        elif int(el) > minn:
            minn = int(el)
    print(maxx, minn)
