import urllib
from urllib import request
import numpy as np

f = urllib.request.urlopen('https://stepic.org/media/attachments/lesson/16462/boston_houses.csv')  # open file from URL
data = np.loadtxt(f, delimiter=',', skiprows=1)  # load data to work with

def main ():
    count = data.shape[0]
    x1 = data[:,1]
    x2 = data[:,2]
    x3 = data[:,3]
    x4 = data[:,4]
    x5 = data[:,5]
    x6 = data[:,6]
    ones = np.ones(count)
    X = np.column_stack((ones,x1,x2,x3,x4,x5,x6))


if __name__ == "__main__":
    main()
