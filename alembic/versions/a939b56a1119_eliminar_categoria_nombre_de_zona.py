"""Eliminar categoria_nombre de Zona

Revision ID: a939b56a1119
Revises: 06d6c28e0b06
Create Date: 2025-01-27 07:56:02.970571

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'a939b56a1119'
down_revision: Union[str, None] = '06d6c28e0b06'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    pass
    # ### end Alembic commands ###