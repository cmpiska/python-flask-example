from flask import Flask
import os

app = Flask(__name__)

@app.route("/")
def hello_world():
    return "ola mundo"

@app.route("/health")
def health():
    #return str(os.environ.get("STATUS"))
    return "OK"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=os.environ.get("APP_PORT"), debug=True)
    

     #app.run(host="0.0.0.0", port=3000) 
