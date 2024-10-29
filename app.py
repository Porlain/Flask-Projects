from flask import Flask
app = Flask(__name__)

# Create a mapping between routing and view functions
@app.route('/')
def hello_world():  # put application's code here
    return 'Hello World!'

if __name__ == '__main__':
    app.run()
