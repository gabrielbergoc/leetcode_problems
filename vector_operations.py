# This wasn't part of any problem, I just wanted to write these functions on my own

import math

def vector_sum(vetor1, vetor2):
    resp = [0 for i in range(len(max(vetor1, vetor2)))]
    for i in range(len(vetor1)):
        resp[i] = vetor1[i] + vetor2[i]

    return resp


def scalar_product(vetor1, vetor2):
    resp = 0
    for i in range(len(vetor1)):
        resp += vetor1[i] * vetor2[i]

    return resp


def vectorial_product(vetor1, vetor2):
    return [(vetor1[1] * vetor2[2] - vetor1[2] * vetor2[1]), \
            (vetor1[2] * vetor2[0] - vetor1[0] * vetor2[2]), \
            (vetor1[0] * vetor2[1] - vetor1[1] * vetor2[0])]


def vector_module(vetor):
    resp = 0
    for i in range(len(vetor)):
        resp = math.sqrt(resp ** 2 + vetor[i] **2)

    return resp


def angle_btwn_vectors(vetor1, vetor2): # arccos(A.B/|A||B|)

    return math.degrees(math.acos(scalar_product(vetor1, vetor2)
                                  / (vector_module(vetor1) * vector_module(vetor2))))


print('Vector sum')
print()
print('Testing: [1, 1, 1], [2, 2, 2]')
print('Expected: [3, 3, 3]')
print('Answer:', vector_sum([1, 1, 1], [2, 2, 2]))
print()

print('Testing: [1, 1], [2, 2]')
print('Expected: [3, 3]')
print('Answer:', vector_sum([1, 1], [2, 2]))
print()

print('Testing: [1, 10, -1], [2, 20, -2]')
print('Expected: [3, 30, -3]')
print('Answer:', vector_sum([1, 10, -1], [2, 20, -2]))
print()

print('Scalar product')
print()
print('Testing: [1, 1, 1], [2, 2, 2]')
print('Expected: 6')
print('Answer:', scalar_product([1, 1, 1], [2, 2, 2]))
print()

print('Testing: [1, 1], [2, 2]')
print('Expected: 4')
print('Answer:', scalar_product([1, 1], [2, 2]))
print()

print('Testing: [1, 10, -1], [2, 20, -2]')
print('Expected: 204')
print('Answer:', scalar_product([1, 10, -1], [2, 20, -2]))
print()

print('Vector module')
print()
print('Testing: [1, 1, 1]')
print('Expected: 1.7320508075688772')
print('Answer:', vector_module([1, 1, 1]))
print()

print('Testing: [1, 1]')
print('Expected: 1.4142135623730951')
print('Answer:', vector_module([1, 1]))
print()

print('Testing: [1, 10, -1]')
print('Expected: 10.099504938362077')
print('Answer:', vector_module([1, 10, -1]))
print()

print('Vectorial product')
print()
print('Testing: [1, 1, 1], [2, 2, 2]')
print('Expected: ')
print('Answer:', vectorial_product([1, 1, 1], [2, 2, 2]))
print()

print('Testing: [1, 1, 0], [2, 2, 0]')
print('Expected: ')
print('Answer:', vectorial_product([1, 1, 0], [2, 2, 0]))
print()

print('Testing: [1, 10, -1], [2, 20, -2]')
print('Expected: ')
print('Answer:', vectorial_product([1, 10, -1], [2, 20, -2]))
print()

print('Angle between vectors')
print()
print('Testing: [2, 0], [0, 2]')
print('Expected: 90')
print('Answer:', angle_btwn_vectors([2, 0], [0, 2]))
print()

print('Testing: [1, 0], [2, 2]')
print('Expected: 45')
print('Answer:', angle_btwn_vectors([1, 0], [2, 2]))
print()

print('Testing: [1, 0], [-1, 1]')
print('Expected: 135')
print('Answer:', angle_btwn_vectors([1, 0], [-1, 1]))
print()

print('Testing: [1, 0], [-1, -1]')
print('Expected: 135')
print('Answer:', angle_btwn_vectors([1, 0], [-1, -1]))
print()

print('Testing: [1, 1], [2, 2]')
print('Expected: 0')
print('Answer:', angle_btwn_vectors([1, 1], [2, 2]))
print()

print('Testing: [1, 1], [-1, -1]')
print('Expected: 180')
print('Answer:', angle_btwn_vectors([1, 1], [-1, -1]))
print()