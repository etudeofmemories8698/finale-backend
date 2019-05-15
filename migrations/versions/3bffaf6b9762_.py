"""empty message

Revision ID: 3bffaf6b9762
Revises: 80a90ad42b3a
Create Date: 2019-05-13 22:41:33.180678

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '3bffaf6b9762'
down_revision = '80a90ad42b3a'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('user', sa.Column('imgurl', sa.String(length=500), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('user', 'imgurl')
    # ### end Alembic commands ###
