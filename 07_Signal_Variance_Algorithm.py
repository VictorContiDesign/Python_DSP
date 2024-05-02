import mysignals as sigs

_mean = 0.0
_variance = 0.0

def calc_variance(sigs_src_arr):
    # Variables declaration
    global _mean
    global _variance
    # Mean calculation
    for x in range(len(sigs_src_arr)):
        _mean += sigs_src_arr[x]
    _mean = _mean / len(sigs_src_arr)
    # Variance calculation
    for y in range(len(sigs_src_arr)):
        _variance += ((sigs_src_arr)[y] - _mean)**2
    _variance = _variance / len(sigs_src_arr)
    return _variance

result = calc_variance(sigs.InputSignal_1kHz_15kHz)
print(result)  
