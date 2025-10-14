from flask import Flask, render_template

app = Flask(__name__)

# Page d'accueil par défaut
@app.route('/')
def accueil():
    return render_template('accueil.html')

# Page Hello (optionnelle)
@app.route('/hello')
def hello():
    return render_template('hello.html')

if __name__ == '__main__':
    app.run(debug=True)
