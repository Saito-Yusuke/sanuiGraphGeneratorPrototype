import numpy as np
import pandas as pd
import scipy.stats as stt
import matplotlib.pyplot as plt
import matplotlib.lines as lin

df = pd.read_csv('sample.csv')
header = df.columns.values.tolist()
data = df.values

xi = df['RUN_CAN'].T + df['AUX_CAN'].T + df['AC_CAN'].T
yi = df['RUN_ECOLOG'].T + df['AUX_CAN'].T + df['AC_NN'].T
sum_xx = sum(xi * xi)
sum_xy = sum(xi * yi)
slope = sum_xy / sum_xx
sigma = np.std(yi - slope * xi)

print("回帰直線の傾き = " + str(slope))
print("回帰直線との標準偏差 = " + str(sigma))

fig = plt.figure()
ax = fig.add_subplot(111)
left = np.array(df['RUN_CAN'].T + df['AUX_CAN'].T + df['AC_CAN'].T)
height_run = np.array(df['RUN_ECOLOG'].T)
height_aux = np.array(df['AUX_CAN'].T)
height_ac = np.array(df['AC_NN'].T)
line = lin.Line2D([0, 5], [0, slope * 5],linewidth = 3, color = "black")
line_sigma = lin.Line2D([0, 5], [sigma, slope * 5 + sigma], color = "black")
line_2sigma = lin.Line2D([0, 5], [2 * sigma, slope * 5 + 2 * sigma], color = "black")
line_minus_sigma = lin.Line2D([0, 5], [-1 * sigma, slope * 5 - sigma], color = "black")
line_minus_2siguma = lin.Line2D([0, 5], [-2 * sigma, slope * 5 - 2 * sigma], color = "black")
p_run = plt.bar(left, height_run, color = "green", width = 0.01)
p_aux = plt.bar(left, height_aux, bottom = height_run, color = "yellow", width = 0.01)
p_ac = plt.bar(left, height_ac, bottom = height_run + height_aux, color = "blue", width = 0.01)
ax.add_line(line)
ax.add_line(line_sigma)
ax.add_line(line_2sigma)
ax.add_line(line_minus_sigma)
ax.add_line(line_minus_2siguma)
plt.title("ECOLOG Estimation Accuracy", fontsize = 15)
plt.xlabel("Energy Consumption from CAN [kWh]", fontsize = 12)
plt.ylabel("Estimated Energy Consumption [kWh]", fontsize = 12)
ax.set_aspect('equal')
#plt.grid(True)
plt.legend((p_run[0], p_aux[0], p_ac[0]), ("ECOLOG Estimation", "AUX Consumption", "AC Estimation"))
plt.show()