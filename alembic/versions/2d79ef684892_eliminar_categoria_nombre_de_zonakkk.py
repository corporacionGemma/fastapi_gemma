"""Eliminar categoria_nombre de Zonakkk

Revision ID: 2d79ef684892
Revises: a939b56a1119
Create Date: 2025-01-27 08:02:40.124030

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = '2d79ef684892'
down_revision: Union[str, None] = 'a939b56a1119'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_constraint('fk_zona_categoria', 'zonas', type_='foreignkey')
    op.drop_column('zonas', 'categoria_nombre')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('zonas', sa.Column('categoria_nombre', sa.VARCHAR(length=100, collation='SQL_Latin1_General_CP1_CI_AS'), autoincrement=False, nullable=False))
    op.create_foreign_key('fk_zona_categoria', 'zonas', 'categorias', ['categoria_nombre'], ['nombre'])
    # ### end Alembic commands ###