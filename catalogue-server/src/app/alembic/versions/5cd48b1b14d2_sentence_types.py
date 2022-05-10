"""sentence types

Revision ID: 5cd48b1b14d2
Revises: 5bca04bb04f5
Create Date: 2022-02-17 05:33:18.011076

"""
from alembic import op
import sqlalchemy as sa
import sqlalchemy_utils

# revision identifiers, used by Alembic.
revision = '5cd48b1b14d2'
down_revision = '5bca04bb04f5'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('sentence', sa.Column('has_punctuation', sa.Boolean()))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('sentence', 'has_punctuation')
    # ### end Alembic commands ###