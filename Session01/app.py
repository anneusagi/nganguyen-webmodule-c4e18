from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def index():
    posts = [
        {
            "title": " Mát Trời ",
            "content": "Hôm nay thời tiết mát zời, chỉ muốn ngủ thôi ối giời ơi",
            "author": "LT",
            'gender':1
        },
        {
            "title": " abc ",
            "content": "abc",
            "author": "NN",
            "gender":0
        },
        {
            "title": " def ",
            "content": "defghi",
            "author": "NN",
            "gender":0

        }
    ]


    return render_template("index.html", posts=posts) 
    #nên đặt trùng tên. 

@app.route('/hello')
def say_hello():
    return "Hello C4E 18"

@app.route('/sayhi/<name>/<age>')
def say_hi(name,age):
    return "Hi {0}, you're {1} years old".format(name, age)

@app.route('/sum/<int:x>/<int:y>')
def sum(x,y):
    return str(x+y)   
    # ( chuyển sang string )


if __name__ == '__main__':
  app.run(debug=True)
 