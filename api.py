from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        username = request.form.get('username')
        email = request.form.get('email')
        password = request.form.get('password')

        if not username or len(username) < 3:
            error = " not username or len(username) < 3"
            raise error
        elif not email or "@" not in email:
            error = " @ not in email"
        elif not password or len(password) > 6:
            error = "not password or len(password) < 6 "
            raise error
        else:
            return 

    return render_template('index.html', error=error)

if __name__ == '__main__':
    app.run(debug=True)