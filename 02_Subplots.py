from matplotlib import pyplot as plt
from matplotlib import style
import mysignals as sig

style.use("ggplot")
# style.use("dark_background")
f, plt_arr = plt.subplots(3, sharex = True)
f.suptitle("Multiplot")

plt_arr[0].plot(sig.InputSignal_1kHz_15kHz, color = "magenta")
plt_arr[0].set_title("Subplot 1", color = "magenta")
plt_arr[1].plot(sig.InputSignal_1kHz_15kHz, color = "orange")
plt_arr[1].set_title("Subplot 2", color = "orange")
plt_arr[2].plot(sig.InputSignal_1kHz_15kHz, color = "red")
plt_arr[2].set_title("Subplot 2", color = "red")

plt.show()