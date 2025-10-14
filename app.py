from flask import Flask, render_template

app = Flask(__name__)

# =========================================================
# 🌐 MAIN ROUTES — HABINÉO WEBSITE
# =========================================================

# 🏠 Home
@app.route('/')
def home():
    return render_template('home.html')

# 🏡 Sales page
@app.route('/sales')
def sales():
    return render_template('sales.html')

# 🏘️ Rentals page
@app.route('/rentals')
def rentals():
    return render_template('rentals.html')

# 📏 Estimate page
@app.route('/estimate')
def estimate():
    return render_template('estimate.html')

# 🏢 Agency page
@app.route('/agency')
def agency():
    return render_template('agency.html')

# 💬 Contact page
@app.route('/contact')
def contact():
    return render_template('contact.html')

# 👤 Signup page
@app.route('/signup')
def signup():
    return render_template('signup.html')

# 🔐 Login page
@app.route('/login')
def login():
    return render_template('login.html')

# =========================================================
# 🧪 Optional: Hello test page (for dev/test only)
# =========================================================
@app.route('/hello')
def hello():
    return render_template('hello.html')

# =========================================================
# ⚙️ RUN FLASK SERVER
# =========================================================
if __name__ == '__main__':
    app.run(debug=True)
