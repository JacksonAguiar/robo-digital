from flask import Flask, render_template, request, url_for, redirect, jsonify
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy()
db.app = app
db.init_app(app)
app.app_context().push()

class Position(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    x = db.Column(db.String(15))
    y = db.Column(db.String(15))
    z = db.Column(db.String(15))

@app.route("/")
def index():
    pos = getLastPosition()
    return render_template("index.html", position = pos)

@app.route("/save", methods=['POST'])
def save():
    x = request.form['x']
    y = request.form['y']
    z = request.form['z']
    item = Position(x = x, y = y, z = z)
    db.session.add(item)
    db.session.commit()
    return redirect(url_for('index'))


def getLastPosition():
    result = Position.query.order_by(-Position.id).first()
    return result

@app.route("/last-position")
def sendToGodot():
    pos = getLastPosition()
    return jsonify(x=pos.x, y=pos.y,z=pos.z)

if __name__ == '__main__':
    db.create_all()
    app.run(debug=True)



