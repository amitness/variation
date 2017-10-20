from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Homepage"

def main():
    app.run('0.0.0.0', 8000)

if __name__ == '__main__':
    main()
