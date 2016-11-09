"""empty message

Revision ID: d92998342804
Revises: None
Create Date: 2016-10-31 13:01:49.458272

"""

# revision identifiers, used by Alembic.
revision = 'd92998342804'
down_revision = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('image', sa.Column('thumbnail', sa.String(length=1000), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('image', 'thumbnail')
    ### end Alembic commands ###