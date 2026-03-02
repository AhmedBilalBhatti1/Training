import numpy as np

def sigmoid(z):
    return 1 / (1 + np.exp(-z))

def sigmoid_derivative(a):
    return a * (1 - a)

def binary_cross_entropy(y_true, y_pred):
    epsilon = 1e-8
    return -np.mean(y_true * np.log(y_pred + epsilon) + (1 - y_true) * np.log(1 - y_pred + epsilon))

def forward(X, W1, b1, W2, b2):
    Z1 = X @ W1 + b1
    A1 = sigmoid(Z1)

    Z2 = A1 @ W2 + b2
    A2 = sigmoid(Z2)

    return A2, (A1, A2)

def backward(X, y, cache, W1, W2):
    A1, A2 = cache
    m = X.shape[0]
    dA2 = A2 - y
    dW2 = A1.T @ (dA2 * sigmoid_derivative(A2)) / m
    db2 = np.sum(dA2 * sigmoid_derivative(A2), axis=0, keepdims=True) / m
    dA1 = (dA2 * sigmoid_derivative(A2)) @ W2.T
    dW1 = X.T @ (dA1 * sigmoid_derivative(A1)) / m
    db1 = np.sum(dA1 * sigmoid_derivative(A1), axis=0, keepdims=True) / m

    return dW1, db1, dW2, db2

def train(X, y):
    np.random.seed(42)
    W1 = np.random.randn(2, 8) * np.sqrt(2/2)
    b1 = np.zeros((1, 8))
    W2 = np.random.randn(8, 1) * np.sqrt(2/8)
    b2 = np.zeros((1, 1))

    lr     = 1e-0
    epochs = 20000

    for epoch in range(epochs):
        A2, cache = forward(X, W1, b1, W2, b2)
        loss = binary_cross_entropy(y, A2)

        dW1, db1, dW2, db2 = backward(X, y, cache, W1, W2)
        W1 -= lr * dW1
        b1 -= lr * db1
        W2 -= lr * dW2
        b2 -= lr * db2

        if epoch % 5000 == 0:
            preds = (A2 > 0.5).astype(int)
            acc   = np.mean(preds == y) * 100
            print(f"Epoch {epoch:5d} | Loss: {loss:.4f} | Acc: {acc:.0f}%")

    return W1, b1, W2, b2

X = np.array([[0,0],[0,1],[1,0],[1,1],[0,0],[0,1],[1,0],[1,1],[0,0],[0,1],[1,0],[1,1]])
y = np.array([[0],[1],[1],[0],[0],[1],[1],[0],[0],[1],[1],[0]])

W1, b1, W2, b2 = train(X, y)
A2, _ = forward(X, W1, b1, W2, b2)
preds = (A2 > 0.5).astype(int)

print("\nFinal Results:")
print("Input  | Expected | Predicted | Confidence")
for i in range(len(X)):
    print(f"{X[i]}  |    {y[i][0]}     |     {preds[i][0]}     |  {A2[i][0]:.4f}")