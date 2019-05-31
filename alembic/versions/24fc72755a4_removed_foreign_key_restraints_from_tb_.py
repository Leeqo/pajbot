"""Removed foreign key restraints from tb_pleblist_song_info

Revision ID: 24fc72755a4
Revises: 1daf721dac
Create Date: 2015-12-09 02:40:54.595340

"""

# revision identifiers, used by Alembic.
revision = '24fc72755a4'
down_revision = '1daf721dac'
branch_labels = None
depends_on = None

from alembic import op


def upgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('tb_pleblist_song_info_ibfk_1', 'tb_pleblist_song_info', type_='foreignkey')
    ### end Alembic commands ###


def downgrade():
    ### commands auto generated by Alembic - please adjust! ###
    op.create_foreign_key('tb_pleblist_song_info_ibfk_1', 'tb_pleblist_song_info', 'tb_pleblist_song', ['pleblist_song_youtube_id'], ['youtube_id'])
    ### end Alembic commands ###
