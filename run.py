from app import create_app #import flask setup
from app.models import db 

app = create_app() #creates flask app

@app.route("/") 
def home():
    return "SlotFlow is running!"

@app.cli.command("init-db")
def init_db():
    """Create database tables."""
    with app.app_context():
        db.create_all()
    print("Database tables created successfully!")

if __name__ == "__main__":
    app.run(debug=True)
