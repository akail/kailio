"""unique slug

Revision ID: 333a67a5bd77
Revises: b6756ff75a38
Create Date: 2020-07-01 21:21:09.098722

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '333a67a5bd77'
down_revision = 'b6756ff75a38'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint('pags_slug_unique_constraint', 'pages', ['slug'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('pags_slug_unique_constraint', 'pages', type_='unique')
    # ### end Alembic commands ###
