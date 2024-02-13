import random

# Matrix Randomizer
def randomizeMatrix(m, n): 
    matrix = []
    for _ in range(n):
        row = [random.choice(['7A', '55', 'E9', '1C', 'BD']) for _ in range(m)]
        matrix.append(row)
    return matrix

# Sequences and Rewards Randomizer
def randomizeSAR(numOfSequences):
    sequencesAndRewards = {}
    for _ in range(numOfSequences):
        sequenceLenght = random.randint(1, 5)
        sequence = ' '.join(random.choices(['7A', '55', 'E9', '1C', 'BD'], k=sequenceLenght))
        reward = random.randint(10, 50)
        sequencesAndRewards[sequence] = reward
    return sequencesAndRewards

def randomize():
    bufferSize = random.randint(5, 10)
    m = random.randint(4, 8)
    n = random.randint(4, 8)
    numOfSequences = random.randint(1, 5)

    matrix = randomizeMatrix(m, n)

    sequencesAndRewards = randomizeSAR(numOfSequences)

    return bufferSize, m, n, matrix, sequencesAndRewards