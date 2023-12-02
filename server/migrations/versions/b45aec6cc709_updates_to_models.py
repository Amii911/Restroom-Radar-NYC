"""updates to models

Revision ID: b45aec6cc709
Revises: eceee570d985
Create Date: 2023-11-23 16:17:39.972313

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b45aec6cc709'
down_revision = 'eceee570d985'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('user_bathrooms',
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('bathroom_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['bathroom_id'], ['bathrooms.id'], name=op.f('fk_user_bathrooms_bathroom_id_bathrooms')),
    sa.ForeignKeyConstraint(['user_id'], ['users.id'], name=op.f('fk_user_bathrooms_user_id_users')),
    sa.PrimaryKeyConstraint('user_id', 'bathroom_id')
    )
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.create_unique_constraint(None, ['username'])

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('users', schema=None) as batch_op:
        batch_op.drop_constraint(None, type_='unique')

    op.drop_table('user_bathrooms')
    # ### end Alembic commands ###