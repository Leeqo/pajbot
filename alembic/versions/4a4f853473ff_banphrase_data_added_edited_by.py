"""Banphrase Data added edited_by

Revision ID: 4a4f853473ff
Revises: da98ae62a74c
Create Date: 2016-02-11 06:01:44.517139

"""

# revision identifiers, used by Alembic.
revision = '4a4f853473ff'
down_revision = 'da98ae62a74c'
branch_labels = None
depends_on = None

from alembic import op
import sqlalchemy as sa


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.add_column('tb_banphrase_data', sa.Column('edited_by', sa.Integer(), nullable=True))
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('tb_banphrase_data', 'edited_by')
    ### end Alembic commands ###