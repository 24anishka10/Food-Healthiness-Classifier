# No 'import' statements allowed per your request

class FoodModel:
    def __init__(self):
        # Weights: [Calories, Fat, Sugar, Sodium, Protein] + Bias
        self.w = [0.0, 0.0, 0.0, 0.0, 0.0]
        self.b = 0.0
        self.lr = 0.01  # Learning rate

    def predict(self, x):
        # Activation = Sum(weight * feature) + bias
        activation = self.b
        for i in range(len(x)):
            activation += self.w[i] * x[i]
        return 1 if activation >= 0 else 0

    def train(self, data, labels, epochs=50):
        for _ in range(epochs):
            for i in range(len(data)):
                x = data[i]
                y_true = labels[i]
                y_pred = self.predict(x)
                
                # Perceptron Update Rule
                error = y_true - y_pred
                if error != 0:
                    for j in range(len(x)):
                        self.w[j] += self.lr * error * x[j]
                    self.b += self.lr * error

# --- Manual Data Handling ---
def get_data():
    # Features: [Cal, Fat, Sugar, Sod, Prot]
    X = [
        [50, 0.2, 1, 5, 1],    # Apple (Healthy)
        [550, 30, 10, 900, 25], # Burger (Unhealthy)
        [160, 2, 0, 70, 30],   # Chicken (Healthy)
        [400, 20, 40, 300, 4],  # Cake (Unhealthy)
        [30, 0.1, 0.5, 20, 2]   # Spinach (Healthy)
    ]
    y = [1, 0, 1, 0, 1]
    return X, y

def main():
    import sys # Used ONLY for CLI arguments as required by project brief
    model = FoodModel()
    
    # Simple CLI logic using sys.argv
    if len(sys.argv) < 2:
        print("Usage: python classify_food.py [train/predict] [features...]")
        return

    mode = sys.argv[1]

    if mode == "train":
        X, y = get_data()
        model.train(X, y)
        # Save weights to a plain text file
        with open("weights.txt", "w") as f:
            f.write(str(model.w) + "\n" + str(model.b))
        print("Model trained and weights saved to weights.txt.")

    elif mode == "predict":
        try:
            # Load weights from text file manually
            with open("weights.txt", "r") as f:
                lines = f.readlines()
                # Simple string parsing since we can't use 'json'
                w_str = lines[0].strip("[]\n").split(", ")
                model.w = [float(x) for x in w_str]
                model.b = float(lines[1])
            
            # Get user inputs from CLI
            user_features = [float(x) for x in sys.argv[2:]]
            result = model.predict(user_features)
            print("Result:", "HEALTHY" if result == 1 else "UNHEALTHY")
        except:
            print("Error: Train the model first or check your inputs.")

if __name__ == "__main__":
    main()