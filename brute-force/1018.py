chess_board_B = [
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
]
chess_board_W = [
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
    'WBWBWBWB',
    'BWBWBWBW',
]
N, M = map(int, input().split())
board = []
for i in range(N):
    board.append(input())

def loop_board(arr):
    for i in range(len(arr)-8):
        line = list(arr[i])
        for j in range(len(line)-8):
            line