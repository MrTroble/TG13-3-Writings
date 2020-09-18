import matplotlib.pyplot as plot


def plotovertime(functions, samplerate, samplefactor):
    time = []
    lists = []
    for x in functions:
        lists.append([])
    for x in range(samplerate):
        timeinput = x * samplefactor
        time.append(timeinput)
        for i in range(len(functions)):
            lists[i].append(functions[i](timeinput))
    for lis in lists:
        plot.plot(time, lis)
    plot.show()
