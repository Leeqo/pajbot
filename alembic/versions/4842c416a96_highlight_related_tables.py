"""highlight-related tables

Revision ID: 4842c416a96
Revises: 59a5d12aa83
Create Date: 2015-11-19 02:35:41.066633

"""

# revision identifiers, used by Alembic.
revision = '4842c416a96'
down_revision = '59a5d12aa83'
branch_labels = None
depends_on = None

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import mysql


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_stream',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('title', sa.String(length=256), nullable=False),
    sa.Column('stream_start', sa.DateTime(), nullable=False),
    sa.Column('stream_end', sa.DateTime(), nullable=True),
    sa.Column('ended', sa.Boolean(), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_stream_chunk',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('stream_id', sa.Integer(), nullable=False),
    sa.Column('broadcast_id', mysql.BIGINT(unsigned=True), nullable=False),
    sa.Column('video_url', sa.String(length=128), nullable=True),
    sa.Column('chunk_start', sa.DateTime(), nullable=False),
    sa.Column('chunk_end', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['stream_id'], ['tb_stream.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('broadcast_id')
    )
    op.create_table('tb_stream_chunk_highlight',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('stream_chunk_id', sa.Integer(), nullable=False),
    sa.Column('created_at', sa.DateTime(), nullable=False),
    sa.Column('highlight_offset', sa.Integer(), nullable=False),
    sa.Column('description', sa.String(length=128), nullable=True),
    sa.ForeignKeyConstraint(['stream_chunk_id'], ['tb_stream_chunk.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tb_stream_chunk_highlight')
    op.drop_table('tb_stream_chunk')
    op.drop_table('tb_stream')
    ### end Alembic commands ###
