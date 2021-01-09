"""Adds current_stage_id to leads

Revision ID: ff965a5b7ee8
Revises: da8054d1df51
Create Date: 2021-01-09 19:09:03.967853

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'ff965a5b7ee8'
down_revision = 'da8054d1df51'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('leads', sa.Column('current_stage_id', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('leads', 'current_stage_id')
    # ### end Alembic commands ###
