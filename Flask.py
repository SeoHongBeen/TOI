#Flask "Hello World" 웹 서버-> 키트 외에 필요 부품 x
from flask import Flask
app = Flask(__name__)

@app.route('/')
def home():
    return "Hello, Raspberry Pi Flask!"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
