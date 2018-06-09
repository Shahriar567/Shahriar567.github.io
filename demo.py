
my_list = [10, 15, 3 ,7]

for x in my_list:
    for y in my_list:
        if x + y == 17:
            print('({x}, {y})'.format(x=x, y=y))
