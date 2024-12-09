import pickle
from flask import Flask, request, app, jsonify, url_for, render_template
import numpy
import pandas


app = Flask(__name__)
model = pickle.load(open("../model.pkl", 'rb'))

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/predict_api', methods=['POST'])

def predict_api():
    data = request.json['data']
    print(data)
    book_id = np.where(book_pivot.index == data)[0][0]
    distance, suggestion = model.kneighbors(book_pivot.iloc[book_id,:].values.reshape(1,-1), n_neighbors = 6)
    #books
    for i in range(len(suggestion)):
        books = book_pivot.index[suggestion[i]]
        for j in books:
            print(j)
        return jsonify(books)

if __name__ == "__main__":
    app.run(debug=True)

