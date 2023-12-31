#!/usr/bin/env python3
#program for producing a graph of spherical volume based on dimension and radius

import math
import matplotlib.pyplot as plt
import matplotlib.colors as colors
import numpy
import pprint

def volume(n, r):
    return math.pi**(n/2.0) / math.gamma(n/2.0 + 1) * r**n


#plt.imshow(a, cmap="hot",interpolation="nearest")
#plt.show()

arr = []
starting = True
min, max
for n in range(50):
    arr.append([])
    for i_r in range(20):
        vol = volume(n, 1.0 + 0.05*i_r)
        if starting:
            min, max = vol, vol
            starting = False
        else:
            if vol > max: max = vol
            if vol < min: min = vol
        #print(str(n) + ","+str(1.0 + 0.05*i_r))
        arr[n].append(vol)
#pprint(arr)

#for s in arr:
#    print(s)
left = 1.0
right = 2.0
top = 0
bottom = 50
extent = [left, right, bottom, top]

#fig, ax = plt.subplots()
ax = plt.gca()
#plt.imshow(arr, cmap="gnuplot", interpolation="nearest")
#cmap = plt.get_cmap("gnuplot", arr)
pcm = plt.pcolor(arr,norm=colors.LogNorm(vmin=min,vmax=max), shading='auto')
print(min)
print(max)
ax.set_xticks([0, 9, 19], ["1.0", "1.5","2.0"])
plt.colorbar(pcm, ax=ax, extend="max")
plt.xlabel("Radius ")
plt.ylabel("Dimension (n)")
plt.title("Volume of n-dimensional sphere")
#plt.logscale()
plt.savefig("Pic.pdf")
plt.show()
print(volume(8, 5))

