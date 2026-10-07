from flask_sqlalchemy import SQLAlchemy

# Initialize the SQLAlchemy object
db = SQLAlchemy()
#defining the many to many relationships with staff adn services
staff_services = db.Table(
    "staff_services",

    db.Column(
        "staff_id",
        db.Integer,
        db.ForeignKey("staff.id"),
        primary_key=True
    ),

    db.Column(
        "service_id",
        db.Integer,
        db.ForeignKey("services.id"),
        primary_key=True
    )
)

# business model with relationships to servuces, staff, and customers
class Business(db.Model):
    __tablename__ = "businesses"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)
    business_type = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(30))
    address = db.Column(db.String(200))

    services = db.relationship(
    "Service",
    backref="business",
    lazy=True
)
    staff_members = db.relationship(
    "Staff",
    backref="business",
    lazy=True
)
    customers = db.relationship(
    "Customer",
    backref="business",
    lazy=True
)

    def __repr__(self):
        return f"<Business {self.name}>"

# Service model with a foreign key to the Business model
class Service(db.Model):
    __tablename__ = "services"

    id = db.Column(db.Integer, primary_key=True)

    business_id = db.Column(
        db.Integer,
        db.ForeignKey("businesses.id"),
        nullable=False
    )

    name = db.Column(db.String(120), nullable=False)
    description = db.Column(db.String(300))
    duration_minutes = db.Column(db.Integer, nullable=False)
    price = db.Column(db.Numeric(10, 2), nullable=False)

    def __repr__(self):
        return f"<Service {self.name}>"

# Staff model with a foreign key to the Business model and a many-to-many relationship with the Service model
class Staff(db.Model):
    __tablename__ = "staff"

    id = db.Column(db.Integer, primary_key=True)

    business_id = db.Column(
        db.Integer,
        db.ForeignKey("businesses.id"),
        nullable=False
    )

    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120))
    phone = db.Column(db.String(30))

    services = db.relationship(
        "Service",
        secondary=staff_services,
        backref="staff_members"
    )

    def __repr__(self):
        return f"<Staff {self.name}>"

# Customer model with a foreign key to the Business model
class Customer(db.Model):
    __tablename__ = "customers"

    id = db.Column(db.Integer, primary_key=True)

    business_id = db.Column(
        db.Integer,
        db.ForeignKey("businesses.id"),
        nullable=False
    )

    name = db.Column(db.String(120), nullable=False)
    email = db.Column(db.String(120), nullable = False)
    phone = db.Column(db.String(30))

    def __repr__(self):
        return f"<Customer {self.name}>"
