"""Adds disabled_at field

Revision ID: e106239a3986
Revises: 798ea0a04eeb
Create Date: 2021-02-13 05:35:49.240346

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'e106239a3986'
down_revision = '798ea0a04eeb'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('leads', sa.Column('disabled_at', sa.DateTime(), nullable=True))
    op.add_column('stages', sa.Column('disabled_at', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('stages', 'disabled_at')
    op.drop_column('leads', 'disabled_at')
    # ### end Alembic commands ###
