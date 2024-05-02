from matplotlib import pyplot as plt, style
import mysignals as sigs

style.use('ggplot')

f, plt_arr = plt.subplots(2, sharex=True)
plt_arr[0].plot(sigs.InputSignal_1kHz_15kHz)
plt_arr[1].plot(sigs.Impulse_response)   
plt.show() 
