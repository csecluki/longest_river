import numpy as np
from random import randint

# 1 -> river
# 0 -> land

visited = []
unchecked = []
connected = []
river_length_array = []


def matrix_generator():
    matrix_builder = np.random.randint(2, size=[randint(4, 5), randint(8, 9)])
    matrix_x, matrix_y = matrix_builder.shape

    add_h = np.reshape(np.zeros(matrix_x, dtype=int), (matrix_x, 1))
    add_v = np.zeros(matrix_y + 2, dtype=int)

    matrix_builder = np.hstack((add_h, matrix_builder, add_h))
    matrix_builder = np.vstack((add_v, matrix_builder, add_v))

    return matrix_builder


def river():
    global p, q
    p = 0
    q = 0
    while True:
        while True:
            if p in range(matrix.shape[0]):
                if q in range(matrix.shape[1]):
                    if matrix[p][q] == 1:
                        visited.append([p, q])
                        q += 1
                        continue
                    else:
                        q += 1
                        continue
                else:
                    q = 0
                    p += 1
                    continue
            else:
                break
        break


def look_for_neighbour(n, m):
    if [n, m] not in connected:
        connected.append([n, m])
        unchecked.append(([n, m]))
    else:
        pass
    neighbours = [[n - 1, m], [n + 1, m], [n, m - 1], [n, m + 1]]
    for neighbour in neighbours:
        if neighbour in visited:
            if neighbour not in connected:
                unchecked.append(neighbour)
                connected.append(neighbour)
            else:
                pass
        else:
            pass
    unchecked.remove([n, m])
    visited.remove([n, m])
    if len(unchecked) > 0:
        n, m = unchecked[0]
        look_for_neighbour(n, m)
    else:
        river_length_array.append(len(connected))
        connected.clear()
    while len(visited) > 0:
        n, m = visited[0]
        look_for_neighbour(n, m)
    else:
        pass


if __name__ == '__main__':
    matrix = matrix_generator()
    river()
    if len(visited) > 0:
        p, q = visited[0]
        look_for_neighbour(p, q)
    else:
        print("There's no river")

    print(matrix)
    print(river_length_array)
    print(max(river_length_array))
