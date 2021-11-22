list_1 = [(), (), ('',), ('a', 'b'), {}, ('a', 'b', 'c'), ('d'), '', []]
list_2 = [i for i in list_1 if len(i)>0]
print(list_2)

