import numpy as np
import NeighborJoin as nj

if __name__ == '__main__':
    D = np.array([
        [0, 4, 5, 10],
        [4, 0, 7, 12],
        [5, 7, 0, 9],
        [10, 12, 9, 0]])  # distance matrix

    T, seqID = nj.NeighborJoin(D)
    print(T)
    print(seqID)
