from flask import Flask,render_template,redirect,url_for,request
import searching
import os
app=Flask(__name__)
@app.route("/")
def home():
    return render_template('index.html')


@app.route("/search",methods=["POST","GET"])
def search():
    #if request.method=="POST":
    word=request.form["usr"]
    return redirect(url_for("list",keyword=word))
    #else:
    #return render_template('search.html', name = word)


#

#searching.find()



@app.route("/<keyword>")
def list(keyword):
    searching.find(keyword)
    return f"<h1>{keyword}</h1>"

    

if __name__=="__main__":
    app.run()