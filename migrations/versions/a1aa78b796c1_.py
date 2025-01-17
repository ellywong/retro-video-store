"""empty message

Revision ID: a1aa78b796c1
Revises: 94bbcc986726
Create Date: 2021-11-11 12:46:56.699849

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a1aa78b796c1'
down_revision = '94bbcc986726'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('customer', sa.Column('name', sa.String(), nullable=True))
    op.add_column('customer', sa.Column('phone', sa.String(), nullable=True))
    op.add_column('customer', sa.Column('postal_code', sa.String(), nullable=True))
    op.add_column('customer', sa.Column('register_at', sa.DateTime(), nullable=True))
    op.add_column('rental', sa.Column('customer_id', sa.Integer(), nullable=False))
    op.add_column('rental', sa.Column('video_id', sa.Integer(), nullable=False))
    op.create_foreign_key(None, 'rental', 'customer', ['customer_id'], ['id'])
    op.create_foreign_key(None, 'rental', 'video', ['video_id'], ['id'])
    op.add_column('video', sa.Column('release_date', sa.DateTime(), nullable=True))
    op.add_column('video', sa.Column('title', sa.String(), nullable=True))
    op.add_column('video', sa.Column('total_inventory', sa.Integer(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('video', 'total_inventory')
    op.drop_column('video', 'title')
    op.drop_column('video', 'release_date')
    op.drop_constraint(None, 'rental', type_='foreignkey')
    op.drop_constraint(None, 'rental', type_='foreignkey')
    op.drop_column('rental', 'video_id')
    op.drop_column('rental', 'customer_id')
    op.drop_column('customer', 'register_at')
    op.drop_column('customer', 'postal_code')
    op.drop_column('customer', 'phone')
    op.drop_column('customer', 'name')
    # ### end Alembic commands ###
