# A. Forked!
def solve():
    import sys
    input = sys.stdin.readline

    t = int(input().strip())
    for _ in range(t):
        a, b = map(int, input().split())
        xK, yK = map(int, input().split())
        xQ, yQ = map(int, input().split())

        # Define the knight moves.
        moves = {(a, b), (a, -b), (-a, b), (-a, -b),
                 (b, a), (b, -a), (-b, a), (-b, -a)}

        # Compute possible knight positions that attack the king.
        king_positions = {(xK - dx, yK - dy) for (dx, dy) in moves}
        # Compute possible knight positions that attack the queen.
        queen_positions = {(xQ - dx, yQ - dy) for (dx, dy) in moves}

        # The knight must be placed in the intersection.
        result = king_positions & queen_positions

        # Output the number of positions.
        print(len(result))

if __name__ == '__main__':
    solve()
