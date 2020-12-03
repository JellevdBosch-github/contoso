from app import db


class Base(db.Model):

    __abstract__ = True

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date_created = db.Column(db.DateTime, default=db.func.current_timestamp())
    date_modified = db.Column(db.DateTime, default=db.func.current_timestamp(),
                              onupdate=db.func.current_timestamp())


class Customer(Base):

    __tablename__ = 'customer'

    # Personal info
    first_name = db.Column(db.String(50), nullable=False)
    middle_name = db.Column(db.String(50), nullable=True)
    last_name = db.Column(db.String(50), nullable=False)

    birth_date = db.Column(db.DATE, default=db.func.current_date(), nullable=False)
    # m = married, s = single, d = divorced, u = unknown
    marital_status = db.Column(db.CHAR(1), default='u', nullable=False)
    # m = male, f = female, o = other, u = unknown
    gender = db.Column(db.CHAR(1), default='u', nullable=False)
    total_children = db.Column(db.SMALLINT, default=0, nullable=False)
    education = db.Column(db.String(40), default='', nullable=False)
    occupation = db.Column(db.String(100), default='', nullable=False)
    phone_number = db.Column(db.String(20), default='', nullable=False)
    yearly_income = db.Column(db.DECIMAL(8, 2), default=0.00, nullable=False)

    # Address
    country = db.Column(db.String(40), default='', nullable=False)
    city = db.Column(db.String(40), default='', nullable=False)
    street = db.Column(db.String(40), default='', nullable=False)
    house_number = db.Column(db.String(6), default='', nullable=False)
    zip_code = db.Column(db.CHAR(6), default='', nullable=False)

    # Identification: email & password
    email = db.Column(db.String(50), nullable=False,
                      unique=True)
    password = db.Column(db.String(50), nullable=False)

    # Customer info
    date_first_purchase = db.Column(db.DateTime, default=db.func.current_timestamp(), nullable=False)
    customer_type = db.Column(db.String(15), default='', nullable=False)
    title = db.Column(db.String(8), default='', nullable=False)

    # orders = db.relationship('Order', lazy='select', backref=db.backref('customer', lazy='joined'))

    def __repr__(self):
        return f'<Customer #{self.id} | {self.first_name} {self.middle_name} {self.last_name}>'
