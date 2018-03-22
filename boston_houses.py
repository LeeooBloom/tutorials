import numpy as np

data = np.loadtxt('boston_houses.csv', delimiter=',', skiprows=1)  # load data to work with

def main ():
    y = np.copy(data[:, 0])
    data[:, 0] = 1
    Xt = np.transpose(data)
    XtX = np.matrix.dot(Xt,data)
    XtXinv = np.linalg.inv(XtX)
    XtY = np.matrix.dot(Xt,y)
    beta = np.matrix.dot(XtXinv,XtY)
    to_print = " ".join(list(map(lambda b: str(b), beta)))
    print(to_print)



if __name__ == "__main__":
    main()
