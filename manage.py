from flask_script import Manager
from flask_migrate import Migrate, MigrateCommand
from app import app, db, models
from app.models import User, Conhap, ConhapItem
import unittest
import coverage
import os
import forgery_py as faker
from random import randint
from sqlalchemy.exc import IntegrityError

# Initializing the manager
manager = Manager(app)

# Initialize Flask Migrate
migrate = Migrate(app, db)

# Add the flask migrate
manager.add_command('db', MigrateCommand)

# Test coverage configuration
COV = coverage.coverage(
    branch=True,
    include='app/*',
    omit=[
        'app/auth/__init__.py',
        'app/conhap/__init__.py'
    ]
)
COV.start()


# Add test command
@manager.command
def test():
    """
    Run tests without coverage
    :return:
    """
    tests = unittest.TestLoader().discover('tests', pattern='test*.py')
    result = unittest.TextTestRunner(verbosity=2).run(tests)
    if result.wasSuccessful():
        return 0
    return 1


@manager.command
def dummy():
    # Create a user if they do not exist.
    user = User.query.filter_by(email="user@email.com").first()
    if not user:
        user = User("user@email.com", "123456")
        user.save()

    for _ in range(100):
        # Add series to the database
        series = Conapp(faker.name.industry(), user.id)
        series.save()

    for _ in range(1000):
        # Add items to the series
        series = Conhap.query.filter_by(id=randint(1, Conhap.query.count() - 1)).first()
        item = ConhapItem(faker.name.company_name(), faker.lorem_ipsum.word(), series.id)
        db.session.add(item)
        try:
            db.session.commit()
        except IntegrityError:
            db.session.rollback()


# Run the manager
if __name__ == '__main__':
    manager.run()
