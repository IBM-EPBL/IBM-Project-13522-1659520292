#Done by Rakesh Kumar M , Srimukund K G G , Kailash A L , Hariharan M

#Team ID : PNT2022TMID04164

from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
@app.route("/home")

def home():
	return render_template("index.html")

if __name__ =='__main__':
	app.run(debug=True , port=5000)
