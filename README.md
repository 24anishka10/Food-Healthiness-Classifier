# Food Healthiness Classifier  
## Quick Start  
### 1. Environment Setup  
Since this project uses only core Python syntax, no virtual environment or dependency installation is required.  
- Ensure you have **Python 3.x** installed.  
* Verify by running: python --version  
### 2. Training the Model  
Before making predictions, you must train the model to "learn" the weights for each nutrient.  
- &nbsp; py classify_food.py train  

This will generate a weights.txt file in your directory containing the learned parameters.  
### 3. Running a Prediction  
Use the --predict flag followed by the nutritional values for 100g of food.  

**Format:** py classify_food.py predict [Calories] [Fat] [Sugar] [Sodium] [Protein]  

**Example (Apple):**  
&nbsp;&nbsp; py classify_food.py predict 52 0.2 10 1 0.3  
**Example (Fried Snack):**  
&nbsp;&nbsp; py classify_food.py predict 300 20 15 600 2  
## How it Works  
The classifier uses the **Perceptron Learning Rule**. It treats the nutritional values as a feature vector (x) and calculates a weighted sum (z):  
&nbsp;&nbsp;&nbsp; z=(w1*cal)+(w2*fat)+(w3*sugar)+(w4*sod)+(w5*prot)+b  
- If z>=0 , the food is classified as **Healthy (1)**.  
* If z<0 , it is classified as **Unhealthy (0)**.  

During training, the model adjusts the weights (w) and bias (b) whenever it makes a mistake, slowly aligning its logic with the provided training data.  
## Repository Structure  
- classify_food.py: The main source code containing the ML logic and CLI.  
* weights.txt: Created after training; stores the AI's "memory."  
+ README.md: Project documentation and setup guide.  
## Troubleshooting  
- **Error: "No trained model found":** Ensure you run the train command first to create the weights.txt file.  
* **Input Format:** Ensure all 5 nutritional values are provided as numbers (integers or floats).


### Designed and developed by : Anishka Narang | 25BAI10513
