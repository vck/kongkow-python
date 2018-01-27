from flask import Flask, request, render_template
import namaclf
app = Flask(__name__)

def predict(nama):
  return namaclf.predict(nama)

@app.route('/', methods=["GET","POST"])
def index():
  if request.method == "POST":
    data = predict(request.form['nama'])
    return render_template("index.html", data=data, nama=request.form['nama'])
  else:
    return render_template("index.html")

