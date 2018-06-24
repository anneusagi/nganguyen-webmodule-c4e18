from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
#vào trang chủ
def index():
    return "Hello world"
#chạy hàm index bên trên

if __name__ == '__main__':  
    #( file được chạy trực tiếp thì nó sẽ run app) pythonapp.py , 
  app.run(debug=True)

