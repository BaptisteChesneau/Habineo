from flask import Flask, render_template, request, redirect, url_for, session, flash
from functools import wraps

app = Flask(__name__)
app.secret_key = "change-me-in-prod"  # nécessaire pour la session

# =========================================================
# Helpers
# =========================================================
def login_required(view):
    @wraps(view)
    def wrapped(*args, **kwargs):
        if not session.get("user_id"):
            flash("Veuillez vous connecter pour accéder à cette page.")
            return redirect(url_for("login", next=request.path))
        return view(*args, **kwargs)
    return wrapped

# =========================================================
# 🌐 MAIN ROUTES — HABINÉO WEBSITE
# =========================================================
@app.route("/")
def home():
    return render_template("home.html")

@app.route("/sales")
def sales():
    return render_template("sales.html")

@app.route("/rentals")
def rentals():
    return render_template("rentals.html")

@app.route("/estimate")
def estimate():
    return render_template("estimate.html")

@app.route("/agency")
def agency():
    return render_template("agency.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

# =========================================================
# 👤 Auth (signup / login / logout)
# =========================================================
@app.route("/signup", methods=["GET","POST"])
def signup():
    if request.method == "POST":
        session["user_id"] = request.form.get("email") or "demo@habineo.fr"
        session["user_name"] = request.form.get("name") or "Client Habinéo"
        return redirect(url_for("dashboard"))
    return render_template("signup.html")

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form.get("email") or "demo@habineo.fr"
        session["user_id"] = email
        session["user_name"] = "Client Habinéo"
        return redirect(request.args.get("next") or url_for("dashboard"))
    return render_template("login.html")

@app.route("/logout")
def logout():
    session.clear()
    flash("Vous êtes déconnecté.")
    return redirect(url_for("home"))

# =========================================================
# 🧑‍💻 Espace client (protégé)
# =========================================================
@app.route("/dashboard")
@login_required
def dashboard():
    user = {"email": session.get("user_id"), "name": session.get("user_name", "Client")}
    stats = {"favoris": 5, "visites": 2, "messages": 3}
    return render_template("dashboard.html", user=user, stats=stats)

@app.route("/account/profile", methods=["GET", "POST"])
@login_required
def account_profile():
    if request.method == "POST":
        session["user_name"] = request.form.get("name") or session.get("user_name", "Client")
        flash("Profil mis à jour.")
        return redirect(url_for("account_profile"))
    user = {
        "email": session.get("user_id"),
        "name": session.get("user_name", "Client"),
        "phone": "06 12 34 56 78",
    }
    return render_template("account_profile.html", user=user)

@app.route("/account/favorites")
@login_required
def account_favorites():
    favorites = [
        {"title": "Appartement — Issy", "price": "510 000 €"},
        {"title": "Loft — Saint-Ouen", "price": "1 020 000 €"},
    ]
    return render_template("account_favorites.html", favorites=favorites)

@app.route("/account/messages", methods=["GET", "POST"])
@login_required
def account_messages():
    if request.method == "POST":
        flash("Message envoyé à l’agence.")
        return redirect(url_for("account_messages"))
    threads = [
        {"subject": "Demande de visite — Paris 15e", "last": "Hier", "unread": True},
        {"subject": "Documents estimation", "last": "Lun.", "unread": False},
    ]
    return render_template("account_messages.html", threads=threads)

@app.route("/account/settings", methods=["GET", "POST"])
@login_required
def account_settings():
    if request.method == "POST":
        flash("Préférences enregistrées.")
        return redirect(url_for("account_settings"))
    return render_template("account_settings.html")

# =========================================================
# 🧪 Optional: Hello (dev)
# =========================================================
@app.route("/hello")
def hello():
    return render_template("hello.html")

# =========================================================
# ⚙️ RUN FLASK SERVER
# =========================================================
if __name__ == "__main__":
    app.run(debug=True)
