import json
from flask import Flask, render_template, request, redirect, url_for, session, flash
import hashlib
import os

app = Flask(__name__)
app.secret_key = '1a2b3c4d5a'  

USERS_FILE = 'users.json'
PRODUCTS_FILE = 'products.json'

def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

def load_users():
    if os.path.exists(USERS_FILE):
        with open(USERS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_users(users):
    with open(USERS_FILE, 'w') as f:
        json.dump(users, f)

def load_products():
    if os.path.exists(PRODUCTS_FILE):
        with open(PRODUCTS_FILE, 'r') as f:
            return json.load(f)
    return []

def save_products(products):
    with open(PRODUCTS_FILE, 'w') as f:
        json.dump(products, f)


@app.route('/')
def home():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    products = load_products()
    return render_template('index.html', products=products)


@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hash_password(password)

        users = load_users()

        for user in users:
            if user['username'] == username:
                flash('Username already taken!', 'danger')
                return redirect(url_for('register'))

        user_id = len(users) + 1
        users.append({'id': user_id, 'username': username, 'password': hashed_password})

        save_users(users)
        flash('Registration successful! Please log in.', 'success')
        return redirect(url_for('login'))

    return render_template('register.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if 'user_id' in session:
        return redirect(url_for('home'))

    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        hashed_password = hash_password(password)

        users = load_users()

        for user in users:
            if user['username'] == username and user['password'] == hashed_password:
                session['user_id'] = user['id']
                flash('Login successful!', 'success')
                return redirect(url_for('home'))

        flash('Invalid credentials! Please try again.', 'danger')
        return redirect(url_for('login'))

    return render_template('login.html')

@app.route('/logout')
def logout():
    session.pop('user_id', None) 
    flash('You have logged out successfully.', 'info')
    return render_template('logout.html')  

@app.route('/add_product', methods=['GET', 'POST'])
def add_product():
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    if request.method == 'POST':
        name = request.form['name']
        price = request.form['price']
        product_id = len(load_products()) + 1

        products = load_products()
        products.append({'id': product_id, 'name': name, 'price': price})

        save_products(products)
        flash('Product added successfully!', 'success')
        return redirect('/')
    
    return render_template('add_product.html')

@app.route('/delete_product/<int:product_id>', methods=['POST'])
def delete_product(product_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    products = load_products()
    product = next((p for p in products if p['id'] == product_id), None)
    if product:
        products.remove(product)
        save_products(products)
        flash('Product deleted successfully!', 'success')
    else:
        flash('Product not found!', 'danger')
    return redirect('/')

@app.route('/update_product/<int:product_id>', methods=['GET', 'POST'])
def update_product(product_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    products = load_products()
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        flash('Product not found!', 'danger')
        return redirect('/')

    if request.method == 'POST':
        product['name'] = request.form['name']
        product['price'] = request.form['price']
        save_products(products)
        flash('Product updated successfully!', 'success')
        return redirect('/')
    
    return render_template('update_product.html', product=product)

@app.route('/product/<int:product_id>', methods=['PUT'])
def update_product_put(product_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    products = load_products()
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return "Product not found!", 404

    data = request.get_json()
    product['name'] = data.get('name', product['name'])
    product['price'] = data.get('price', product['price'])
    save_products(products)

    return json.dumps({'message': 'Product updated successfully!'}), 200

@app.route('/product/<int:product_id>', methods=['PATCH'])
def update_product_patch(product_id):
    if 'user_id' not in session:
        return redirect(url_for('login'))
    
    products = load_products()
    product = next((p for p in products if p['id'] == product_id), None)
    if not product:
        return "Product not found!", 404

    data = request.get_json()
    if 'name' in data:
        product['name'] = data['name']
    if 'price' in data:
        product['price'] = data['price']
    save_products(products)

    return json.dumps({'message': 'Product partially updated successfully!'}), 200

if __name__ == '__main__':
    app.run(debug=True)
