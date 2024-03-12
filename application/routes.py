from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def hello_world():
    return render_template('home.html')


@app.route("/gallery")
def page():
    return render_template('gallery.html')

@app.route("/about")
def about_us():
    return render_template('about_us.html')

@app.route("/contact")
def contact():
    return render_template('contact.html')