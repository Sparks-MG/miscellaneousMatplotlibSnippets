import matplotlib as plt
fig= plt.figure()
ax=fig.add_subplot(111)

#Formatting the axis in scientific notation
from matplotlib.ticker import FormatStrFormatter
formatter = mtick.ScalarFormatter(useMathText=True)
formatter.set_powerlimits((-3,2))
ax.yaxis.set_major_formatter(formatter)