from flask import Flask, redirect, request, url_for, make_response, render_template_string,render_template
import uuid, json, numbers

app = Flask(__name__) 

# mock cookies
def validate_cookie(cookie):
    return cookie=="123"

# mock auth
def try_get_cookie(login, password):
    return "123" if(login=="ivan" and password=="2281337") else None

@app.route('/', methods=['GET', 'POST'])
def login():
    cookie = request.cookies.get('auth')
    if cookie and validate_cookie(cookie):
        return render_template("index.html")
    
    if request.method == 'POST':
        login = request.form.get('login')
        password = request.form.get('password')
        new_cookie = try_get_cookie(login, password)
        
        if new_cookie:
            resp = make_response(render_template("index.html"))
            resp.set_cookie('auth', new_cookie)
            return resp
        else:
            return "Login failed!", 401
    
    return render_template_string('''
        <form method="post">
            <input type="text" name="login" placeholder="Login" required>
            <input type="password" name="password" placeholder="Password" required>
            <button type="submit">Login</button>
        </form>
    ''')


if(__name__=="__main__"):
    app.run("0.0.0.0",4321)