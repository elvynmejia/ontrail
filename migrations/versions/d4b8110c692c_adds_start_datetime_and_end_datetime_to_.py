"""Adds start_datetime and end_datetime to stage

Revision ID: d4b8110c692c
Revises: 771d7baa44e5
Create Date: 2020-10-19 18:49:35.929132

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd4b8110c692c'
down_revision = '771d7baa44e5'
branch_labels = None
depends_on = None


def upgrade():
		op.add_column('stage', sa.Column('start_datetime', sa.DateTime, nullable=True)) # nullable=False
		op.add_column('stage', sa.Column('end_datetime', sa.DateTime, nullable=True))


def downgrade():
    op.drop_column('stage', sa.Column('start_datetime'))
    op.drop_column('stage', sa.Column('end_datetime'))