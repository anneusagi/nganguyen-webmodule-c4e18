from flask import Flask, render_template
app = Flask(__name__)


@app.route('/user/<username>')
def user(username):
    user = {

        "hera" : { "name": "Fullname Hera", "age": 18},
        "dinhquy": { "name": "Dinh Cong Quy", "age": 20}
    }


    return render_template('user.html', users=users, username=username)


if __name__ == '__main__':
  app.run(debug=True)
 