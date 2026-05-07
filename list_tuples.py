marks = [78.44, 67.54, 43.22, 78.89, 98.4]
print(marks)
print(type(marks))

print(marks[0])

print(marks[4])
# ......................................................
student= ["niharika", 21, 99.5, "gurugram"]
print(student)
print(student[0])
student[0]= "manjeet"
print(student)
# ..........................................................
marks = [78.44, 67.54, 43.22, 78.89, 98.4]
print (marks[:4])
print (marks[:2])
# ..................
marks.append(48)
print(marks)
# ..................
marks = [78, 67, 43, 78, 98]
print(marks[:4])
print(marks[:2])
# .........................
marks.sort()
print(marks)
# ...............
marks.sort(reverse=True)
print(marks)
# .....................
marks.reverse()
print(marks)
# .................
marks.insert(1,6)
print(marks)
# ......................
marks.remove(78)
print(marks)
# .......................
marks.pop(3)
print(marks)
# ................
tup =(2,4,5,6,88,99,3)
print(tup[2])
print(tup[5])
print(tup)
print(type(tup))
print(tup[1:5])
print(tup.count(5))
# ...................................
# practice question........................
movies = []

movies.append(input("Enter movie 1: "))
movies.append(input("Enter movie 2: "))
movies.append(input("Enter movie 3: "))

print(movies)
# practice question........................

list1 = [1,2,3,2,1]

copy_list1 = list1.copy()
copy_list1.reverse()

if(copy_list1 == list1):
    print("palindrome")
else:
    print("not palindrome")
        
 # practice question..........................
grade =  ("A","C","B","D","F","E")
print(grade.count("A"))

grade =  ["A","C","B","D","F","E"]
grade.sort()
print(grade)
