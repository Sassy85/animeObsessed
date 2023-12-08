"""created streams, animes, and platforms table and foreign keys

Revision ID: 273674f1e04f
Revises: 26b19dbaabb2
Create Date: 2023-12-07 15:47:05.773545

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '273674f1e04f'
down_revision = '26b19dbaabb2'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('animes',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.Column('num_episodes', sa.Integer(), nullable=True),
    sa.Column('summary', sa.String(), nullable=True),
    sa.Column('completed', sa.String(), nullable=True),
    sa.Column('likes', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('streams',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(), nullable=True),
    sa.Column('image', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('platforms',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('anime_id', sa.Integer(), nullable=True),
    sa.Column('stream_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['anime_id'], ['animes.id'], name=op.f('fk_platforms_anime_id_animes')),
    sa.ForeignKeyConstraint(['stream_id'], ['streams.id'], name=op.f('fk_platforms_stream_id_streams')),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('platforms')
    op.drop_table('streams')
    op.drop_table('animes')
    # ### end Alembic commands ###
