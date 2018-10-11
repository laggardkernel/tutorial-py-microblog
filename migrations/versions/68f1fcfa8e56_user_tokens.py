"""user tokens

Revision ID: 68f1fcfa8e56
Revises: 2996a6881c60
Create Date: 2019-02-05 21:39:18.550695

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '68f1fcfa8e56'
down_revision = '2996a6881c60'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('token', sa.String(length=32), nullable=True))
    op.add_column('user', sa.Column('token_expiration', sa.DateTime(), nullable=True))
    op.create_index(op.f('ix_user_token'), 'user', ['token'], unique=True)
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f('ix_user_token'), table_name='user')
    op.drop_column('user', 'token_expiration')
    op.drop_column('user', 'token')
    # ### end Alembic commands ###
