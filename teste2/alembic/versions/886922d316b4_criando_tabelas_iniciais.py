"""Criando tabelas iniciais

Revision ID: 886922d316b4
Revises: 
Create Date: 2024-07-18 17:12:22.735572

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '886922d316b4'
down_revision: Union[str, None] = None
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('fornecedores',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.Column('cnpj', sa.String(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('tecnicos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.Column('matricula', sa.String(), nullable=False),
    sa.Column('telefone', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('matricula'),
    sa.UniqueConstraint('matricula', name='_matricula_uc')
    )
    op.create_table('usuarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.Column('username', sa.String(), nullable=False),
    sa.Column('senha', sa.String(), nullable=False),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('username')
    )
    op.create_table('materiais',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nome', sa.String(), nullable=False),
    sa.Column('preco', sa.Float(), nullable=False),
    sa.Column('nota_fiscal', sa.String(), nullable=False),
    sa.Column('quantidade', sa.Integer(), nullable=False),
    sa.Column('data', sa.DateTime(), nullable=True),
    sa.Column('fornecedor_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['fornecedor_id'], ['fornecedores.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('nota_fiscal')
    )
    op.create_table('retirada_material',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('codigo', sa.String(length=20), nullable=False),
    sa.Column('ordem_servico', sa.String(length=50), nullable=False),
    sa.Column('produto_id', sa.Integer(), nullable=False),
    sa.Column('tecnico_id', sa.Integer(), nullable=False),
    sa.Column('quantidade', sa.Integer(), nullable=False),
    sa.Column('data', sa.Date(), nullable=False),
    sa.Column('local', sa.Text(), nullable=False),
    sa.ForeignKeyConstraint(['produto_id'], ['materiais.id'], ),
    sa.ForeignKeyConstraint(['tecnico_id'], ['tecnicos.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('codigo'),
    sa.UniqueConstraint('ordem_servico')
    )
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('retirada_material')
    op.drop_table('materiais')
    op.drop_table('usuarios')
    op.drop_table('tecnicos')
    op.drop_table('fornecedores')
    # ### end Alembic commands ###
