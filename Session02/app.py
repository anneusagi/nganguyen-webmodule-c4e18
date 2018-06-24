from flask import Flask, render_template
import mlab
from models.service import Service


app = Flask(__name__)

#0. Create connection
mlab.connect()

# new_service = Service(
# name="Đạt 100",
# dob=1996,
# gender=1,
# height=174,
# phone="018272414251",
# address="Trần Duy Hưng",
# status=False
# )
# new_service.save()

@app.route('/')
def index():
  return render_template('index.html')

@app.route('/search/<gender>')
def search(gender):
  all_service = Service.objects(gender=gender, dob__lte=1998, address__exact="Hà Nội")
  return render_template('search.html', all_service=all_service)

if __name__ == '__main__':
  app.run(debug=True)
 