from scipy import signal
from matplotlib import pyplot as plt, style
import numpy as np
import mysignals as sigs

corr_output_signal = signal.correlate(sigs.InputSignal_1kHz_15kHz, sigs.Impulse_response, mode = "same")
conv_output_signal = signal.convolve(sigs.InputSignal_1kHz_15kHz, sigs.Impulse_response, mode = "same")

style.use('ggplot')

plt.plot(corr_output_signal)
plt.show()