from flask import Flask
app = Flask(__name__) #__name__ is the module will be executed

@app.route("/")  #function decorator
def home():
    return "企鹅教育-Elise"

@app.route("/piano")
def piano():
    return "this is Piano"

if __name__=="__main__":
    app.run() #start server