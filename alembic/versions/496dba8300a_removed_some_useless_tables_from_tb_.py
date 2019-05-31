"""Removed some useless tables from tb_command

Revision ID: 496dba8300a
Revises: 36dcb45bcaf
Create Date: 2015-12-13 01:09:31.940434

"""

# revision identifiers, used by Alembic.
revision = '496dba8300a'
down_revision = '36dcb45bcaf'
branch_labels = None
depends_on = None

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import mysql


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tb_command', 'created')
    op.drop_column('tb_command', 'last_updated')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tb_command', sa.Column('last_updated', mysql.DATETIME(), nullable=True))
    op.add_column('tb_command', sa.Column('created', mysql.DATETIME(), nullable=True))
    ### end Alembic commands ###
