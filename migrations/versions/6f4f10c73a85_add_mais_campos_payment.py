"""add mais campos Payment

Revision ID: 6f4f10c73a85
Revises: 5247d61dcd8a
Create Date: 2024-10-08 22:13:47.778556

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '6f4f10c73a85'
down_revision = '5247d61dcd8a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('payments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('description', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('status', sa.String(), nullable=True))
        batch_op.add_column(sa.Column('due_date', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('payment_date', sa.DateTime(), nullable=True))
        batch_op.add_column(sa.Column('date_created', sa.DateTime(), nullable=True))
        batch_op.drop_column('date')

    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    with op.batch_alter_table('payments', schema=None) as batch_op:
        batch_op.add_column(sa.Column('date', sa.DATETIME(), nullable=True))
        batch_op.drop_column('date_created')
        batch_op.drop_column('payment_date')
        batch_op.drop_column('due_date')
        batch_op.drop_column('status')
        batch_op.drop_column('description')

    # ### end Alembic commands ###
