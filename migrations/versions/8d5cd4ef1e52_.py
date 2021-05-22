"""empty message

Revision ID: 8d5cd4ef1e52
Revises: aaa88a2bdc94
Create Date: 2021-05-22 11:25:00.300933

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8d5cd4ef1e52'
down_revision = 'aaa88a2bdc94'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('Artist', sa.Column('website_link', sa.String(length=120), nullable=True))
    op.add_column('Artist', sa.Column('looking_for_venues', sa.Boolean(), nullable=True))
    op.add_column('Artist', sa.Column('seeking_description', sa.String(length=1000), nullable=True))
    op.add_column('Venue', sa.Column('genres', sa.String(length=120), nullable=True))
    op.add_column('Venue', sa.Column('website_link', sa.String(length=120), nullable=True))
    op.add_column('Venue', sa.Column('looking_for_talent', sa.Boolean(), nullable=True))
    op.add_column('Venue', sa.Column('seeking_description', sa.String(length=1000), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('Venue', 'seeking_description')
    op.drop_column('Venue', 'looking_for_talent')
    op.drop_column('Venue', 'website_link')
    op.drop_column('Venue', 'genres')
    op.drop_column('Artist', 'seeking_description')
    op.drop_column('Artist', 'looking_for_venues')
    op.drop_column('Artist', 'website_link')
    # ### end Alembic commands ###
