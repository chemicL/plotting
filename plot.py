#!/usr/bin/env python

import csv
import sys
import matplotlib.pyplot as plt
import dateutil.parser as dateparser
import numpy as np

from matplotlib.backends.backend_pdf import PdfPages

PDF_FILENAME = 'plots.pdf'
YLABEL = 'Amount'

def getDatesAndAmounts(filename):
    dates = []
    amounts = []

    with open(filename, 'rb') as tsvin:
        tsvin = csv.reader(tsvin, delimiter='\t')
        for row in tsvin:
            dates.append(dateparser.parse(row[0]))
            amounts.append(int(row[1]))

    # return dates array and a numpy array of amounts
    return (dates, np.array(amounts))
    
def plotTsv(filename):
    dates, amounts = getDatesAndAmounts(filename)

    figure, axes = plt.subplots()

    axes.set_title(filename)
    axes.set_ylabel(YLABEL)
    
    axes.plot(dates, amounts, 'r-')

    axes.fill_between(dates, 0, amounts, facecolor='red', alpha=0.5)
    axes.grid(True)

    # rotate and align the tick labels so they look better
    figure.autofmt_xdate()
    return figure
    

def plotTsvs(filenames):
    pp = PdfPages(PDF_FILENAME)
    
    for filename in filenames:
        fig = plotTsv(filename)
        pp.savefig(fig)
        plt.close(fig)

    pp.close()

        
def main():
    plotTsvs(sys.argv[1:])
        

if __name__ == '__main__':
    sys.exit(main())
