# In a 16GB system, this works well up to input lists of 
# 24 millions element (file size of 230 MB)

# make DEVICE=GPU TARGETS=86 test > data_vdw

# python3 plot_vdw.py precisionlogs/1mzc_ad

import matplotlib.pyplot as plt
from matplotlib.ticker import FormatStrFormatter
import numpy as np

import sys

import os
path = './precisionlogs'
dir_list = os.listdir(path)
print("Files and directories in ", path, ":")
print(dir_list)

search_text = "vdw = "

vdw = []
el = []
desol = []

all_min_vdw = []
all_min_el  = []
all_min_desol = []

all_max_vdw = []
all_max_el  = []
all_max_desol = []

for myfile in dir_list:
	filename = path + '/' + myfile

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
	len_el = len(el); min_el = min(el); max_el = max(el)
	len_desol = len(desol); min_desol = min(desol); max_desol = max(desol)
	print("\n", filename)
	print("len_vdw =", len_vdw,   "\tmin_vdw =", min_vdw,   "\tmax_vdw =", max_vdw)
	print("len_el  =", len_el,    "\tmin_el  =", min_el,    "\tmax_el  =", max_el)
	print("len_des =", len_desol, "\tmin_des =", min_desol, "\tmax_des =", max_desol)

	x = list(range(0, len_vdw))
	len_x = len(x); min_x = min(x); max_x = max(x)

	assert len_x == len_vdw == len_el == len_desol, "Number of elements is expected to be the same for both axes"

	# Printing only min and max in ticks
	t_x = [min_x, max_x]
	t_vdw = [min_vdw, max_vdw]
	t_el = [min_el, max_el]
	t_desol = [min_desol, max_desol]

	min_all = min(min_vdw, min_el, min_desol)
	max_all = max(max_vdw, max_el, max_desol)
	t_all = [min_all, max_all]
	print("min_all =", min_all, "\tmax_all =", max_all)

	# Appending all mins and maxs
	all_min_vdw.append(min_vdw); all_max_vdw.append(max_vdw)
	all_min_el.append(min_el); all_max_el.append(max_el)
	all_min_desol.append(min_desol); all_max_desol.append(max_desol)

#	# Plotting
#	fig, axs = plt.subplots(3, sharex=True)
#	axs[0].plot(x, vdw, color = 'lightcoral', marker='o')
#	axs[0].set_title('Van der Waals', rotation = 0, position = (1, 0.1), ha = 'left', va = 'center', fontsize = 15, color='lightcoral')
#	axs[0].set_ylabel('Energy (kcal/mol)')
#	axs[0].set_xticks(t_x)
#	axs[0].set_yticks(t_vdw)
#	axs[0].xaxis.set_major_formatter(FormatStrFormatter('%d'))
#	axs[0].yaxis.set_major_formatter(FormatStrFormatter('%.7f'))
#
#	axs[1].plot(x, el, color = 'aquamarine', marker='x')
#	axs[1].set_title('Electrostatic', rotation = 0, position = (1, 0.1), ha = 'left', va = 'center', fontsize = 15, color='aquamarine')
#	axs[1].set_ylabel('Energy (kcal/mol)')
#	axs[1].set_yticks(t_el)
#	axs[1].yaxis.set_major_formatter(FormatStrFormatter('%.7f'))
#
#	axs[2].plot(x, desol, color = 'greenyellow', marker='4')
#	axs[2].set_title('Desolvation', rotation = 0, position = (1, 0.1), ha = 'left', va = 'center', fontsize = 15, color='greenyellow')
#	axs[2].set_ylabel('Energy (kcal/mol)')
#	axs[2].set_yticks(t_desol)
#	axs[2].yaxis.set_major_formatter(FormatStrFormatter('%.7f'))
#
#	# Annotating min and max coordinates
#	xmax_vdw = x[np.argmax(vdw)]
#	text = "vdw = {:.7f} \nsample = {}".format(max_vdw, xmax_vdw)
#	axs[0].annotate(text, xy=(xmax_vdw, max_vdw))
#
#	xmin_vdw = x[np.argmin(vdw)]
#	text = "vdw = {:.7f} \nsample = {}".format(min_vdw, xmin_vdw)
#	axs[0].annotate(text, xy=(xmin_vdw, min_vdw))
#
#	xmax_el = x[np.argmax(el)]
#	text = "el = {:.7f} \nsample = {}".format(max_el, xmax_el)
#	axs[1].annotate(text, xy=(xmax_el, max_el))
#
#	xmin_el = x[np.argmin(el)]
#	text = "el = {:.7f} \nsample = {}".format(min_el, xmin_el)
#	axs[1].annotate(text, xy=(xmin_el, min_el))
#
#	xmax_desol = x[np.argmax(desol)]
#	text = "desol = {:.7f} \nsample = {}".format(max_desol, xmax_desol)
#	axs[2].annotate(text, xy=(xmax_desol, max_desol))
#
#	xmin_desol = x[np.argmin(desol)]
#	text = "desol = {:.7f} \nsample = {}".format(min_desol, xmin_desol)
#	axs[2].annotate(text, xy=(xmin_desol, min_desol))

	# TODO: Calculating minimum number of bits
	# required for correct representation
	#https://www.mathworks.com/help/dsp/ug/concepts-and-terminology.html

	# Label in x axis is shared
#	plt.xlabel("Samples")
#	plt.show()

#print('\n')
#print(all_min_vdw); print(all_max_vdw)
#print(all_min_el); print(all_max_el)
#print(all_min_desol); print(all_max_desol)
print('\nMins and maxs in all tests')
print("min_vdw = ", min(all_min_vdw), "\tmax_vdw = ", max(all_max_vdw))
print("min_el = ", min(all_min_el), "\tmax_el = ", max(all_max_el))
print("min_desol = ", min(all_min_desol), "\tmax_desol = ", max(all_max_desol))
