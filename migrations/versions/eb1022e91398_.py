"""empty message

Revision ID: eb1022e91398
Revises: 903d2f48d84f
Create Date: 2023-09-12 22:05:19.048553

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'eb1022e91398'
down_revision = '903d2f48d84f'
branch_labels = None
depends_on = None


def upgrade():
    with op.batch_alter_table('learned_word', schema=None) as batch_op:
        batch_op.add_column(sa.Column('definition', sa.String(length=20), nullable=True))


def downgrade():
    with op.batch_alter_table('learned_word', schema=None) as batch_op:
        batch_op.drop_column('definition')
