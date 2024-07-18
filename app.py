'''TODO: Write better docstring'''
from flask import Flask, request, render_template
import joblib
import pandas as pd
from datetime import datetime


app = Flask(__name__)

# Load Model and Feature Names
model = joblib.load('model.pkl')
feature_names = joblib.load('feature_names.pkl')


# Home Page
@app.route('/', methods=['GET', 'POST'])
def index():
    prediction = None

    if request.method == 'POST':
        # Convert time string to integer hour of day
        time_str = request.form['hour_of_day']  # e.g. 15:32
        hour_of_day = datetime.strptime(time_str, '%H:%M').hour

        pickup_location = int(request.form['pickup_location'])

        # Create dataframe and initialize dummy columns
        input_data = pd.DataFrame({col: [0] for col in feature_names})
        input_data['hour_of_day'] = hour_of_day

        # Set relevant PULocationID to 1
        input_data[f'PULocationID_{pickup_location}'] = 1

        # Predict the fare
        prediction = model.predict(input_data)[0]

    return render_template('index.html', prediction=prediction)


# Summary Page
@app.route('/summary')
def summary():
    # Generate summary statistics and visualizations
    return render_template('summary.html')


if __name__ == '__main__':
    app.run(debug=True)
