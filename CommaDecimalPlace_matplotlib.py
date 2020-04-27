#Python Test Gist
#Komma statt Punkt bei Matplotlib: https://stackoverflow.com/questions/49445935/change-decimal-point-to-comma-in-matplotlib-plot?rq=1
#Locale settings
import locale
# apply German locale settings
locale.setlocale(locale.LC_ALL, 'de_DE')
# Tell matplotlib to use the locale we set above
plt.rcParams['axes.formatter.use_locale'] = True