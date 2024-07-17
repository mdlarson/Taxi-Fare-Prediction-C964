'''TODO: Write better docstring'''
from flask import Flask, request, render_template
import joblib
import pandas as pd


app = Flask(__name__)

# Load the Model
model = joblib.load('model.pkl')


# Home and Summary Pages
@app.route('/')
def index():
    return render_template('index.html')


@app.route('/summary')
def summary():
    # Generate summary statistics and visualizations
    return render_template('summary.html')


# Fare Prediction
@app.route('/predict', methods=['POST'])
def predict():
    pickup_time = request.form['pickup_time']
    pickup_location = request.form['pickup_location']

    input_data = pd.DataFrame([[pickup_time, pickup_location]],
                              columns=['columne_name', 'columne_name2'])

    prediction = model.predict(input_data)[0]

    return render_template('result.html', prediction=prediction)


if __name__ == '__main__':
    app.run(debug=True)
