from functools import reduce


my_list = [1, 2, 3, 4]


#traditional sum of ^2 approach - not using mapreduce
ssv_trad = sum(yin**2 for yin in my_list)

# mapreduce way sum of ^2 approach

squared_values = map(lambda yin: yin**2, my_list)
def  add_num(yeet_1, yeet_2):
    return yeet_1 + yeet_2


ssv_mapreduce = reduce(add_num, squared_values)



print(ssv_trad)
print(ssv_mapreduce)

