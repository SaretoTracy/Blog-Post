"""Initial Migration

Revision ID: b262c86e1ab6
Revises: 
Create Date: 2022-03-14 12:57:40.714332

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'b262c86e1ab6'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('content', sa.String(), nullable=True))
    op.drop_index('ix_blogs_description', table_name='blogs')
    op.create_index(op.f('ix_blogs_content'), 'blogs', ['content'], unique=False)
    op.drop_column('blogs', 'description')
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('blogs', sa.Column('description', sa.VARCHAR(), autoincrement=False, nullable=True))
    op.drop_index(op.f('ix_blogs_content'), table_name='blogs')
    op.create_index('ix_blogs_description', 'blogs', ['description'], unique=False)
    op.drop_column('blogs', 'content')
    # ### end Alembic commands ###
