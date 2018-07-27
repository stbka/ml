import math
# https://www.youtube.com/watch?v=pyJa2kpWYtM

# euklidische Distanz zweier n-dimensionaler Vektoren
def euk_dist(x, y, d):
    r = .0
    for i in range(d):
        r += (x[i] - y[i])**2
    print "distance: " + str(math.sqrt(r))
    return math.sqrt(r)  

# Maximums-Distanz
def max_dist(x, y, d):
    r = .0
    for i in range(d):
        r_tmp = (x[i] - y[i]) * -1
        r = r_tmp if r_tmp > r else r
    print "distance: " + str(r)
    return r

# Taxicab Distanz
def taxicab_dist(x, y, d):
    r = .0
    for i in range(d):
        r += (x[i] - y[i]) * -1
    print "distance: " + str(r)
    return r

# TODO: Levensthein Distanz
def lev_dist(w_1, w_2):
    pass