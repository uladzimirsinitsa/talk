"""empty message

Revision ID: db67c931bca0
Revises: 476a5fe419a8
Create Date: 2021-02-07 16:32:58.377099

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'db67c931bca0'
down_revision = '476a5fe419a8'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('promotion', 'body',
               existing_type=sa.TEXT(),
               nullable=False)
    op.alter_column('promotion', 'description',
               existing_type=sa.VARCHAR(length=160),
               nullable=False)
    op.alter_column('promotion', 'img',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.alter_column('promotion', 'img_alt',
               existing_type=sa.VARCHAR(length=100),
               nullable=False)
    op.alter_column('promotion', 'link_casino',
               existing_type=sa.VARCHAR(length=300),
               nullable=False)
    op.alter_column('promotion', 'slug',
               existing_type=sa.VARCHAR(length=75),
               nullable=True)
    op.alter_column('promotion', 'title',
               existing_type=sa.VARCHAR(length=70),
               nullable=False)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('promotion', 'title',
               existing_type=sa.VARCHAR(length=70),
               nullable=True)
    op.alter_column('promotion', 'slug',
               existing_type=sa.VARCHAR(length=75),
               nullable=False)
    op.alter_column('promotion', 'link_casino',
               existing_type=sa.VARCHAR(length=300),
               nullable=True)
    op.alter_column('promotion', 'img_alt',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('promotion', 'img',
               existing_type=sa.VARCHAR(length=100),
               nullable=True)
    op.alter_column('promotion', 'description',
               existing_type=sa.VARCHAR(length=160),
               nullable=True)
    op.alter_column('promotion', 'body',
               existing_type=sa.TEXT(),
               nullable=True)
    # ### end Alembic commands ###
