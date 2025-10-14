from flask import Flask, render_template

app = Flask(__name__)

# 🏠 Page d'accueil
@app.route('/')
def accueil():
    return render_template('accueil.html')

# 👋 Page Hello (test initial)
@app.route('/hello')
def hello():
    return render_template('hello.html')

# 🏡 Page Vente
@app.route('/vente')
def vente():
    return render_template('vente.html')

# 🔑 Page Location
@app.route('/location')
def location():
    return render_template('location.html')

# 📏 Page Estimation
@app.route('/estimation')
def estimation():
    return render_template('estimation.html')

# 🏢 Page Agence
@app.route('/agence')
def agence():
    return render_template('agence.html')

# 💬 Page Contact
@app.route('/contact')
def contact():
    return render_template('contact.html')

# 👤 Page Créer un compte
@app.route('/creer-compte')
def creer_compte():
    return render_template('creer_compte.html')

# 🔐 Page Connexion
@app.route('/connexion')
def connexion():
    return render_template('connexion.html')


# =========================================================
# 🔧 Exécution du serveur Flask
# =========================================================
if __name__ == '__main__':
    app.run(debug=True)
