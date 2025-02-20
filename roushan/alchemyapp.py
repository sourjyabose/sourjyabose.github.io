from flask import Flask,redirect,request,render_template 
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"

db = SQLAlchemy(app)

class UserProfile(db.Model):
    uname = db.Column(db.String(20), primary_key=True)
    upass = db.Column(db.String(20), unique=True,nullable=False)
    utype = db.Column(db.String(20), unique=True,nullable=False)
    uremarks = db.Column(db.String(20), unique=True,nullable=False)
    
@app.route("/")
def createuserinfo():
    return render_template("userform.html")

@app.route("/saveuser",methods=['POST'])
def saveuser():
    uname = request.form.get('uname')
    upass = request.form.get('upass')
    utype = request.form.get('utype')
    uremarks = request.form.get('uremarks')
    up = UserProfile(uname = uname, upass = upass, utype = utype, uremarks = uremarks)
    db.session.add(up)
    db.session.commit()
    return redirect('/')

@app.route("/list")
def list_all_user():
    alluser=UserProfile.query.all()
    print(alluser)
    return render_template("showuser.html",alluser=alluser)
'''
@app.route("/....",method=['post'])
def upload1():
    f=request.files['files']
    upob=Upload(filename=f, data=f.read())
    db.session.add(upob)
    db.session.commit()
'''
if __name__=="__main__":
    app.run(debug=True)
    