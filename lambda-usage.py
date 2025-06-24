from functools import reduce
from collections import Counter
from re import match


def fun():
    a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
c = [x for x in b]
#print(type(c))
#print(sum(c))

b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
c = [x*x for x in b]
#print(sum(c))
#print(c)

k = reduce(lambda x,y: x+y, range(11))
#print(k)

l = reduce(lambda x,y: x if x>y else y, range(11))
#print(l)

l = reduce(lambda x,y:x if(x<y) else y, range(11))
#print(l)

str = "Implementing word count count"
#print(len(str.split()))

#print(f'word count: {str} is {Counter(str.split())}')
#Counter(str.split())


l1 = [1, 2, 3, 4]
l2 = [2, 7, 9, 11]
res = list(map(lambda x,y: x + y,l1, l2 ))
#print(res)


data = [(1, 'one'), (3, 'three'), (0, 'zero')]
people = [
    {'name': 'rohit', 'age': 21},
    {'name': 'amit', 'age': 23},
    {'name': 'tanyy', 'age': 21}
]

print(reduce(lambda x, y: x + y, l1))

mylist = ["tanmay", "rohit", "atharv", ""]
result = all(map(lambda s: s!= "", mylist))
#print(result)

'''
students = [("ashwini", 20, 98, "kop"), ("ram", 21, 97, "shirdi"), ("Aditya", 18, 91, "kop"), ("rohit", 19, 88, "pune")]
obj: 1. collect only names
2. collect names if marks are more than 19
3. who is topper
4. who is younger
5. how many belongs to kop
6. list out the names who do not belong to kop
'''

from itertools import groupby
data = [5, 1, 1, 4, 4, 3, 4, 2, 1, 5, 3, 6 ]
data = sorted(data)
groups = [list(group) for key, group in groupby(data, key = lambda  x:x)]
print(groups)

result = [x ** 3 for x in range(11)]
result1 = list(map(lambda x: x ** 3, range(11)))
# result == result1
print(result1)


'''
students = [("ashwini", 20, 98, "kop"), ("ram", 21, 97, "shirdi"), ("Aditya", 18, 91, "kop"), ("rohit", 19, 88, "pune")]
while True:
    print("1. Collect only names")
    print("2. Names with marks more than 90")
    print("3. Who is topper")
    print("4. who is younger")
    print("5. How many belong to kop")
    print("6. List out the names not in kop")
    print("7. Exit")
    ip = int(input("Enter the choice"))
    match ip:
        case 1:
            print(list(map(lambda x: x[0], students)))
        case 2:
            temp = list(filter(lambda x:x[2] > 90, students))
            print(list(map(lambda x: x[0] , temp)))
        case 3:
            print(list(reduce(lambda x, y: x if x[2] > y[2] else y, students)))
        case 4:
            print(list(reduce(lambda x, y: x if x[1] < y[1] else y, students)))
        case 5:
            kop_res = list(filter(lambda x: x[3]=='kop', students))
            print(list(map(lambda x: x[0], kop_res)))
        case 6:
            not_in_kop = list(filter(lambda x: x[3] != 'kop', students))
            print(list(map(lambda x: x[0], not_in_kop)))
        case 7:
            exit(0)
        case _:
            print("no match")
'''