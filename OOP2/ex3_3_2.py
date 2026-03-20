def print_horizontal(n):
    for _ in range(n):
        print("+ - - - -", end=" ")
    print("+")

def print_vertical(n):
    for _ in range(n):
        print("|         ", end="")
    print("|")

def draw_grid(n):
    for _ in range(n):
        print_horizontal(n)
        for _ in range(4):
            print_vertical(n)
    print_horizontal(n)


draw_grid(4)
#hihiihihihi
#dd