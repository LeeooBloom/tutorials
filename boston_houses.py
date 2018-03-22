import numpy as np

data = np.loadtxt('boston_houses.csv', delimiter=',', skiprows=1)  # load data to work with

def main ():
    count = data.shape[0]
    y =  data[:,0]
    x1 = data[:,1]
    x2 = data[:,2]
    x3 = data[:,3]
    x4 = data[:,4]
    x5 = data[:,5]
    x6 = data[:,6]
    ones = np.ones(count)
    X = np.column_stack((ones,x1,x2,x3,x4,x5,x6))
    Xt = np.transpose(X)
    XtX = np.matrix.dot(Xt,X)
    XtXinv = np.linalg.inv(XtX)
    XtY = np.matrix.dot(Xt,y)
    beta = np.matrix.dot(XtXinv,XtY)
    print beta



if __name__ == "__main__":
    main()
