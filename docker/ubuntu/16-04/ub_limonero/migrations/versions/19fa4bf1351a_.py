"""empty message

Revision ID: 19fa4bf1351a
Revises: 275b0e49dff7
Create Date: 2018-08-10 10:44:21.652231

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '19fa4bf1351a'
down_revision = '275b0e49dff7'
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('model', sa.Column('job_id', sa.Integer(), nullable=False))
    op.add_column('model', sa.Column('task_id', sa.String(length=200), nullable=False))
    op.add_column('model', sa.Column('workflow_id', sa.Integer(), nullable=False))
    op.add_column('model', sa.Column('workflow_name', sa.String(length=200), nullable=True))
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_column('model', 'workflow_name')
    op.drop_column('model', 'workflow_id')
    op.drop_column('model', 'task_id')
    op.drop_column('model', 'job_id')
    # ### end Alembic commands ###
