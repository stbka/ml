import numpy as np
import ImageGen

v_min = 0
v_max = 100
p_num = 100
p_dim = 2

data = np.random.random_integers(v_min, v_max, size=(p_num,p_dim))
center_1 = np.array([[v_max * .95, v_max * .95]])
center_2 = np.array([[v_max * .05, v_max * .05]])

imgg = ImageGen.ImageGen(v_max, v_max)

imgg.plot2dArray(center_1, 'ro')
imgg.plot2dArray(center_2, 'go')
imgg.plot2dArray(data, 'bo', .5)
imgg.store('../data/images-run-1')

center_changed = True
while center_changed:


