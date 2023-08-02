import numpy as np

def stepFun(v):
    if v > 0:
        return 1
    else:
        return 0

def perceptron(X, W, b):
    y = np.dot(X, W) + b
    v = stepFun(y)
    return v

def orGate(X):
    b = -0.5
    W = np.array([1, 1])
    return perceptron(X, W, b)

def notGate(X):
    b = 0.5
    W = np.array([-1])
    return perceptron(X, W, b)

def andGate(X):
    b = -1.5
    W = np.array([1, 1])
    return perceptron(X, W, b)

def train_perceptron(gate_name, X, y, W, b, learning_rate=0.1, epochs=30):
    for epoch in range(epochs):
        print("Training {} gate - Epoch {}: ".format(gate_name, epoch + 1), end="")
        for i in range(X.shape[0]):
            x_i = X[i]
            y_pred = perceptron(x_i, W, b)
            error = y[i] - y_pred
            W += (learning_rate * error * x_i).astype(int)
            b += int(learning_rate * error)
        print("W = {}, b = {}".format(W, b))

def main():
    test1 = np.array([0, 0])
    test2 = np.array([0, 1])
    test3 = np.array([1, 0])
    test4 = np.array([1, 1])

    # OR gate training
    X_or = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y_or = np.array([0, 1, 1, 1])
    W_or = np.array([1, 1])
    b_or = -0.2
    print("Training OR gate:")
    train_perceptron("OR", X_or, y_or, W_or, b_or, epochs=30)

    # AND gate training
    X_and = np.array([[0, 0], [0, 1], [1, 0], [1, 1]])
    y_and = np.array([0, 0, 0, 1])
    W_and = np.array([1, 1])
    b_and = -1.5
    print("\nTraining AND gate:")
    train_perceptron("AND", X_and, y_and, W_and, b_and, epochs=30)

    # NOT gate training
    X_not = np.array([[0], [1]])
    y_not = np.array([1, 0])
    W_not = np.array([-1])
    b_not = 0.5
    print("\nTraining NOT gate:")
    train_perceptron("NOT", X_not, y_not, W_not, b_not, epochs=30)

    print("\nAND({}, {}) = {}".format(0, 0, andGate(test1)))
    print("AND({}, {}) = {}".format(0, 1, andGate(test2)))
    print("AND({}, {}) = {}".format(1, 0, andGate(test3)))
    print("AND({}, {}) = {}".format(1, 1, andGate(test4)))

    print("OR({}, {}) = {}".format(0, 0, orGate(test1)))
    print("OR({}, {}) = {}".format(0, 1, orGate(test2)))
    print("OR({}, {}) = {}".format(1, 0, orGate(test3)))
    print("OR({}, {}) = {}".format(1, 1, orGate(test4)))

    print("NOT({}) = {}".format(0, notGate(test1[0])))
    print("NOT({}) = {}".format(1, notGate(test2[0])))

if __name__ == "__main__":
    main()
