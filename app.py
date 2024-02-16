from flask import Flask, request, render_template, jsonify
import pickle

app = Flask(__name__)

with open('model.pkl', 'rb') as model_file:
    model = pickle.load(model_file)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if request.method == 'POST':
        data = request.json
        text = data['text']
        prediction = model.predict([text])[0]
        probability = model.predict_proba([text]).max() * 100
        return jsonify(prediction=prediction, probability=probability)

if __name__ == '__main__':
    app.run(debug=True)
