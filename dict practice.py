
# d={"a":"cat","b":"dog","c":"fly"}
# print(d["a"])   #print value of "a" key
# d["b"]="elephant"   #it will change "b" ki value to elphant
# print(d) 
# d["b"]+="elephant" # it wll concatinate elephannt with key value of "b"
# print(d)
# s=d.keys() #it will return keys of dict. in a list
# s1=d.values()   #it will return values of dict. in a list
# print(s1)
# print(s)

# d1={"a":1,"b":2,"c":3}
# d2={"b":2,"c":3,"a":1}
# a=[1,2,3,4]
# b=[2,3,4,1]
# print(d1==d2)
# print(a==b)

# s=d1.items()
# print(s)
# print(type(s))
# for i in s:
#     print(i)


# d={}
# s=[2,3,4,5,2,1,7,4,3,2,2,6,7,8,0,7,5,5,4,3]
# for ch in s:
#     d.setdefault(ch,0)
#     d[ch]+=1
# print(d)
# x=dict(s)
# l1=list(d.values())
# l2=list(d.keys())
# print(l1.index(max(l1)))
# print(l2[l1.index(max(l1))])

# max=0
# key=0
# for k,v in d.items():
#     if v>max:
#         max=v
#         key=k
# print(max, key)


# a=int(input())
# for i in range(a):
#     n=int(input())
#     s=input()
#     al="abcdefghijklmnopqrstuvwxyz"
#     m=max(s)
#     print(al.index(m)+1)

# n=int(input())
# for i in range(n):
#     a,b,c=map(int,input().split())
#     if (a>b and a<c) or (a<b and a>c):
#         print(a)
#     elif (b>a and b<c) or (b<a and b>c):
#         print(b)
#     else:
#         print(c)

# a=int(input())
# for i in range(a):
#     n=int(input())
#     k =list(map(int,input().split()))
#     for j in range(n):
#         num=k[j]
#         k[j]=0
#         m=max(k)
#         print(num-m,end=" ")
#         k[j]=num

'''Write a Python program to sort a list alphabetically in a dictionary.'''

# num = {'n1': [2, 3, 1], 'n2': [5, 1, 2], 'n3': [3, 2, 4]}
# sorted_dict = {x: sorted(y) for x, y in num.items()}
# print(sorted_dict)


'''Write a Python program to remove spaces from dictionary keys.'''


# student_list = {'S  001': ['Math', 'Science'], 'S    002': ['Math', 'English']}
# print("Original dictionary: ",student_list)
# student_dict = {x.translate({32: None}): y for x, y in student_list.items()}
# print("New dictionary: ",student_dict)

'''Write a Python program to count number of items in a dictionary value that is a list.'''

# dict =  {'Alex': ['subj1', 'subj2', 'subj3'], 'David': ['subj1', 'subj2']}
# ctr = sum(map(len, dict.values()))
# print(ctr)

'''second method'''
# sum=0
# l=(list(dict.values()))
# for i in l:
#     sum+=len(i)
# print(sum)


'''Write a Python program to replace dictionary values with their average.
'''
# student_details= [
#   {'id' : 1, 'subject' : 'math', 'V' : 70, 'VI' : 82},
#   {'id' : 2, 'subject' : 'math', 'V' : 73, 'VI' : 74},
#   {'id' : 3, 'subject' : 'math', 'V' : 75, 'VI' : 86}
# ]

# for d in student_details:
#     n1 = d.pop('V')
#     n2 = d.pop('VI')
#     d['V+VI'] = (n1 + n2)/2
#     print(d) 


'''Write a Python program to match key values in two dictionaries.
'''

# x = {'key1': 1, 'key2': 3, 'key3': 2}
# y = {'key1': 1, 'key2': 2}
# for (key, value) in set(x.items()) & set(y.items()):
#     print('%s: %s is present in both x and y' % (key, value))

# 50. A Python Dictionary contains List as value. Write a Python program to clear the list values
#  in the said dictionary. Go to the editor
# Original Dictionary:
# d={'C1': [10, 20, 30], 'C2': [20, 30, 40], 'C3': [12, 34]}
# Clear the list values in the said dictionary:
# {'C1': [], 'C2': [], 'C3': []}

# for k in d:
#     # v=list(v)
#     d[k].clear()
# print(d)
    
'''51. A Python Dictionary contains List as value. Write a Python program to update the list values in the said dictionary. Go to the editor
Original Dictionary:
{'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
Update the list values of the said dictionary:
{'Math': [89, 90, 91], 'Physics': [90, 92, 87], 'Chemistry': [90, 87, 93]}'''

# d={'Math': [88, 89, 90], 'Physics': [92, 94, 89], 'Chemistry': [90, 87, 93]}
# d["Math"]=[x+1 for x in d["Math"]]
# d["Physics"]=[x-2 for x in d["Physics"]]
# print(d)

