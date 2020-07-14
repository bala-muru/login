from flask import *
app=Flask(__name__)
@app.route("/")
def he():
    return render_template("login.html")
data={"bala":"123","arul":"123"}
@app.route("/details",methods=["POST","GET"])
def she():
        username=request.form["username"]
        password=request.form["password"]
        if username not in data:
            return render_template("login1.html",info="Invalid username")
        else:
            if data[username]!=password:
                return render_template("login1.html",info="Invalid password")
            else:
               return render_template("login1.html",name=username)
    
if __name__=='__main__':
    app.run()
