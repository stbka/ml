import Distance
import Knn

data = [[1, 2, 3, 1],
        [2, 3, 4, 1],
        [3, 4, 5, -1],
        [4, 5, 6, -1]]

p = [5, 10, 3]

print 'Euklidische Distanz: ' + str(Knn.wknn(p, data, 3, 4, Distance.euk_dist))
print 'Maximums Distanz: ' + str(Knn.wknn(p, data, 3, 4, Distance.max_dist))
print 'Taxicab Distanz: ' + str(Knn.wknn(p, data, 3, 4, Distance.taxicab_dist))
