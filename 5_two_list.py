list1 = [10,20,25,30,35]
list2 = [40,45,60,75,90]
list3 = [n for n in list1 if n%2] + [n for n in list2 if not n%2]
print("result list: ",list3)
