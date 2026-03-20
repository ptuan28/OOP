def print_horizontal():
    print("+ - - - - + - - - - +")

def print_vertical():
    print("|         |         |")

def draw_grid():
    print_horizontal()
    for _ in range(4):
        print_vertical()
    print_horizontal()
    for _ in range(4):
        print_vertical()
    print_horizontal()


draw_grid()