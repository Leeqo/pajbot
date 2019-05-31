"""Initial DB Version

Revision ID: 4f48d3dd0fb
Revises: 
Create Date: 2015-11-03 17:19:00.113496

"""

# revision identifiers, used by Alembic.
revision = '4f48d3dd0fb'
down_revision = None
branch_labels = None
depends_on = None

import sqlalchemy as sa
from alembic import op
from sqlalchemy.dialects import mysql


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_table('tb_commands',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.Column('action', mysql.TEXT(), nullable=True),
    sa.Column('extra_args', mysql.TEXT(), nullable=True),
    sa.Column('command', mysql.TEXT(), nullable=True),
    sa.Column('description', mysql.TEXT(), nullable=True),
    sa.Column('delay_all', sa.Integer(), nullable=True),
    sa.Column('delay_user', sa.Integer(), nullable=True),
    sa.Column('enabled', sa.Boolean(), nullable=True),
    sa.Column('num_uses', sa.Integer(), nullable=True),
    sa.Column('cost', sa.Integer(), nullable=True),
    sa.Column('can_execute_with_whisper', sa.Boolean(), nullable=True),
    sa.Column('sub_only', sa.Boolean(), nullable=True),
    sa.Column('created', sa.DateTime(), nullable=True),
    sa.Column('last_updated', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_emote',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('emote_id', sa.Integer(), nullable=True),
    sa.Column('emote_hash', sa.String(length=32), nullable=True),
    sa.Column('code', sa.String(length=64), nullable=True),
    sa.Column('tm_record', sa.Integer(), nullable=True),
    sa.Column('count', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_filters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=128), nullable=True),
    sa.Column('type', sa.String(length=64), nullable=True),
    sa.Column('action', mysql.TEXT(), nullable=True),
    sa.Column('extra_args', mysql.TEXT(), nullable=True),
    sa.Column('filter', mysql.TEXT(), nullable=True),
    sa.Column('source', mysql.TEXT(), nullable=True),
    sa.Column('enabled', sa.Boolean(), nullable=True),
    sa.Column('num_uses', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_idata',
    sa.Column('id', sa.String(length=64), nullable=False),
    sa.Column('value', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_link_blacklist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('domain', sa.String(length=256), nullable=True),
    sa.Column('path', mysql.TEXT(), nullable=True),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_link_data',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('url', mysql.TEXT(), nullable=True),
    sa.Column('times_linked', sa.Integer(), nullable=True),
    sa.Column('first_linked', sa.DateTime(), nullable=True),
    sa.Column('last_linked', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_link_whitelist',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('domain', sa.String(length=256), nullable=True),
    sa.Column('path', mysql.TEXT(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_motd',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('message', sa.String(length=400), nullable=True),
    sa.Column('enabled', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_settings',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('setting', sa.String(length=128), nullable=True),
    sa.Column('value', mysql.TEXT(), nullable=True),
    sa.Column('type', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_twitter_following',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=32), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_user',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=128), nullable=True),
    sa.Column('username_raw', sa.String(length=128), nullable=True),
    sa.Column('level', sa.Integer(), nullable=True),
    sa.Column('points', sa.Integer(), nullable=True),
    sa.Column('num_lines', sa.Integer(), nullable=True),
    sa.Column('subscriber', sa.Boolean(), nullable=True),
    sa.Column('last_seen', sa.DateTime(), nullable=True),
    sa.Column('last_active', sa.DateTime(), nullable=True),
    sa.Column('minutes_in_chat_online', sa.Integer(), nullable=True),
    sa.Column('minutes_in_chat_offline', sa.Integer(), nullable=True),
    sa.Column('twitch_access_token', sa.String(length=128), nullable=True),
    sa.Column('twitch_refresh_token', sa.String(length=128), nullable=True),
    sa.Column('discord_user_id', sa.String(length=32), nullable=True),
    sa.Column('ignored', sa.Boolean(), nullable=True),
    sa.Column('banned', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tb_whisper_account',
    sa.Column('username', sa.String(length=128), nullable=False),
    sa.Column('oauth', sa.String(length=128), nullable=True),
    sa.Column('enabled', sa.Boolean(), nullable=True),
    sa.PrimaryKeyConstraint('username')
    )
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('tb_whisper_account')
    op.drop_table('tb_user')
    op.drop_table('tb_twitter_following')
    op.drop_table('tb_settings')
    op.drop_table('tb_motd')
    op.drop_table('tb_link_whitelist')
    op.drop_table('tb_link_data')
    op.drop_table('tb_link_blacklist')
    op.drop_table('tb_idata')
    op.drop_table('tb_filters')
    op.drop_table('tb_emote')
    op.drop_table('tb_commands')
    ### end Alembic commands ###
