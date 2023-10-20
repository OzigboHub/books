from app import app, db
from routes import *


if __name__ == "__main__":
    app.app_context().push()
    db.create_all()
    app.run(debug=True)