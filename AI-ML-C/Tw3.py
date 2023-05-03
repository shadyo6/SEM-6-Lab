import numpy as np

def stepFun(v):
        if(v>0):
            return 1;
        else:
            return 0;

def perceptron(X,W,b):
    y=np.dot(X,W)+b
    v=stepFun(y)
    return v

def orGate(X):
        b=-0.5
        W = np.array([1,1])
        return perceptron(X,W,b)

def notGate(X):
        b=0.5
        W = -1;
        return perceptron(X,W,b)

def andGate(X):
        b=-1.5
        W = np.array([1,1])
        return perceptron(X,W,b)

def xorGate(X):
        Y1 = andGate([notGate(X[0]),X[1]])
        Y2 = andGate([X[0],notGate(X[1])])
        Y = orGate([Y1,Y2]);
        return Y;

def main():
        test1 = np.array([0,0])
        test2 = np.array([0,1])
        test3 = np.array([1,0])
        test4 = np.array([1,1])
	
        print("AND({},{})={}".format(0,0,andGate(test1)))
        print("AND({},{})={}".format(0,1,andGate(test2)))
        print("AND({},{})={}".format(1,0,andGate(test3)))
        print("AND({},{})={}".format(1,1,andGate(test4)))

        print("OR({},{})={}".format(0,0,orGate(test1)))
        print("OR({},{})={}".format(0,1,orGate(test2)))
        print("OR({},{})={}".format(1,0,orGate(test3)))
        print("OR({},{})={}".format(1,1,orGate(test4)))

        print("NOT({})={}".format(0,notGate(test1[0])))
        print("NOT({})={}".format(1,notGate(test2[1])))

        print("XOR({},{})={}".format(0,0,xorGate(test1)))
        print("XOR({},{})={}".format(0,1,xorGate(test2)))
        print("XOR({},{})={}".format(1,0,xorGate(test3)))
        print("XOR({},{})={}".format(1,1,xorGate(test4)))

if __name__ == "__main__":
        main()
