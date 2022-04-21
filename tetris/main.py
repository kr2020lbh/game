import time
import random

def block_print(block):
    r,c = len(block),len(block[0])
    print(block,r,c)
    pivot = [0,0,0]
    for i in range(r):
        for j in range(c):
            if block[i][j]:
                if pivot[0] == 0:
                    pivot = 1,i,j
                print("■",end="")
            else:
                print("□",end="")
        print()
    print("pivot : {}".format(pivot))

def play(turn,gameBoard):
    print("NOW TURN : {}".format(turn))

    idx = random.randrange(7)
    cur_blocks = [blocks[idx]]

    if idx == 1: #하나
        pass
    elif idx == 0 or idx == 5 or idx == 6: #둘
        for _ in range(1):
            cur_blocks.append(list(zip(*cur_blocks[-1][::-1])))
    else: #넷
        for _ in range(3):
            cur_blocks.append(list(zip(*cur_blocks[-1][::-1])))

    for block in cur_blocks:
        block_print(block)


cnt = 0
gameBoard = [[0]*10 for _ in range(15)]
blocks = [
    [[1,1,1,1]],
    [[1,1],[1,1]],
    [[1,0,0],[1,1,1]],
    [[0,0,1],[1,1,1]],
    [[0,1,0],[1,1,1]],
    [[1,1,0],[0,1,1]],
    [[0,1,1],[1,1,0]]
]
while 1:
    play(cnt,gameBoard)
    cnt += 1
    time.sleep(1)
    