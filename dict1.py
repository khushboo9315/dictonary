'''"Write a Python script to add a key to a dictionary.'''

# d={}
# d["year"]=2006
# print(d)

'''Write a Python script to concatenate the following dictionaries to create a new one.
Sample Dictionary :
dic1={1:10, 2:20}
dic2={3:30, 4:40}
dic3={5:50,6:60}
Expected Result : {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}'''


# dict={}
# dic1={1:10, 2:20}
# dic2={3:30, 4:40}
# dic3={5:50,6:60}
# dic1.update(dic2)
# print(dic1)
# dic1.update(dic3)
# print(dic1)
# dict.update(dic1)
# print(dict)

'''Write a Python script to check whether a given key already exists in a dictionary.'''

# n=input()
# d={"brand":"ford","model":"mustana","year":1965}
# for i in d:
#     if i==n:
#         print("YEs")
#         break
# else:
#     print("NO")

'''Write a Python program to iterate over dictionaries using for loops.'''

# d={"brand":"ford","model":"mustana","year":1965}
# for i in d.items():
#     print(i)

'''Write a Python script to generate and print a dictionary that contains a number
 (between 1 and n) in the form (x, x*x).
Sample Dictionary ( n = 5) :
Expected Output : {1: 1, 2: 4, 3: 9, 4: 16, 5: 25}'''

# d={}
# n=int(input())
# for i in range(1,n+1):
#     d.setdefault(i,i*i)
# print(d) 




# for i in range(1,6):
#     d[i]=i*i
# print(d)


'''Write a Python program to remove a key from a dictionary.'''

# d={"brand":"ford","model":"mustana","year":1965}
# d.pop("brand")
# print(d)

'''Write a Python program to map two lists into a dictionary.'''

# a=["name","age","dob","addres"]
# b=["khushboo",21,"4/april","delhi"]
# d={}
# for i in range(len(a)):
#     d[a[i]]=b[i]
# print(d)
    
'''Write a Python program to get the maximum and minimum value in a dictionary.'''

# d={1:4,3:6,7:9,2:5,0:7,5:10,9:1}
# l1=list(d.keys())
# l2=list(d.values())
# max=l1[l2.index(max(l2))]
# min=l1[l2.index(min(l2))]
# print(max)
# print(min)
# print(len(d))

'''Write a Python program to check if a dictionary is empty or not.'''

# d={1:4,3:6,7:9,2:5,0:7,5:10,9:1}
# if len(d)==0:
#     print("yes its empty")
# else:
#     print("No")

'''Write a Python program to combine two dictionary adding values for common keys.
d1 = {'a': 100, 'b': 200, 'c':300}
d2 = {'a': 300, 'b': 200, 'd':400}
Sample output: Counter({'a': 400, 'b': 400, 'd': 400, 'c': 300})'''

# d1 = {'a': 100, 'b': 200, 'c':300}
# d2 = {'a': 300, 'b': 200, 'd':400}
# for i in d1:
#     if i in d2:
#         d2[i]=d2[i]+d1[i]
#     else:
#         d2[i]=d1[i]
# print(d2)

'''Write a Python program to create and display all combinations of letters, 
selecting each letter from a different key in a dictionary.
Sample data : {'1':['a','b'], '2':['c','d']}
Expected Output:
ac
ad
bc
bd'''

# d={'1':['a','b'], '2':['c','d']}
# l1=list(d.values())
# for  i in l1[0]:
#     for j in l1[1]:
#         print(i+j)

'''Write a Python program to combine values in a list of dictionaries.
Sample data: [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, 
{'item': 'item1', 'amount': 750}]
Expected Output: Counter({'item1': 1150, 'item2': 300})'''

# x = [{'item': 'item1', 'amount': 400}, {'item': 'item2', 'amount': 300}, {'item': 'item1', 'amount': 750}]
# result={}
# for d in x:
#     result[d['item']] = result.get(d['item'], 0) + d['amount']
#     print(result)

'''2nd mwthod'''

# data = [
# {'item': 'item1', 'amount': 400},
# {'item': 'item2', 'amount': 300},
# {'item': 'item1', 'amount': 750}
# ]
# my_dict = {}
# for i in data:
#     if i["item"] not in my_dict:
#         my_dict[i["item"]] = i["amount"]
#     else:
#         my_dict[i["item"]] += i["amount"]
# print(my_dict)



'''Write a Python program to create a dictionary that stores the count of the occurrences of
 a letter from a string'''


# l=["a","d","r","e","s","y","u","e","w","q","h","g","f","d","s","e","r","t"]
# l="khushboosharma"
# d={}
# for ch in l:
#     d.setdefault(ch,0)
#     d[ch]+=1
# print(d)


'''Write a Python program to remove spaces from dictionary keys.'''

# d={"p 3":45,"u 8":67}
# dic={}
# for k,v in d.items():
#     k=k.replace(" ","")
#     dic[k]=v
# print(dic)

'''Write a Python program to get the key, value and item in a dictionary.'''

# d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}
# for k,v in d.items():
#     print(k,v)
# print(d.items())

'''Write a Python program to drop empty values from a given Dictionary. (empty string is not an emply value)'''

# d={1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: None}
# print(d)
# d={x:v for x,v in d.items()if v is not None}
# print(d)

'''Write a Python program to filter a dictionary based on values.
Original Dictionary:
{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
Marks greater than 170:
{'Cierra Vega': 175, 'Alden Cantrell': 180, 'Pierre Cox': 190}'''

# d={'Cierra Vega': 175, 'Alden Cantrell': 180, 'Kierra Gentry': 165, 'Pierre Cox': 190}
# print(d)
# d={x:v for x,v in d.items()if v>170}
# print(d)

'''Write a Python program to filter the students based on their height and weight,
 which are stored in a dictionary.
Original Dictionary:
{'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
Height > 6ft and Weight> 70kg:
{'Cierra Vega': (6.2, 70)}'''

# d={'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# print(d)
# d={x:v for x,v in d.items()if v[0]>=6 and v[1]>=70 }
# print(d)

'''Write a Python program to create a dictionary grouping a sequence of key-value 
pairs into a dictionary of lists.
Original list:
[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
Grouping a sequence of key-value pairs into a dictionary of lists:
{'yellow': [1, 3], 'blue': [2, 4], 'red': [1]}'''

# l=[('yellow', 1), ('blue', 2), ('yellow', 3), ('blue', 4), ('red', 1)]
# d={}
# for k,v in l:
#     d.setdefault(k,[]).append(v)
# print(d)

'''Write a Python program to sort a given dictionary by key'''

# d={"name":"khushi","study":"ba hons","age":21,"location":"delhi","year":2001}
# d1={}
# for k in sorted(d):
#     d1+=(k,d[k])
# print(d1)
'''Write a Python script to sort (ascending and descending) a dictionary by value '''

# student={"math":78,"english":56,"science":67,"bio":90,"hindi":89,"sanskrit":50}
# for v in sorted(student.values()):
#     print(v)
# d={"math":78,"english":56,"science":67,"bio":90,"hindi":89,"sanskrit":50}
# a={}
# de={}
# k=list(d.keys())
# v=list(d.values())
# s=v.copy()
# s.sort()
# r=s[::-1]
# for i in range(len(v)):
#     ind=v.index(s[i])
#     a[k[ind]]=s[i]
# print(a)

# for j in range(len(r)):
#     ind=v.index(r[j])
#     de[k[ind]]=r[j]
# print(de)


'''Write a Python program to split a given dictionary of lists into a list of dictionaries.
Original dictionary of lists:
{'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
Split said dictionary of lists into list of dictionaries:
[{'Science': 88, 'Language': 77}, {'Science': 89, 'Language': 78}, 
{'Science': 62, 'Language': 84}, {'Science': 95, 'Language': 80}]'''

# d={'Science': [88, 89, 62, 95], 'Language': [77, 78, 84, 80]}
# l=[]
# val=(list(d.values()))
# k=list(d.keys())
# for i in range(len(val[0])):
#     d1={}
#     for j in range(len(k)):
#         d1[k[j]]=val[j][i]
#     l.append(d1)
# print(l)


'''Write a Python program to extract a list of values from a given list of dictionaries.
Original Dictionary:
[{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
Extract a list of values from said list of dictionaries where subject = Science
[92, 94, 88]
Original Dictionary:
[{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
Extract a list of values from said list of dictionaries where subject = Math
[90, 89, 92]'''

# l=[{'Math': 90, 'Science': 92}, {'Math': 89, 'Science': 94}, {'Math': 92, 'Science': 88}]
# n=input()
# lst=[]
# for i in (l):
#     for k,v in i.items():
#         if k==n:
#             lst.append(v)
# print(n,"=",lst)


'''Write a Python program to filter even numbers from a given dictionary values.
Original Dictionary:
{'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
Filter even numbers from said dictionary values:
{'V': [4, 6, 10], 'VI': [4, 12], 'VII': [8]}'''

# d={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# k=list(d.keys())
# v=list(d.values())
# d1={}
# for i in range(len(v)):
#     # d1={}
#     l1=[]
#     for j in range(len(v[i])):
#         if v[i][j]%2==0:
#             l1.append(v[i][j])
#             # d1[k[i]]=v[i][j]
#     d1[k[i]]=l1
# print(d1)
'''Original Dictionary:
{'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
Filter even numbers from said dictionary values:
{'V': [], 'VI': [], 'VII': [2]}'''
# d={'V': [1, 3, 5], 'VI': [1, 5], 'VII': [2, 7, 9]}
# d={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# k=list(d.keys())
# v=list(d.values())
# d1={}
# for i in range(len(v)):
#     # d1={}
#     l1=[]
#     for j in range(len(v[i])):
#         if v[i][j]%2==0:
#             l1.append(v[i][j])
#             # d1[k[i]]=v[i][j]
#     d1[k[i]]=l1
# print(d1)


'''Write a Python program to get all combinations of key-value pairs in a given dictionary.
Original Dictionary:
{'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
Combinations of key-value pairs of the said dictionary:
[{'V': [1, 4, 6, 10], 'VI': [1, 4, 12]}, {'V': [1, 4, 6, 10], 'VII': [1, 3, 8]}, 
{'VI': [1, 4, 12], 'VII': [1, 3, 8]}]'''

# d={'V': [1, 4, 6, 10], 'VI': [1, 4, 12], 'VII': [1, 3, 8]}
# l=[]
# k=list(d.keys())
# v=list(d.values())
# for i in range(k):
#     d1={}
#     for j in range(i+1):
#         d1[]

# Original Dictionary:
# {'V': [1, 3, 5], 'VI': [1, 5]}
# Combinations of key-value pairs of the said dictionary:
# [{'V': [1, 3, 5], 'VI': [1, 5]}]
#  Write a Python program to find the key of the maximum value in a dictionary.
# Sample Output:
# Original dictionary elements:
# {'Theodore': 19, 'Roxanne': 22, 'Mathew': 21, 'Betty': 20}
# Finds the key of the maximum and minimum value of the said dictionary:
# ('Roxanne', 'Theodore')


print(5+7)