import matplotlib.pyplot as plt
import matplotlib.ticker as ticker
import numpy as np
import os

plt.rcParams.update({
  'font.size'        : 9, 
  'font.weight'      : 'bold', 
  'figure.facecolor' : 'w',
  'figure.dpi'       : 500,
  'figure.figsize'   : (6,3),
  # basic properties
  'axes.linewidth'   : 1,
  'xtick.top'        : True,
  'xtick.direction'  : 'in',
  'xtick.major.size' : '2',
  'xtick.major.width': '1',
  'ytick.right'      : True,
  'ytick.direction'  : 'in',
  'ytick.major.size' : '2',
  'ytick.major.width': '1', 
  'axes.grid'        : False,
  'grid.linewidth'   : '1',
  'legend.fancybox'  : False,
  'legend.framealpha': 1,
  'legend.edgecolor' : 'black',
  # case dependent
  'axes.autolimit_mode': 'round_numbers', # 'data' or 'round_numbers'
  'lines.linewidth'  : 1,
  'lines.markersize' : 6,
})

# Placeholder data
cases = ['StreamDedup, 80% dup', 'StreamDedup, 50% dup', 'HW Baseline, 80% dup', 'HW Baseline, 50% dup']
node_lst = [idx for idx in range(1, 11)]

condition_1 = [
5287290.0,
5294440.0,
5292200.0,
5293070.0,
5292110.0,
5296000.0,
5296992.857142857,
5297015.0,
5296911.111111111,
5297067.0,
]

condition_2 = [
5286860.0,
5293810.0,
5312403.333333333,
5298620.0,
5298726.0,
5302045.0,
5301592.857142857,
5302897.5,
5304198.888888889,
5308070.0,
]

data = {'node_count': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 
        'max_hop_count': [0, 2, 2, 2, 2, 4, 4, 4, 4, 4],
        'avg_hop_count': [0.0, 1.0, 1.3333333333333333, 1.5, 1.6, 2.0, 2.2857142857142856, 2.25, 2.2222222222222223, 2.4]}
latency_data = [a for a in data['max_hop_count']]
util_data = [a*512/(4096*8)/2 for a in data['avg_hop_count']]

throughput_1 = [16384*4.096/(condition_1[idx]/1000) * (idx + 1) * (1-util_data[idx]) for idx in range(len(condition_1))]
throughput_2 = [16384*4.096/(condition_2[idx]/1000) * (idx + 1) * (1-util_data[idx]) for idx in range(len(condition_2))]
throughput_3 = [12.8 * (n + 1) for n in range(2)]
throughput_4 = [51/5 * (n + 1) for n in range(2)]
print(np.asarray(throughput_1))
print(np.asarray(throughput_2))
# Number of cases
n_cases = len(cases)

# Creating the bar plot
fig, ax = plt.subplots()

# line1, = plt.plot(node_lst, throughput_1, label=cases[0], marker='o', zorder=3, color = '#1f77b4',)
# line2, = plt.plot(node_lst, throughput_2, label=cases[1], marker='x', zorder=3, color = '#1f77b4',)
# line3, = plt.plot(node_lst, throughput_3, label=cases[2], marker='+', zorder=3, color = '#ff7f0e',)
# line4, = plt.plot(node_lst, throughput_4, label=cases[3], marker='v', zorder=3, color = '#ff7f0e',)
# line5, = plt.plot(node_lst, throughput_5, label=cases[4], marker='^', zorder=3, color = '#2ca02c',)
# default color: ['#1f77b4', '#ff7f0e', '#2ca02c', '#d62728', '#9467bd', '#8c564b', '#e377c2', '#7f7f7f', '#bcbd22', '#17becf']
line1, = plt.plot(node_lst, throughput_1, label=cases[0], marker='s', markersize = 10, zorder=3, linestyle='-', linewidth = 2)
line2, = plt.plot(node_lst, throughput_2, label=cases[1], marker='d', markersize = 9, zorder=3, linestyle='-', linewidth = 2)
line3, = plt.plot([(n+1) for n in range(2)], throughput_3, label=cases[2], marker='x', markersize = 8, zorder=3, markeredgewidth=2, linewidth = 2)
line4, = plt.plot([(n+1) for n in range(2)], throughput_4, label=cases[3], marker='+', markersize = 10, zorder=3, markeredgewidth=2, linewidth = 2)
line1.set_clip_on(False)
line2.set_clip_on(False)
line3.set_clip_on(False)
line4.set_clip_on(False)

# line for 12.7
position_127GB = 124.3
plt.axhline(y = position_127GB, color = 'r', linestyle = 'dashed', linewidth = 1, zorder = 5)
plt.text(5.5, position_127GB*1.02, f"124.3 GB/s", fontsize = 8, rotation=0, rotation_mode='anchor', weight = 'bold', ha = 'center', va = 'bottom')

arrow_config = dict(facecolor='black', shrink=0.05, width=1, headwidth=4, headlength=5, linewidth=0.5)
ax.annotate(f"", xy=(2, 35), xytext=(2, 70), fontsize = 8,
                arrowprops=arrow_config, ha='left', va='bottom')
plt.text(1.2, 73, f"Only 2 Nodes in\nHW Baseline", fontsize = 9, rotation=0, rotation_mode='anchor', weight = 'bold', ha = 'left', va = 'bottom')
# ax.annotate(f"Evaluation in HW baseline only up to 2 nodes", xy=(2, 30), xytext=(2, 100), fontsize = 8,
#                 arrowprops=arrow_config, ha='left', va='bottom')

# Adding labels and title
ax.set_xlabel('Number of FPGA nodes', fontsize = 9, weight = 'bold')
ax.set_ylabel('Throughput [GB/s]', fontsize = 9, weight = 'bold')
ax.set_xticks(node_lst)
# ax.tick_params(axis='x', which='both', length=0, width=0)  # Adjust length and width as needed
# ax.set_xticklabels(cases)

legend = plt.legend()
ax.legend(loc='upper center', bbox_to_anchor=(0.5, 1.3), ncol=2)
legend.get_frame().set_linewidth(1)
# legend.get_frame().set_edgecolor("b")

# plt.xlim([0 + (bar_dist + bar_width) / 2 - bar_width - 0.2, n_cases - 1 + (bar_dist + bar_width) / 2 + bar_width + 0.2])
plt.xlim([1, 10])
plt.ylim([0, 150])
# plt.yscale('log')
# ax.yaxis.set_major_locator(ticker.MultipleLocator(2))
# ax.yaxis.set_minor_locator(ticker.MultipleLocator(0.5))

# Adjusting the layout
plt.subplots_adjust(left=0.1, right=0.95, top=0.8, bottom=0.17)
# Alternatively
# plt.tight_layout()

# Function to save the plot in a given directory in both PNG and PDF formats
def save_plot(directory, filename):
    # Create the directory if it doesn't exist
    os.makedirs(directory, exist_ok=True)
    plt.savefig(f"{directory}/{filename}.png")
    plt.savefig(f"{directory}/{filename}.pdf")

# Example usage (replace 'your_directory_path' with the actual path)
save_plot('./section3', 'plot1_throughput_node_line_full_corrected')


# marker_lst      = ['o','x','+','v','^','s','d']
# # marker_size_lst =  [1,  2,  3,  1,  1,  1,  1]
# marker_size_lst =  [2,  3,  4,  2,  2,  2,  2]
# marker_idx = 2
# save_format_lst = ['pdf', 'png']
# case_lst = ['Insertion', 'Deletion']
# case_file_lst = ['insertion_6FSM_BF', 'deletion_6FSM_BF']

# case_lst.reverse()
# case_file_lst.reverse()

# fig, ax1 = plt.subplots()

# for case_idx in range(len(case_lst)):
#   case_label = case_lst[case_idx]
#   case_file = case_file_lst[case_idx]
#   latency_data_csv = pd.read_csv('./plot1/'+ case_file + '_latency.csv')
#   latency_data = latency_data_csv.iloc[:, [1]].to_numpy().reshape([-1])
#   fullness_data = [0.1 + idx * 0.1 for idx in range(10)]
  
#   # data extracted, plot
#   # plt.plot(fullness_data, latency_data, label = f"Hash Table Fullness = {fullness:.0%}", marker = marker_lst[marker_idx], markersize = marker_size_lst[marker_idx])
#   plt.plot(fullness_data, latency_data, 
#            linewidth=2, 
#            label = case_label, 
#            marker = marker_lst[marker_idx], 
#            markersize = marker_size_lst[marker_idx]+2,
#            markeredgewidth = 2)
#   marker_idx = marker_idx - 1
# print(max_freq_lst)
# print(power_at_max_freq_lst)

# if case_name == 'mmfp32':
#   plt.plot([370, 340, 310, 280, 250, 220, 180],
#            [35.296729199999994, 29.6508939, 24.7147813, 20.34978855, 16.48387, 13.0884749, 9.666480600000002],
#            '-.',linewidth = 1, alpha = 1)
#   plt.text(250, 14, "Max Frequency", fontsize = 7, rotation=40, rotation_mode='anchor')
#   plt.title("MATMUL FP32 Power vs. Frequency", weight = 'bold')
# elif case_name == 'mmint32':
#   plt.plot([370, 340, 310, 280, 250, 220, 180],
#            [29.155039200000004, 24.556644599999995, 20.453543, 16.86332025, 13.600857, 10.78313555, 7.947639899999999],
#            '-.',linewidth = 1, alpha = 1)
#   plt.text(250, 11, "Max Frequency", fontsize = 7, rotation=35, rotation_mode='anchor', weight = 'bold')
#   plt.title("MATMUL INT32 Power vs. Frequency",  weight = 'bold')

# legend = plt.legend()
# legend.get_frame().set_linewidth(1)
# # legend.get_frame().set_edgecolor("b")

# plt.xlim([0, 1])
# plt.ylim([0,35])

# plt.axhline(y = ((12/4)/1.024), color = 'r', linestyle = 'dashed')
# plt.text(1.01, 2.85, f"12 GB/s", fontsize = 6, rotation=0, rotation_mode='anchor', weight = 'bold')
# plt.text(0.45, 2.6, f"12 GB/s", fontsize = 6, rotation=0, rotation_mode='anchor', weight = 'bold')

# ax1.set_xticklabels(['{:,.0%}'.format(x) for x in [0 + idx * 0.2 for idx in range(6)]])

# # plt.xticks(x, weight = 'bold')
# plt.xlabel("Hash Table Fullness", fontsize = 9, weight = 'bold')
# plt.ylabel("Latency[us]", fontsize = 10, weight = 'bold')


# for save_format in save_format_lst:
#   plt.savefig("./plot1/" + "latency_fullness_6FSM_BF_big." + save_format)