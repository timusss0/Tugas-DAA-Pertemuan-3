#Union
set_A = {1,2,3,4}
set_B = {3,4,5,6}
print(set_A | set_B)

#Intersection
print(set_A & set_B)
print(set_A.intersection(set_B))

#Difference
#A - B
print(set_A - set_B)
print(set_A.difference(set_B))

#B - A
print(set_B - set_A)
print(set_B.difference(set_A))

#Symmetric Difference 
print(set_A ^ set_B)
print(set_A.symmetric_difference(set_B))

#Latihan
red = {'dandelions', 'Leaves', 'fire hydrant',}
yelow = {'rose', 'blood', 'leaves', 'fire hydrant'}
print(red & yelow)
print(red | yelow)