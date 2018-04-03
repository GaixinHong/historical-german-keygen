import random as ra;

def first(a,b):
    for i in a:
        if (i in b):
            return i;
        

def KeyGen():
    V1 = list(range(2,10))
    V2 = V1[:]
    V3 = list(range(1,37))    
    V4 = V3[:]
    ra.shuffle(V1)
    ra.shuffle(V2)
    ra.shuffle(V3)
    ra.shuffle(V4)
#    print(V1, V2, V3, V4)
    
    L1 = list(range(2,9))
    l1 = first(L1, V1)
    
    if (l1 in [2, 3, 4]):
        L2 = [5, 7, 8];
    elif (l1 in [6, 7 ,8]):
        L2 = [2, 3, 4];

    l2 = first(L2, V1)

#    print(V2);     
    
    V2.remove(5)
    V2.remove(6)

#    print(V2);     
    
    if l1 != 6:
        V2.insert(l1, 5)
        V2.insert(l2, 6)
    else:
        V2.insert(l2, 6)
        V2.insert(l1, 5)

#    print(V2);
    
    D = [None] * 9
    for i in range(1, 9):
        D[i] = 0;
    D[0] = 0
    D[V2[0]-1] = 4
    for i in range(1, 8):
        D[V2[i]-1] = 4 * V2[i-1]

    P = [None] * 27

    P[2] = 33
    P[6] = 5
    P[8] = 9
    P[14] = 21
    P[17] = 25
    P[23] = 29

    P[19] = 4*V2[7]
    P[5] = D[7]
    P[12] = D[6]

#    print(P)

    l3 = first([1,2,4,5], V3)

    S = [1,2,4,5,21,22,23,25,26]
    l4 = first([x for x in S if (x != l3)],V3)

    S = [1,2,4,5,14,16,17,19,21,22,23,25,26]
    l5 = first([x for x in S if (x not in [l3, l4])], V3)
    l6 = first([x for x in S if (x not in [l3, l4] and x != l5)], V3)

    S = [3,6,7,9,13,15,18,20,24,l3,l4,l5,l6]
    l7 = first([x for x in range(1, 27) if (x not in S)], V3)
    l8 = first([x for x in range(1, 27) if (x not in S and x != l7)], V3)

#    print(P)
    
    P[l3-1] = D[2]
    P[l4-1] = D[3]
    P[l5-1] = D[4]
    P[l6-1] = D[5]
    P[l7-1] = D[1]
    P[l8-1] = D[8]

    V5 = [None] * 21;
    W = [5,9,21,25,29,33]
    k = 0;
    for i in V4:
        if (i % 4 == 0):
            continue;
        if (i in W):
            continue;
        V5[k] = i;
        k = k + 1;

    
    k = 0;
    for i in range(len(P)):
        if (P[i] == None):
            P[i] = V5[k];
            k = k + 1;
       
    alpha = ra.choice([x for x in range(1, 37) if (x not in [5,9,21,25,29,33])])
    
    return D, P, alpha


