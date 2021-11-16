"""CRUD operations."""


from model import db, User, Reservation, connect_to_db


def create_user(name, email):
    """Create a new user."""

    user = User(name=name, email=email)
    db.session.add(user)
    db.session.commit()

    return user


def create_reservation(user, details):
    """Create a reservation."""

    reservation = Reservation(user=user, details=details)
    db.session.add(reservation)
    db.session.commit()

    return reservation


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()


def get_all_reservations_by_email(email):
    """Return all saved items."""

    user = get_user_by_email(email)

    return Reservation.query.filter(Reservation.user == user).all()

if __name__ == '__main__':
    # from server import app
    connect_to_db(app)