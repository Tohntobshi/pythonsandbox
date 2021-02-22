from flask import Flask, request, make_response
from models import db, Item

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "postgres://postgres:secret@postgres/mydb"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

@app.route('/')
def hello():
    return { 'hello': 'motherfuckers' }

@app.route('/create_item', methods=['POST'])
def create_item():
    form = request.get_json()
    title = form['title']
    description = form['description']
    db.session.add(Item(title = title, description = description))
    db.session.commit()
    return { 'status': 'created' }

@app.route('/get_item/<int:item_id>')
def get_item(item_id):
    el = Item.query.get(item_id)
    if not(el): return make_response({ 'status': 'not found' }, 404)
    return { 'title': el.title, 'description': el.description }
    

@app.route('/get_items')
def get_items():
    result = map(lambda el: { 'id': el.id, 'title': el.title, 'description': el.description }, Item.query.all())
    return { 'result': list(result) } 
