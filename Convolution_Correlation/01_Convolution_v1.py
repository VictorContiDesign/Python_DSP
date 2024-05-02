from matplotlib import pyplot as plt, style
from scipy import signal
import mysignals as sigs

output_signal = signal.convolve(sigs.InputSignal_1kHz_15kHz, sigs.Impulse_response, mode='same')

style.use('ggplot')

f, plt_arr = plt.subplots(3, sharex=True)
f.suptitle("Convolution")
plt_arr[0].plot(sigs.InputSignal_1kHz_15kHz, color='blue')
plt_arr[1].plot(sigs.Impulse_response, color='orange')
plt_arr[2].plot(output_signal, color='red')    
plt.show() 
