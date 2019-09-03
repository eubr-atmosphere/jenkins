"""empty message

Revision ID: c1124305c79e
Revises: 
Create Date: 2017-02-16 23:30:48.456635

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'c1124305c79e'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('storage',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('type', sa.Enum('HDFS', '__module__', 'OPHIDIA', 'ELASTIC_SEARCH', 'MONGODB', 'POSTGIS', 'HBASE', '__doc__', 'CASSANDRA', name='StorageTypeEnumType'), nullable=False),
    sa.Column('url', sa.String(length=1000), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('data_source',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('enabled', sa.Boolean(), nullable=False),
    sa.Column('read_only', sa.Boolean(), nullable=False),
    sa.Column('url', sa.String(length=200), nullable=False),
    sa.Column('created', sa.DateTime(), nullable=False),
    sa.Column('format', sa.Enum('__module__', 'XML_FILE', 'NETCDF4', 'HDF5', 'SHAPEFILE', 'TEXT', 'CUSTOM', 'JSON', 'CSV', 'PICKLE', '__doc__', name='DataSourceFormatEnumType'), nullable=False),
    sa.Column('provenience', sa.Text(), nullable=True),
    sa.Column('estimated_rows', sa.Integer(), nullable=True),
    sa.Column('estimated_size_in_mega_bytes', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('expiration', sa.String(length=200), nullable=True),
    sa.Column('user_id', sa.Integer(), nullable=True),
    sa.Column('user_login', sa.String(length=50), nullable=True),
    sa.Column('user_name', sa.String(length=200), nullable=True),
    sa.Column('tags', sa.String(length=100), nullable=True),
    sa.Column('temporary', sa.Boolean(), nullable=False),
    sa.Column('workflow_id', sa.Integer(), nullable=True),
    sa.Column('task_id', sa.Integer(), nullable=True),
    sa.Column('storage_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['storage_id'], ['storage.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('attribute',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=100), nullable=False),
    sa.Column('description', sa.String(length=500), nullable=True),
    sa.Column('type', sa.Enum('__module__', 'ENUM', 'LAT_LONG', 'DOUBLE', 'DECIMAL', 'FLOAT', 'CHARACTER', 'LONG', 'DATETIME', 'VECTOR', 'TEXT', 'TIME', 'DATE', 'INTEGER', 'TIMESTAMP', '__doc__', '__init__', name='DataTypeEnumType'), nullable=False),
    sa.Column('size', sa.Integer(), nullable=True),
    sa.Column('precision', sa.Integer(), nullable=True),
    sa.Column('nullable', sa.Boolean(), nullable=False),
    sa.Column('enumeration', sa.Boolean(), nullable=False),
    sa.Column('missing_representation', sa.String(length=200), nullable=True),
    sa.Column('feature', sa.Boolean(), nullable=False),
    sa.Column('label', sa.Boolean(), nullable=False),
    sa.Column('distinct_values', sa.Integer(), nullable=True),
    sa.Column('mean_value', sa.Float(), nullable=True),
    sa.Column('median_value', sa.String(length=200), nullable=True),
    sa.Column('max_value', sa.String(length=200), nullable=True),
    sa.Column('min_value', sa.String(length=200), nullable=True),
    sa.Column('std_deviation', sa.Float(), nullable=True),
    sa.Column('missing_total', sa.String(length=200), nullable=True),
    sa.Column('deciles', sa.Text(), nullable=True),
    sa.Column('data_source_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['data_source_id'], ['data_source.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('attribute')
    op.drop_table('data_source')
    op.drop_table('storage')
    # ### end Alembic commands ###
