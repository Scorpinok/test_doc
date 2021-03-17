from flask import Flask, render_template, request
import pickle

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        flavanoids = request.form['flavanoids']
        od280 = request.form['od280']
        #total_phenols = request.form['total_phenols']
        #proline = request.form['proline']
        #hue = request.form['hue']

        #data = [[float(flavanoids), float(od280), float(total_phenols), float(proline), float(hue)]]
        data = [[float(flavanoids), float(od280)]]

        lr = pickle.load(open('ml_wine.pkl', 'rb'))
        prediction = lr.predict(data)[0]

        if prediction == 0:
            prediction = 'Class_0'
        if prediction == 1:
            prediction = 'Class_1'
        if prediction == 2:
            prediction = 'Class_2'

    return render_template('index.html', prediction=prediction)


if __name__ == '__main__':
    app.run(host='0.0.0.0')