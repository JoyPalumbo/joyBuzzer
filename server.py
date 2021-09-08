
from flask import Flask, render_template
app = Flask(__name__)

@app.route('/')
def home():
   return render_template('index.html')

@app.route('/', methods=['POST'])
def test():
        # POST request
    print('you clicked')
    return render_template('index.html');


if __name__ == '__main__':
   app.run()