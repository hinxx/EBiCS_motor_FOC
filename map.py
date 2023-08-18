

def  map(x, in_min, in_max, out_min, out_max):
  # if input is smaller/bigger than expected return the min/max out ranges value
  if x < in_min:
    return out_min
  elif x > in_max:
    return out_max

  # map the input to the output range.
  # round up if mapping bigger ranges to smaller ranges
  elif (in_max - in_min) > (out_max - out_min):
    return (x - in_min) * (out_max - out_min + 1) / (in_max - in_min + 1) + out_min
  # round down if mapping smaller ranges to bigger ranges
  else:
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


i = 20
i_min = 14
i_max = 52
o_min = 0
o_max = 18000.0 / 38.0
for i in range(0, 60):
    res = -map(i, i_min, i_max, o_min, o_max)
    print("FW @ %d km/h: %d %d" % (i, res, res * 38))
