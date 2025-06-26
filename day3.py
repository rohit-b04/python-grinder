from functools import reduce
'''
employees = [("Aditya", 18, 33, 20), ("Deep", 18, 48, 16), ("Anisha", 19, 56, 42), ("Ganesh", 20, 36, 24), ("Pratiksha", 20, 52, 39)]
# name age task-assigned task-done

while True:
    print("1. List out all the employees")
    print("2. Who is younger")
    print("3. Top performer")
    print("4. Top tasks assigned")
    print("5. Max tasks done by ")
    choice = int(input("Enter your choice"))

    match choice:
        case 1:
            li = list(map(lambda x: x[0],employees ))
            print(li)
        case 2:
            younger = list(reduce(lambda x, y: x if x[1] < y[1] else y, employees))
            print(younger)
        case 3:
            topP = reduce(lambda x, y: x if x[2]/x[3]<y[2]/y[3] else y, employees)
            print(topP)
        case 4:
            topT = max(employees, key=lambda x:x[2])
            print(topT)
        case 5:
            maxTasks = max(employees, key=lambda x:x[3])
            print(maxTasks)
        case _:
            print("invalid input")
'''

matrix = [[1,2,3],[4,5,6],[7,8,9]]
transpose = [[row[i] for row in matrix] for i in range(len(matrix[0]))]
print(transpose)

squares = [x**2 for x in range(1,6)]
print(squares)

dict = {x:x**3 for x in range(1,6) if x%2==1}
print(dict)

s = "sanjivani"
remS = set(i for i in s)
print(remS)

#num = int(input("Enter a number: "))
try:
    result = int("abc")/0
    print(result)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)


try:
    result = "abc"/0
    print(result)
except ZeroDivisionError as e:
    print(e)
except ValueError as e:
    print(e)
except TypeError as e:
    print(e)

abc = 0

try:
    num = int("abc")
    result = abc/num
    print(result)
except TypeError as e:
    print(e)
except NameError as e:
    print(e)
except ValueError as e:
    print(e)
else:
    print("no error")



try:
    result = abc/1
    print(result)
except TypeError as e:
    print(e)
except NameError as e:
    print(e)
except ValueError as e:
    print(e)
else:
    print("no error")
finally:
    print("Executed irrespective of error or not")

l = [1, 2, 3, 4, 5]
try:
    print(l[6])
except Exception as e:
    print(e)
