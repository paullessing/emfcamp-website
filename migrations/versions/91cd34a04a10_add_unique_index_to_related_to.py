"""add_unique_index_to_related_to

Revision ID: 91cd34a04a10
Revises: be0934972583
Create Date: 2024-04-21 20:46:28.014878

"""

# revision identifiers, used by Alembic.
revision = '91cd34a04a10'
down_revision = 'be0934972583'

from alembic import op
import sqlalchemy as sa


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_unique_constraint(op.f('uq_push_notification_job_related_to'), 'push_notification_job', ['related_to'])
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint(op.f('uq_push_notification_job_related_to'), 'push_notification_job', type_='unique')
    # ### end Alembic commands ###
