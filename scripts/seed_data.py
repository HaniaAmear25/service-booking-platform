
from app import create_app
from app.models import db, Business, Service, Staff, Customer

app = create_app()

with app.app_context():

    # Prevents duplicate sample data if the script runs again
    existing = Business.query.filter_by(
        email="hello@glowexample.ie"
    ).first()

    if existing:
        print("Glow Hair Studio already exists. Skipping.")
    else:
        # Create a business
        business = Business(
            name="Glow Hair Studio",
            business_type="Hair Salon",
            email="hello@glowexample.ie",
            phone="010000000",
            address="Dublin, Ireland"
        )

        db.session.add(business)
        db.session.flush()

        # Create services
        haircut = Service(
            business_id=business.id,
            name="Haircut",
            duration_minutes=45,
            price=35.00
        )

        colour = Service(
            business_id=business.id,
            name="Hair Colour",
            duration_minutes=120,
            price=90.00
        )

        blowdry = Service(
            business_id=business.id,
            name="Blow Dry",
            duration_minutes=30,
            price=30.00
        )

        # Create staff
        sarah = Staff(
            business_id=business.id,
            name="Sarah"
        )

        emma = Staff(
            business_id=business.id,
            name="Emma"
        )

        # Assign services to staff
        sarah.services.extend([haircut, colour])
        emma.services.extend([haircut, blowdry])

        # Create customers
        customer1 = Customer(
            business_id=business.id,
            name="Hania",
            email="hania@example.com"
        )

        customer2 = Customer(
            business_id=business.id,
            name="Amy",
            email="amy@example.com"
        )

        db.session.add_all([
            haircut, colour, blowdry,
            sarah, emma,
            customer1, customer2
        ])

        db.session.commit()

        print("Sample data inserted successfully!")
