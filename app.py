from flask import Flask, request, render_template
from test import print_internal_name

app = Flask(__name__)

@app.route('/', methods=['GET','POST'])
def index():
    return render_template('index.html')

if __name__ == '__main__':
    print_internal_name()
    app.run()
