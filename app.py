import joblib
import numpy as np

model_filename = 'exmodel.joblib'

try:
    loaded_model = joblib.load(model_filename)
    print("Modellen laddad")
except FileNotFoundError:
    print("Error")
    
    
# new_flower = np.array([[5.6, 3.4, 1.8, 0.3], [2.1, 0.5, 1.8, 1.3], [0.6, 5.4, 3.8, 1.3]])


# new = np.array([[-2.275374, 3.278471, 1.816370, -0.268242, 0.582721, 1.988050, 0.138743, -0.489081],[-2.275374, 3.278471, 2.816370, -0.268242, 0.582721, 2.988050, 0.138743, -0.489081]])
new = np.array([[11.420,20.38, 77.58,386.1,0.14250, 0.28390,0.241400, 0.105200, 0.2597, 0.09744, 0.4956,1.1560,3.4450,27.230,0.009110,0.074580,0.056610,0.018670,0.059630,0.009208,14.910,26.50,98.87,567.7,0.20980,0.86630,0.686900,0.257500,0.6638,0.17300],
[9.504,12.44,60.34,273.9,0.10240,0.06492,0.029560,0.020760,0.1815,0.06905,0.2773,0.9768,1.9090,15.700,0.009606,0.014320,0.019850,0.014210,0.020270,0.002968,10.230,15.66,65.13,314.9,0.13240,0.11480,0.088670,0.062270,0.2450,0.07773]])
predict = loaded_model.predict(new)
predictions = loaded_model.predict(new)
probs = loaded_model.predict_proba(new)

for i, (pred, prob) in enumerate(zip(predictions, probs)):
    print(f"Sample {i+1}: Prediction={pred}, Probs={prob.round(3)}")

print(predict[0])

print(predict[1])