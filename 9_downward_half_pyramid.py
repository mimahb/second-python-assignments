def half_pyramid(rows):

    for i in range(rows, 0, -1):
        for _ in range(0, i):
            print('*', end=' ')
        print('')

half_pyramid(5)