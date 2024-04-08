from flask import Flask, redirect, render_template, request, url_for
from firebase_database import write_user_data, get_all_books, get_user_data;
from random import choice
from string import ascii_letters

app = Flask(__name__, template_folder="templates/")

# (Flask routes and logic for login/signup and book data handling omitted for brevity)

@app.route("/")
def home():
    return render_template('index.html')

@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == 'POST':
        ...#get_user_by_email()
    elif request.method == 'GET':
        print('I am getting a page!')
    return render_template('login.html')

@app.route('/signup', methods=["GET", "POST"])
def signup():
    if request.method == 'POST':
        
        email = request.form['email']
        password = request.form['password']
        user_id = ''.join([choice(ascii_letters) for _ in range(8)]) # Generates random userId (:
        display_image = 'https://upload.wikimedia.org/wikipedia/commons/2/2c/Default_pfp.svg' # Currently default picture beacuse I am lazy.
        
        print("Got values", 'username', email, password, user_id)
        try:
            write_user_data('user_name=username', image_url=display_image, user_password=password, mail=email, user_id=user_id)
            return render_template("index.html"), 
        
        except Exception as e:
            print(f"GOT LIGMAED: {e}")
            return render_template("signup.html")

    return render_template('signup.html')
            
@app.route("/view_books")
def view_books():
  all_books = get_all_books()
  
  return render_template('view_books.html', books=all_books)

if __name__ == '__main__':
    app.run(debug=True)



