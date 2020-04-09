list1=[1,2,3,4]
list2=[9,8,7]
for item in list1:
  if item in list2:
    print("overlapping")
else:
    print("not overlapping")
