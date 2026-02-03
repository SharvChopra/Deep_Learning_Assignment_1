## implementing perceptron from scratch

class Perceptron:
    def __init__(self,learning_rate=0.1,epochs=50):
        self.lr=learning_rate
        self.epochs=epochs
        self.w=[0.0,0.0]
        self.b=0.0

    ## using step function as activation function
    def activation_fn(self,x):
        if x>=0:
            return 1
        else:
            return 0
    
    ## Predict function to calculate output
    def predict(self,x):
        z = self.w[0]*x[0] + self.w[1]*x[1]+self.b
        a = self.activation_fn(z)

        return a
    
     ## built-in zip() function takes two iterables, X and y, and returns an iterator of tuples. Each tuple contains one element from X and one element from y

    def train(self,X,y):
        for i in range(self.epochs):
            error = 0

            for xi,yi in zip(X,y):
                y_pred = self.predict(xi)
                error += abs(yi - y_pred)

                ## weight and bias update
                self.w[0] += self.lr*(yi - y_pred)*xi[0]
                self.w[1] += self.lr*(yi - y_pred)*xi[1]
                self.b += self.lr*(yi - y_pred)


            if error == 0:
                print(f'Training complete after {i} epochs')
                return True
            
        print('Did not converge')
        return False


X = [
    [0,0],
    [0,1],
    [1,0],
    [1,1]
]

# y = [0,0,0,1] ## AND Gate Output
# y = [0,1,1,1] ## OR Gate Output
# y = [1,1,1,0] ## NAND Gate Output
# y = [1,0,0,0] ## NOR Gate Output
y = [0,1,1,0] ## XOR Gate Ouptut

P = Perceptron()
P.train(X,y)

print("Updated Weight and Bias:")
print("Weights:",P.w)
print("Bias:",P.b)

print("Predictions:")
for i in X:
    print(f"Input: {i}, Predicted Output: {P.predict(i)}")

