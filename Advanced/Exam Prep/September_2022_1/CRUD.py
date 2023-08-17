SIZE = 6

matrix = [[x for x in input().split()] for x in range(SIZE)]


starting_positions = []


directions = {
    "up": (-1,0),
    "down": (1,0),
    "left": (0,-1),
    "right": (0,1),

}
