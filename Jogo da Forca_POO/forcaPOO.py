from random import randint

def printForca(chances):

    desenhos = ("""__________________
|                  |
|                  0
|                 /|\\
|                 / \\
|
|
|
|
""","""__________________
|                  |
|                  0
|                 /|\\
|                 /
|
|
|
|
""","""__________________
|                  |
|                  0
|                 /|\\
|
|
|
|
|
""","""__________________
|                  |
|                  0
|                 /|
|
|
|
|
|
""","""__________________
|                  |
|                  0
|                  |
|
|
|
|
|
""","""__________________
|                  |
|                  0
|
|
|
|
|
|
""","""__________________
|                  |
|
|
|
|
|
|
|
""")
    print(desenhos[chances])

