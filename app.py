from flask import Flask,flash,redirect, url_for
from flask import render_template
from config import Config
from db import db
from usuarios import models
from wtforms.validators import ValidationError  # Importar para usar a validação personalizada
from usuarios.forms import RegistrationForm
from email_validator import validate_email, EmailNotValidError  # Importar para validação de e-mail



app = Flask(__name__)

app.config.from_object(Config)
@app.route('/', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        new_user = models.Users(
            nome=form.name.data,
            email=form.email.data,
            senha=form.password.data
        )
        new_user.save()
        flash(f'Account created for {form.name.data}!', 'success')
        return redirect(url_for('login'))  # Redireciona para a página de login
    return render_template('register.html', form=form)

@app.route('/login')
def login():
    return render_template('login.html')
    
db.init_app(app)

with app.app_context():
    print("Creating database tables...")
    db.create_all()
    print("Tables created.")

if __name__ == '__main__':
    app.run(debug=True)
