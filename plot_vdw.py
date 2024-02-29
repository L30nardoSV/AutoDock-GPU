import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import numpy as np

#filename = 'data_small_vdw'
filename = 'data_vdw'
y = []

with open(filename) as f:
	lines = f.readlines()
	for line in lines:
		s = line.split()
		s = float(s[0])
		y.append(s)

# Identifying lengths, mins, and maxs
leny = len(y); miny = min(y); maxy = max(y)
print("leny =", leny, "\nminy =", miny, "\nmaxy =", maxy)

x = list(range(0, leny))
lenx = len(x); minx = min(x); maxx = max(x)
print("lenx =", lenx, "\nminx =", minx, "\nmaxx =", maxx)

assert leny == lenx, "Number of elements is expected to be the same for both axes"
#print(x); print(y)

# Printing only min and max in ticks
xt = [minx, maxx]
yt = [miny, maxy]
print(xt); print(yt)

# Plotting
fig, ax = plt.subplots()
fig = plt.plot(x, y, marker='o')
ax.set_xticks(xt)
ax.set_yticks(yt)
ax.yaxis.set_major_formatter(FormatStrFormatter('%.7f'))

# Annotating min and max coordinates
xmax = x[np.argmax(y)]
text = "x = {} \ny = {:.7f}".format(xmax, maxy)
ax.annotate(text, xy=(xmax, maxy), xytext=(xmax+10, maxy+40))

xmin = x[np.argmin(y)]
text = "x = {} \ny = {:.7f}".format(xmin, miny)
ax.annotate(text, xy=(xmin, miny), xytext=(xmin+10, miny+40))

plt.xlabel("Samples")
plt.ylabel("Energy (kcal/mol)")

plt.show()
# In a 16GB system, this works well up to input lists of 24 millions element (file size of 230 MB)