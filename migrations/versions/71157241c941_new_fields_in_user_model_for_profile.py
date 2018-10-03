"""new fields in user model for profile

Revision ID: 71157241c941
Revises: f1b98dda215f
Create Date: 2019-01-13 16:42:17.524555

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '71157241c941'
down_revision = 'f1b98dda215f'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('about_me', sa.String(length=140), nullable=True))
    op.add_column('user', sa.Column('last_seen', sa.DateTime(), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'last_seen')
    op.drop_column('user', 'about_me')
    # ### end Alembic commands ###
