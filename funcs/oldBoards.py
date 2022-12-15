# This file is like a database of scenarios, its pretty boring



boards = [

    # 1 https://www.youtube.com/watch?v=aNIWqiZt_Rw&list=PLu0rC09yug3YbL_eR6vCK7NAH4bj2VEfZ&index=3&ab_channel=GaryDeVries

    [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, -1, 1, 0, 0],
        [0, 0, 0, 1, -1, 0, 0],
        [0, 0, 0, -1, 1, 0, 0],
        [0, 0, 1, 1, -1, 0, -1]
    ],

    # 2 https://www.youtube.com/watch?v=RoQV1DNIfe0&list=PLu0rC09yug3YbL_eR6vCK7NAH4bj2VEfZ&index=2&ab_channel=GaryDeVries

    [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, -1, 0, 0, 0],
        [0, 0, 1, 1, 0, 0, 0],
        [0, 0, -1, 1, -1, -1, 0],
        [-1, 0, -1, 1, 1, 1, -1]
    ],

    # 3 https://www.youtube.com/watch?v=_ZKl-s5CoI4&list=PLu0rC09yug3YbL_eR6vCK7NAH4bj2VEfZ&index=7&ab_channel=GaryDeVries
    [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 1, 1, -1, 0, 0],
        [0, 0, 1, 1, -1, -1, -1]
    ],

    # 4 https://www.youtube.com/watch?v=8hhxajhHef0&list=PLu0rC09yug3YbL_eR6vCK7NAH4bj2VEfZ&index=8&ab_channel=GaryDeVries
    [
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 1, 1, 0, 0],
        [-1, -1, 0, 1, 1, -1, -1]
    ],

    # 5 https://www.youtube.com/watch?v=m0GIEpcevRc&list=PLu0rC09yug3YbL_eR6vCK7NAH4bj2VEfZ&index=8&ab_channel=GaryDeVries
    [
        [0, 0, 0, -1, -1, 0, 0],
        [0, -1, 0, 1, -1, 0, 0],
        [0, -1, 0, 1, 1, 0, 0],
        [0, 1, 0, 1, -1, 0, 0],
        [0, 1, -1, -1, 1, 1, 0],
        [-1, -1, 1, -1, 1, 1, 0]
    ]
]

boardSols = [[1], [4, 1, 5, 1], [3, 4, 2, 5], [3, 4, 6, 5], [2, 5, 1, 5], [], [], [], []]
boardCompleteMsgs = [
    #board1
    "Congratulations! The AI cannot defend both 4's you can make after you play this splitting move.",

    #board2
    "Nice! By defending the first 4, the opponent gives you a second four to make! Youre sick bruh",

    #board3
    "Good sequence! You created so many threats, even the (almost) unstoppable AI couldn't find a way to beat you",

    #board4
    "Good job! You forced the enemy to keep blocking you, which is very POG indeed",

    #board5
    "Nice, you blocked all open columns so AI HAS to play a move which lets you win."
]
boardHintMsgs = [

    #board1
    ["Hint: Create 2 4's"],

    #board2
    ["Hint: Block 4",
     "Hint: Build up column",
     "Hint: Block 4",
     "Hint: Keep Building!"],

    #board3
    ["Hint: Create a threat",
     "Hint: Diagonal threat",
     "Hint: Third threat!",
     "Hint: Make the double 4 threat!"],

    #board4
    ["Hint: First threat",
     "Hint: Second threat",
     "Hint: Force red to block",
     "Hint: Make the final doubler!"] ,

    ["Hint: Threat on Diagonal",
     "Hint: Vertical Threat",
     "Hint: Filling column",
     "Hint: Fill another column"]

]
# board =
#     [
#         [0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 0, 0, 0, 0, 0],
#         [0, 0, 1, -1, 0, 0, 0],
#         [0, 0, 1, 1, 0, 0, 0],
#         [0, 0, -1, 1, -1, -1, 0],
#         [-1, 0, -1, 1, 1, 1, -1]
#     ]
