from urls import *
from models import *

db.init_app(app)

with app.app_context():
    db.create_all()
    
if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=6011)