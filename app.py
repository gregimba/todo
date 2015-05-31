from flask import *
from peewee import *
from model import Item
app = Flask(__name__)

@app.route("/")
def index():
    return render_template('app.html',model=Item)

@app.route("/new",methods=['GET',"POST"])
def new():
    if request.method == "POST":
        Item.create(name=request.form['name'],description=request.form['description'])
        return redirect(url_for('index'))
    else:
        return render_template('new.html')

if __name__ == '__main__':
    app.run(debug=True)