"""Initial migration.

Revision ID: 70cba098c07c
Revises: 
Create Date: 2020-11-02 20:12:33.628322

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '70cba098c07c'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('announcements',
    sa.Column('uuid', sa.Integer(), nullable=False),
    sa.Column('image', sa.String(length=255), nullable=True),
    sa.Column('name', sa.String(length=255), nullable=True),
    sa.Column('description', sa.String(length=255), nullable=True),
    sa.Column('price', sa.Float(), nullable=True),
    sa.Column('status', sa.Enum('available', 'in_negotiation', 'paid', 'delivered', 'finished', name='announcementstatusenum'), nullable=True),
    sa.Column('type_', sa.Enum('item', 'account', 'gold', name='announcementtypeenum'), nullable=True),
    sa.Column('salesman_uuid', sa.Integer(), nullable=True),
    sa.Column('game', sa.String(length=255), nullable=True),
    sa.Column('server', sa.String(length=255), nullable=True),
    sa.Column('created_at', sa.DateTime(), nullable=True),
    sa.Column('updated_at', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('uuid')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=255), nullable=False),
    sa.Column('phone', sa.String(length=255), nullable=False),
    sa.Column('email', sa.String(length=255), nullable=False),
    sa.Column('password', sa.String(length=255), nullable=False),
    sa.Column('cpf', sa.String(length=255), nullable=False),
    sa.Column('isSalesman', sa.Boolean(), nullable=False),
    sa.Column('avatar', sa.String(length=255), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('phone')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('users')
    op.drop_table('announcements')
    # ### end Alembic commands ###
