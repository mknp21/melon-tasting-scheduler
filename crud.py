"""CRUD operations."""


from model import db, User, Reservation, connect_to_db
from datetime import date, time, datetime


def create_user(name, email):
    """Create a new user."""

    user = User(name=name, email=email)
    db.session.add(user)
    db.session.commit()

    return user


def create_reservation(user, date, start_time, end_time):
    """Create a reservation."""

    date = date(date)
    start_time = time(start_time)
    end_time = time(end_time)

    reservation = Reservation(user=user, date=date, start_time=start_time, end_time=end_time)
    db.session.add(reservation)
    db.session.commit()

    return reservation


def get_user_by_id(user_id):
    """Return a user by id."""

    return User.query.filter(User.user_id == user_id).first()


def get_user_by_email(email):
    """Return a user by email."""

    return User.query.filter(User.email == email).first()


def get_all_reservations_by_email(email):
    """Return all saved items."""

    user = get_user_by_email(email)

    return Reservation.query.filter(Reservation.user == user).all()

if __name__ == '__main__':
    from server import app
    connect_to_db(app)