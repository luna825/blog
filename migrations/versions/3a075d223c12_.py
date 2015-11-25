"""empty message

Revision ID: 3a075d223c12
Revises: None
Create Date: 2015-11-24 09:17:36.653000

"""

# revision identifiers, used by Alembic.
revision = '3a075d223c12'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('administors',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('email', sa.String(length=64), nullable=True),
    sa.Column('password_hash', sa.String(length=128), nullable=True),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.Column('location', sa.String(length=64), nullable=True),
    sa.Column('about_me', sa.Text(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_administors_email'), 'administors', ['email'], unique=True)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_administors_email'), table_name='administors')
    op.drop_table('administors')
    ### end Alembic commands ###