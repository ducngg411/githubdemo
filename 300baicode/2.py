def print_triangle (n_lines, mode, symbol):
    i = 0  
    for i in range (0, n_lines + 1):
        if mode == 'normal':
            t = symbol * i 
            print(t)
            i += 1
        elif mode == 'reversed':
            t = symbol * i 
            print(f'{t:>8}')
            i += 1
        elif mode == 'bottomup':
            i = symbol * n_lines
            print(f'{i}')
            n_lines -= 1


print_triangle(4,'reversed','-')