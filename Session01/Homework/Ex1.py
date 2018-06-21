from flask import Flask, render_temple, redirect
app = Flask(__name__)

@app.route('/about-me')
def aboutme(): 
    return "Nga Nguyen, Travelholic - Shopaholic - Catlover - Daydreamer - Edmlover "

@app.route('/school')
def school():
    return redirect("http://techkids.vn")