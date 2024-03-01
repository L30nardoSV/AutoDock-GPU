# In a 16GB system, this works well up to input lists of 
# 24 millions element (file size of 230 MB)

# make DEVICE=GPU TARGETS=86 test > data_vdw

import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import numpy as np

#filename = 'data_small_vdw'
filename = 'data_vdw'
search_text = "vdw = "

vdw = []
el = []
desol = []

with open(filename) as f:
	lines = f.readlines()
	for line in lines:
		if search_text in line:
			#print(line)
			s = line.split()
			#print(s)
			vdw.append(float(s[2]))
			el.append(float(s[5]))
			desol.append(float(s[8]))
			#print(vdw)

# Identifying lengths, mins, and maxs
len_vdw = len(vdw); min_vdw = min(vdw); max_vdw = max(vdw)
print("len_vdw =", len_vdw, "\nmin_vdw =", min_vdw, "\nmax_vdw =", max_vdw)

x = list(range(0, len_vdw))
len_x = len(x); min_x = min(x); max_x = max(x)
print("len_x =", len_x, "\nmin_x =", min_x, "\nmax_x =", max_x)

assert len_vdw == len_x, "Number of elements is expected to be the same for both axes"
#print(x); print(y)

# Printing only min and max in ticks
t_x = [min_x, max_x]
t_vdw = [min_vdw, max_vdw]
print(t_x); print(t_vdw)

# Plotting
fig, ax = plt.subplots()
fig = plt.plot(x, vdw, marker='o')
ax.set_xticks(t_x)
ax.set_yticks(t_vdw)
ax.yaxis.set_major_formatter(FormatStrFormatter('%.7f'))

# Annotating min and max coordinates
xmax = x[np.argmax(vdw)]
text = "vdw = {:.7f} \nsample = {}".format(max_vdw, xmax)
ax.annotate(text, xy=(xmax, max_vdw), xytext=(xmax+10, max_vdw+40))

xmin = x[np.argmin(vdw)]
text = "vdw = {:.7f} \nsample = {}".format(min_vdw, xmin)
ax.annotate(text, xy=(xmin, min_vdw), xytext=(xmin+10, min_vdw+40))

plt.xlabel("Samples")
plt.ylabel("Energy (kcal/mol)")

plt.show()