import numpy as np
import random

def NeighborJoin(D): # D: distance matrix
    # init parameters
    n = D.shape[0]  # number of nodes (sequences)
    T = np.zeros((n - 1, 5))  # T: tree
    s = 0 # s: index of T
    seqID = np.zeros(n)  # seqID: list to record sequence ID (random number between 100 and 999)
    for i in range(n):
        seqID[i] = random.randint(100, 999)

    tempSeqID = seqID.copy()  # tempSeqID: temporary sequence ID list use to compute

    # do neighbor join until there is only one node left
    while D.shape[0] > 1:

        r = np.zeros(n)  # r: net divergence
        q = np.zeros((n, n))  # q: adjusted distance

        # compute r
        # if there are only two nodes left, compute r directly
        if n == 2:
            T[s, 0] = 0
            T[s, 1] = tempSeqID[0]
            T[s, 2] = tempSeqID[1]
            T[s, 3] = T[s, 4] = D[0, 1]

            return T, seqID
        
        for i in range(n):
            r[i] = (1 / (n - 2)) * np.sum(D[i])

        # compute q
        for i in range(n):
            for j in range(n):
                if i == j:
                    q[i, j] = 0
                else:
                    q[i, j] = D[i, j] - r[i] - r[j]
   
        # find min q
        min_q = np.inf # inf means infinity
        for j in range(n):
            for k in range(n):
                if j != k and q[j, k] < min_q:
                    min_q = q[j, k]
                    min_j = j
                    min_k = k

        # compute new node (parent of min_j and min_k)
        T[s, 0] = random.randint(50, 99) # random number between 100 and 999 for new node ID
        T[s, 1] = tempSeqID[min_j] # min_j is the left child of new node
        T[s, 2] = tempSeqID[min_k] # min_k is the right child of new node

        # compute distance to new node
        T[s, 3] = (D[min_j, min_k] + r[min_j] - r[min_k]) / 2
        T[s, 4] = (D[min_j, min_k] + r[min_k] - r[min_j]) / 2

        # update seqID
        tempSeqID[min_j] = T[s, 0]
        tempSeqID = np.delete(tempSeqID, min_k) 
        np.insert(seqID, seqID.shape[0], T[s, 0]) # insert new node ID to seqID

        # update s
        s += 1

        # update D
        for i in range(n):
            if i != min_j and i != min_k:
                D[i, min_j] = D[min_j, i] = (D[i, min_j] + D[i, min_k] - D[min_j, min_k]) / 2
        
        # remove min_k
        D = np.delete(D, min_k, 0)
        D = np.delete(D, min_k, 1)

        # update n
        n = D.shape[0]
        # while loop ends here



    