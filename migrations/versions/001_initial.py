# 001_initial.py
from alembic import op
import sqlalchemy as sa

def upgrade():
    # Create initial tables
    op.create_table(
        'users',
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('username', sa.String(50), nullable=False),
        sa.Column('email', sa.String(120), nullable=False),
    )

def downgrade():
    # Drop tables if downgrade is needed
    op.drop_table('users')
