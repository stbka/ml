# k-nearest neighbours algorithm
# Theorie: https://www.youtube.com/watch?v=FghB26KmQG0
# Mathematik: https://www.youtube.com/watch?v=gMq4goRUg4k  
# Pseudo-Code: https://www.youtube.com/watch?v=1HZU5pHGOCY

# x_i = vector
# data = vector array
# d = vector dimensions (without positive=0/1 as last dimension)
# k = number of neighbours to check 
# dist_alg = algorithm to calc distance
#
def calcKnn(x_i, data, d, k, dist_alg, weighted):
    
    k_nearest = []
    # x_j = [a_1, a_2, ... , a_n-1=1(pos)/-2(neg), a_n=distance]
    positive = 0
    
    for x_j in data:
        
        #calculate distance
        dist = dist_alg(x_i, x_j, d)  
        x_j.append(dist) 
        
        # fill array  
        if len(k_nearest) < k:
            k_nearest.append(x_j)
            continue

        # find p with max distance
        k_biggest = 0
        for i in range(k):
            if k_nearest[i][-1] > k_nearest[k_biggest][-1]:
                k_biggest = i
        
        # replace p with max distance    
        if x_j[-1] < k_nearest[k_biggest][-1]:
            k_nearest[k_biggest] = x_j
           
    for x_j in k_nearest:
        if weighted and x_j[-1] > 0:
            positive += 1/x_j[-1] * x_j[-2]
        else:
            positive += x_j[-2]
            
    if positive > 0:
        return positive, True
    else:
        return positive, False


# KNN 
def knn(x_i, data, d, k, dist_alg):
    
    return calcKnn(x_i, data, d, k, dist_alg, False)


# KNN weighted
def wknn(x_i, data, d, k, dist_alg):
    
    return calcKnn(x_i, data, d, k, dist_alg, True)