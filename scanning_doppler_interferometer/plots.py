from matplotlib.pyplot import figure

def plotwinds(dat):

    ax = figure().gca()
    ax.plot(dat['Begin Time'],dat.iloc[:,2:])
    ax.set_title(dat.filename.name)
    ax.set_ylabel('Wind Speed [m/s]')
    ax.set_xlabel('Time [UTC]]')
    ax.legend(dat.columns[2:].astype(str),loc='best')
    ax.grid(True)