"""Made a bunch of values non-nullable in the tb_commands table

Revision ID: 278a47e21d5
Revises: 32f05bdc22
Create Date: 2015-11-28 02:49:41.387442

"""

# revision identifiers, used by Alembic.
revision = '278a47e21d5'
down_revision = '32f05bdc22'
branch_labels = None
depends_on = None

from alembic import op
from sqlalchemy.dialects import mysql

def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tb_commands', 'command',
               existing_type=mysql.TEXT(),
               nullable=False)
    op.alter_column('tb_commands', 'cost',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('tb_commands', 'delay_all',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('tb_commands', 'delay_user',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('tb_commands', 'enabled',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False)
    op.alter_column('tb_commands', 'level',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('tb_commands', 'mod_only',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False)
    op.alter_column('tb_commands', 'num_uses',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=False)
    op.alter_column('tb_commands', 'sub_only',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=False)
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('tb_commands', 'sub_only',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True)
    op.alter_column('tb_commands', 'num_uses',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('tb_commands', 'mod_only',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True)
    op.alter_column('tb_commands', 'level',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('tb_commands', 'enabled',
               existing_type=mysql.TINYINT(display_width=1),
               nullable=True)
    op.alter_column('tb_commands', 'delay_user',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('tb_commands', 'delay_all',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('tb_commands', 'cost',
               existing_type=mysql.INTEGER(display_width=11),
               nullable=True)
    op.alter_column('tb_commands', 'command',
               existing_type=mysql.TEXT(),
               nullable=True)
    ### end Alembic commands ###
