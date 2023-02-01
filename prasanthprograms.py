#1
# lst = [[1,2],[2,4,5],2,4,[2,4]]
# lis = []
# for i in lst:
#     if type(i) is list:
#         for j in i:
#             lis.append(j)
#     else:
#         lis.append(i)
# print(lis)


#2
# import re
# strin = "today is jan 13 2023 and tomorrow is 14 jan 2023"
# templat = '\d\d jan \d{4}|jan \d\d \d{4}'
# res = re.findall(templat,strin)
# print(res)


#3
# def charfreq(strin):
#     # count = 0
#     for i in strin:
#         a=strin.count(i)
#         print(i ,"==", a)
# charfreq("listisveryhelpfulinmanyconditions")


#3 original

# def charfreq(stri):
#     dic = {}
#     for n in stri:
#         keys = dic.keys()
#         if n in keys:
#             dic[n]+=1
#         else:
#             dic[n]=1
#     return dic
# print(charfreq("anything which is important"))










#4
# a = 5
# for i in range(a):
#     print(' '*(a-i-1)+("* ")*(i+1))



