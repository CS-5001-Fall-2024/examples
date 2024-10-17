def print_row(current: int, max: int):
    if current == max:
        print(current)
        return
    print(current, end='')
    print_row(current + 1, max)


def print_triangle_helper(current: int, max: int):
    if current == max:
        print_row(0, max)
        return
    print_row(0, current)
    print_triangle_helper(current + 1, max)    
    print_row(0, current)


def print_triangle(max: int):
    if max <= 0:
        return
    print_triangle_helper(0, max - 1)

print_triangle(0)