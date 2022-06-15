from flask import Flask, request, render_template
import pickle

app = Flask(__name__)
model = pickle.load(open("model.pkl","rb"))

@app.route("/")
def Home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():
    form_data=request.form['Years_of_Experience']
    print(form_data)
    feature = [[form_data]]
    prediction = model.predict(feature)
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)