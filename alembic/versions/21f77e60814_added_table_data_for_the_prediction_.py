"""Added table data for the prediction stuff

Revision ID: 21f77e60814
Revises: 465365d933e
Create Date: 2015-12-30 16:33:40.491732

"""

# revision identifiers, used by Alembic.
revision = '21f77e60814'
down_revision = '465365d933e'
branch_labels = None
depends_on = None

import sqlalchemy as sa
from alembic import op


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_prediction_run',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('winner_id', sa.Integer(), nullable=True),
    sa.Column('started', sa.DateTime(), nullable=False),
    sa.Column('ended', sa.DateTime(), nullable=True),
    sa.Column('open', sa.Boolean(), server_default=sa.text('true'), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_prediction_run_entry',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('prediction_run_id', sa.Integer(), nullable=False),
    sa.Column('user_id', sa.Integer(), nullable=False),
    sa.Column('prediction', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['prediction_run_id'], ['tb_prediction_run.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tb_prediction_run_entry')
    op.drop_table('tb_prediction_run')
    ### end Alembic commands ###
