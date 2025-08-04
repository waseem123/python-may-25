from searchsort import search as sc
from searchsort import sort as st

mylist = ['Solapur','Mumbai','Pune','Bengaluru','Delhi']

print(sc.ispresent(mylist,'Pune'))
print(sc.ispresent(mylist,'XYZ'))

print(st.sorting(mylist))
print(st.sorting(mylist,False))