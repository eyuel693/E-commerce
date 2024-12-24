# Eyuel Shop - Flask Web Application

Welcome to the **Eyuel Shop** web application! This is a simple e-commerce platform built with **Flask**, where users can register, log in, add and manage products, and have a smooth shopping experience.

## Features


- **User Registration**: New users can sign up using a username and password.
- **Login and Logout**: Users can log in and out securely.
- **Add Products**: Logged-in users can add new products to the store.
- **Update and Delete Products**: Users can modify product details or delete products.
- **Responsive Design**: The application is built with a clean and user-friendly design that adapts to various screen sizes.
---

## libraries Used

- **Python**: Flask framework for building the web application.
- **HTML/CSS**: Frontend for creating an interactive, user-friendly UI.
- **JSON**: Data is stored locally in JSON files for simplicity and ease of access.
- **Hashing**: Passwords are hashed using SHA-256 for basic security (Note: For production, a stronger hashing method is recommended).
---
## Installation

### Prerequisites

To run this project, you need Python 3.x installed on your machine. You also need to install the necessary dependencies.

### Step-by-Step Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/eyuel693/E-commerce.git
   cd eyuel-shop
2. **Set up a virtual environment (optional but recommended):**

    ```bash
    python3 -m venv venv
    source venv/bin/activate 



3. **File Structure**
```
product management 
│
├── app.py                # Main Flask application
├── requirements.txt      # Project dependencies
├── users.json            # Store user data (JSON format)
├── products.json         # Store product data (JSON format)
├── templates/            # HTML files for each page
│   ├── index.html        # Home page
│   ├── register.html     # Registration page
│   ├── login.html        # Login page
│   ├── add_product.html  # Add product page
│   ├── update_product.html # Update product page
│   ├── logout.html       # Logout confirmation page
│
├── static/               # CSS and other static files
│   └── styles.css        # Styles for the application
└── README.md             # Project documentation
```
**How It Works**
Routes
/: Home page, only accessible for logged-in users.
/register: Page for new users to sign up.
/login: Page for existing users to log in.
/logout: Logs the user out and redirects to the home page.
/add_product: Allows logged-in users to add new products.
/update_product/<product_id>: Allows logged-in users to update product details.
/delete_product/<product_id>: Allows logged-in users to delete products.
