from flask import *
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

@app.route('/admin')
def admin():
  all_service = Service.objects()
  return render_template("admin.html", all_service=all_service)
  
@app.route('/delete/<service_id>')
def delete(service_id):
  service_to_delete = Service.objects().with_id(service_id)
  if service_to_delete is None:
    return "Service not found"
  else:
    service_to_delete.delete()
    # return "Deleted"

    return redirect(url_for("admin"))  #redirect

@app.route('/new-service', methods=["GET", "POST"])
def create():
  if request.method == "GET":
    return render_template("new_service.html")
  elif request.method == "POST":

    form = request.form #mở box
    name = form["name"]
    dob = form["dob"]
    address = form["address"]

    # return "Posted"
    return name + dob + address
    new_service = Service(
      name=name,
      dob=dob,
      address=address
    )
    
    new_service.save()




if __name__ == '__main__':
  app.run(debug=True)
 


  