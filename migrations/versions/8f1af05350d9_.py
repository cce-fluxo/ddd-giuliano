"""empty message

Revision ID: 8f1af05350d9
Revises: 
Create Date: 2022-03-21 13:00:49.307867

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '8f1af05350d9'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('admin',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=70), nullable=False),
    sa.Column('senha_hash', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email')
    )
    op.create_table('carro',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('marca', sa.String(length=70), nullable=True),
    sa.Column('modelo', sa.String(length=100), nullable=True),
    sa.Column('ano', sa.String(length=10), nullable=True),
    sa.Column('cor', sa.String(length=20), nullable=True),
    sa.Column('preco', sa.Float(), nullable=True),
    sa.Column('motor', sa.String(length=50), nullable=True),
    sa.Column('bancos', sa.SmallInteger(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('cliente',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('email', sa.String(length=70), nullable=False),
    sa.Column('senha_hash', sa.LargeBinary(), nullable=False),
    sa.Column('nome', sa.String(length=150), nullable=True),
    sa.Column('cpf', sa.String(length=15), nullable=False),
    sa.Column('celular', sa.String(length=20), nullable=False),
    sa.Column('cep', sa.String(length=15), nullable=False),
    sa.Column('endereco', sa.String(length=150), nullable=True),
    sa.Column('complemento', sa.String(length=30), nullable=True),
    sa.Column('data_de_nascimento', sa.String(length=30), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('celular'),
    sa.UniqueConstraint('cpf'),
    sa.UniqueConstraint('email')
    )
    op.create_table('moto',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('marca', sa.String(length=70), nullable=True),
    sa.Column('modelo', sa.String(length=100), nullable=True),
    sa.Column('ano', sa.String(length=10), nullable=True),
    sa.Column('cor', sa.String(length=20), nullable=True),
    sa.Column('preco', sa.Float(), nullable=True),
    sa.Column('motor', sa.String(length=50), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('moto')
    op.drop_table('cliente')
    op.drop_table('carro')
    op.drop_table('admin')
    # ### end Alembic commands ###
