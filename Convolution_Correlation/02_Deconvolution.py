from scipy import signal
from matplotlib import pyplot as plt, style
import numpy as np

sig = np.array([0,0,0,0,1,1,1,1])
filter = np.array([1,1,0])

conv_result = signal.convolve(sig, filter)
deconv_result = signal.deconvolve(conv_result, filter)

print(f" Convolution result : {conv_result}")
print(f" Deconvolution result : {deconv_result}")

style.use('ggplot')

f, plt_arr = plt.subplots(4, sharex=True)
plt_arr[0].plot(sig, color = "blue")
plt_arr[0].set_title("Input Signal", color = "blue")

plt_arr[1].plot(filter, color = "green")
plt_arr[1].set_title("Filter", color = "green")

plt_arr[2].plot(conv_result, color = "brown")
plt_arr[2].set_title("Convolution Output Signal", color = "brown")

plt_arr[3].plot(deconv_result[0], color = "red")
plt_arr[3].set_title("Deconvolution Input Signal", color = "red")

# plt_arr[4].plot(deconv_result[1], color = "red")
# plt_arr[4].set_title("Deconvolution Output Filter", color = "red")

plt.show()