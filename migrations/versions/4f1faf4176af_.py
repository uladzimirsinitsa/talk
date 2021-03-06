"""empty message

Revision ID: 4f1faf4176af
Revises: 0c3e30899544
Create Date: 2021-02-07 02:11:34.593209

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '4f1faf4176af'
down_revision = '0c3e30899544'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('promotion', 'slug',
               existing_type=sa.VARCHAR(length=75),
               nullable=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('promotion', 'slug',
               existing_type=sa.VARCHAR(length=75),
               nullable=False)
    # ### end Alembic commands ###
