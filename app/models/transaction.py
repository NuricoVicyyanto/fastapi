from app.models import Base
import sqlalchemy as sa

class Transaction(Base):
    __tablename__ = 'transactions'
    id = sa.Column(sa.Integer, primary_key=True)
    user_id = sa.Column('user_id', sa.Integer)
    created_at = sa.Column('created_at', sa.DateTime)
    modified_at = sa.Column('modified_at', sa.DateTime)
    status = sa.Column('status', sa.Integer)
    total = sa.Column('total', sa.Integer)