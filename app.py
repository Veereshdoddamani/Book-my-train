'''import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import bcrypt
from datetime import datetime

app = Flask(__name__)

# Configuration for uploads
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Secret key for session management
app.secret_key = 'your_secret_key_here'

# SQLAlchemy configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://Veeresh:Veeresh123@localhost/train"  # Replace with your database credentials
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Ensure upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Database Models
class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    fullname = db.Column(db.String(100), nullable=False)
    password = db.Column(db.LargeBinary, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Login(db.Model):
    __tablename__ = 'Login'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    login_time = db.Column(db.DateTime, default=datetime.utcnow)
    success = db.Column(db.Boolean, nullable=False)

# Initialize the database
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def home():
    """
    Renders the landing page with a transition animation.
    """
    return render_template('index.html')

@app.route('/index2')
def index2():
    """
    Renders the login page.
    """
    return render_template('index2.html')

@app.route('/signup_page')
def signup_page():
    """
    Renders the signup page.
    """
    return render_template('signup.html')

@app.route('/register', methods=['POST'])
def register():
    """
    Handles user registration and redirects to login page.
    """
    username = request.form['username']
    fullname = request.form['fullname']
    password = request.form['password']
    confirm_password = request.form['confirm-password']
    email = request.form['email']
    phone = request.form['mobile']

    # Check if passwords match
    if password != confirm_password:
        return jsonify({"message": "Passwords do not match."}), 400

    # Check if email or phone already exists
    if User.query.filter_by(email=email).first():
        return jsonify({"message": "Email already registered."}), 400
    if User.query.filter_by(phone=phone).first():
        return jsonify({"message": "Phone number already registered."}), 400

    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    # Save the user to the database
    user = User(username=username, fullname=fullname, password=hashed_password, email=email, phone=phone)
    db.session.add(user)
    db.session.commit()

    # Redirect to login page after successful registration
    return redirect(url_for('index2'))  # Redirect to login page

# Main entry point
if __name__ == "__main__":
    app.run(debug=True)
'''
import os
from flask import Flask, render_template, request, redirect, url_for, jsonify
from flask_sqlalchemy import SQLAlchemy
import bcrypt
from datetime import datetime

app = Flask(__name__)

# Configuration for uploads
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

# Secret key for session management
app.secret_key = 'your_secret_key_here'

# SQLAlchemy configuration
app.config["SQLALCHEMY_DATABASE_URI"] = "mysql+pymysql://Veeresh:Veeresh123@localhost/train"  # Replace with your database credentials
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db = SQLAlchemy(app)

# Ensure upload directory exists
if not os.path.exists(UPLOAD_FOLDER):
    os.makedirs(UPLOAD_FOLDER)

# Database Models
class User(db.Model):
    __tablename__ = 'User'
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    fullname = db.Column(db.String(100), nullable=False)
    password = db.Column(db.LargeBinary, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    phone = db.Column(db.String(15), unique=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

class Login(db.Model):
    __tablename__ = 'Login'
    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('User.id'), nullable=False)
    login_time = db.Column(db.DateTime, default=datetime.utcnow)
    success = db.Column(db.Boolean, nullable=False)

# Initialize the database
with app.app_context():
    db.create_all()

# Routes
@app.route('/')
def home():
    """
    Renders the landing page with a transition animation.
    """
    return render_template('index.html')

@app.route('/index2')
def index2():
    """
    Renders the login page.
    """
    return render_template('index2.html')

@app.route('/signup_page')
def signup_page():
    """
    Renders the signup page.
    """
    return render_template('signup.html')

@app.route('/register', methods=['POST'])
def register():
    """
    Handles user registration and redirects to login page.
    """
    username = request.form['username']
    fullname = request.form['fullname']
    password = request.form['password']
    confirm_password = request.form['confirm-password']
    email = request.form['email']
    phone = request.form['mobile']

    # Check if passwords match
    if password != confirm_password:
        return jsonify({"message": "Passwords do not match."}), 400

    # Check if email or phone already exists
    if User.query.filter_by(email=email).first():
        return jsonify({"message": "Email already registered."}), 400
    if User.query.filter_by(phone=phone).first():
        return jsonify({"message": "Phone number already registered."}), 400

    # Hash the password
    hashed_password = bcrypt.hashpw(password.encode("utf-8"), bcrypt.gensalt())

    # Save the user to the database
    user = User(username=username, fullname=fullname, password=hashed_password, email=email, phone=phone)
    db.session.add(user)
    db.session.commit()

    # Redirect to login page after successful registration
    return redirect(url_for('index2'))

@app.route('/login', methods=['POST'])
def login():
    """
    Handles user login and redirects to search page upon success.
    """
    email_or_number = request.json.get('email_or_number')
    password = request.json.get('password')

    # Validate input
    if not email_or_number or not password:
        return jsonify({"message": "Both fields are required."}), 400

    # Check if the input is email or phone number
    user = None
    if "@" in email_or_number:
        user = User.query.filter_by(email=email_or_number).first()
    elif email_or_number.isdigit():
        user = User.query.filter_by(phone=email_or_number).first()

    # Validate user and password
    if user and bcrypt.checkpw(password.encode("utf-8"), user.password):
        return jsonify({"message": "Login successful.", "redirect": "/search"}), 200

    return jsonify({"message": "Invalid credentials."}), 401

@app.route('/search')
def search_page():
    """
    Renders the search page for finding train routes.
    """
    return render_template('search.html')

@app.route('/search_results', methods=['POST'])
def search_results():
    """
    Handles search form submissions and redirects to the appropriate train page
    based on the 'from_station' and 'to_station' inputs.
    """
    from_station = request.form.get('from_station')
    to_station = request.form.get('to_station')

    # Map routes to train pages (example logic)
    train_routes = {
        ('KSR-BENGALURU', 'HPT-HOSPETE'): 'train1.html',
        ('KSR-BENGALURU', 'HVR-HAVERI'): 'train2.html',
        ('KSR-BENGALURU', 'MYS-MYSURU'): 'train3.html',
        ('KSR-BENGALURU', 'DVG-DAVANGERE'): 'train4.html',
        ('KSR-BENGALURU', 'MAJN-MANGALURU'): 'train5.html',
        ('HPT-HOSPETE', 'KSR-BENGALURU'): 'train6.html',
        ('MYS-MYSURU', 'KSR-BENGALURU'): 'train7.html',
        ('HVR-HAVERI', 'KSR-BENGALURU'): 'train8.html',
        ('DVG-DAVANGERE', 'KSR-BENGALURU'): 'train9.html',
        ('MAJN-MANGALURU', 'KSR-BENGALURU'): 'train10.html',

        # Add more routes as needed
    }

    # Find the corresponding page
    route = (from_station, to_station)
    train_page = train_routes.get(route)

    if train_page:
        return redirect(url_for('show_train_page', page=train_page))
    else:
        return jsonify({"message": "No trains found for the selected route."}), 404

@app.route('/train/<page>')
def show_train_page(page):
    """
    Dynamically renders the train page based on the given page name.
    """
    return render_template(page)

# Main entry point
if __name__ == "__main__":
    app.run(debug=True)
