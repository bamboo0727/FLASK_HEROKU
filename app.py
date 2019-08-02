from flask import Flask
app = Flask(__name__) #__name__ is the module will be executed

@app.route("/")  #function decorator
def home():
    return "Hello Flask"

@app.route("/test")
def test():
    return "this is Test"

if __name__=="__main__":
    app.run() #start server