from flask import Flask, render_template, request
import pickle
import numpy as np

app = Flask(__name__)

# Load the trained model
model = pickle.load(open('model.pkl', 'rb'))

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    try:
        cgpa = float(request.form['cgpa'])
        iq = float(request.form['iq'])

        # Prepare input for model
        features = np.array([[cgpa, iq]])
        prediction = model.predict(features)

        result = "Placed" if prediction[0] == 1 else "Not Placed"
    except Exception as e:
        result = f"Error: {str(e)}"

    return render_template('index.html', prediction_text=f'Prediction: {result}')

if __name__ == '__main__':
    app.run(debug=True)