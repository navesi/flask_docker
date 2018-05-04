from flask import Flask, render_template, jsonify, request
import random
import json

app = Flask(__name__)
app.config['SECRET_KEY'] = random.randint(1, 100)

@app.route('/')
def index():
     return render_template('index.html')

@app.route('/reply', methods=['POST'])
def reply():
    data = json.loads(request.data)
    answer = "Yes, it is %s!\n" % data["keyword"]
    result = {
      "Content-Type": "application/json",
      "Answer":{"Text": answer}
    }
    # return answer
    return jsonify(result)

@app.route('/sample')
def sample():
    return render_template('sample.html')

if __name__ == '__main__':
    app.run(host='0.0.0.0',port=5000,debug=True)
