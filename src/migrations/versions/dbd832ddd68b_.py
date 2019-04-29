"""empty message

Revision ID: dbd832ddd68b
Revises: 
Create Date: 2019-04-03 15:16:23.408023

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'dbd832ddd68b'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('userFeature',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.String(length=100), nullable=False),
    sa.Column('intent_word', sa.String(length=255), nullable=False),
    sa.Column('context', sa.String(length=1000), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('userFeature')
    # ### end Alembic commands ###
