"""empty message

Revision ID: d70d73e99765
Revises: 
Create Date: 2024-12-12 10:31:01.294304

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'd70d73e99765'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('banners',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('titulo', sa.String(length=150), nullable=False),
    sa.Column('imagen_url', sa.String(length=255), nullable=False),
    sa.Column('orden', sa.Integer(), nullable=True),
    sa.Column('estado', sa.Boolean(), nullable=True),
    sa.Column('fecha_creacion', sa.DateTime(), nullable=True),
    sa.Column('fecha_modificacion', sa.DateTime(), nullable=True),
    sa.Column('fecha_inicio', sa.DateTime(), nullable=True),
    sa.Column('fecha_fin', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('categorias',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre_categoria', sa.String(length=80), nullable=False),
    sa.Column('descripcion', sa.Text(), nullable=True),
    sa.Column('id_categoria_padre', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['id_categoria_padre'], ['categorias.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('marcas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre_marca', sa.String(length=80), nullable=False),
    sa.Column('descripcion', sa.Text(), nullable=True),
    sa.Column('sitio_web', sa.String(length=255), nullable=True),
    sa.Column('imagen_url', sa.String(length=255), nullable=False),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('usuarios',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre_usuario', sa.String(length=80), nullable=False),
    sa.Column('contraseña', sa.String(length=200), nullable=False),
    sa.Column('email', sa.String(length=120), nullable=False),
    sa.Column('telefono', sa.String(length=20), nullable=True),
    sa.Column('direccion', sa.String(length=255), nullable=True),
    sa.Column('rol', sa.Enum('cliente', 'administrador', name='roles'), nullable=False),
    sa.Column('fecha_registro', sa.DateTime(), nullable=True),
    sa.Column('fecha_modificacion', sa.DateTime(), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('email'),
    sa.UniqueConstraint('nombre_usuario')
    )
    op.create_table('productos',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('nombre_producto', sa.String(length=80), nullable=False),
    sa.Column('descripcion', sa.Text(), nullable=True),
    sa.Column('precio', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('stock', sa.Integer(), nullable=False),
    sa.Column('peso', sa.Numeric(precision=10, scale=2), nullable=False),
    sa.Column('color', sa.String(length=50), nullable=True),
    sa.Column('volumen', sa.Numeric(precision=10, scale=2), nullable=True),
    sa.Column('id_categoria', sa.Integer(), nullable=False),
    sa.Column('id_marca', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_categoria'], ['categorias.id'], ),
    sa.ForeignKeyConstraint(['id_marca'], ['marcas.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('carrito',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_cliente', sa.Integer(), nullable=False),
    sa.Column('id_producto', sa.Integer(), nullable=False),
    sa.Column('cantidad', sa.Integer(), nullable=False),
    sa.Column('fecha_agregado', sa.DateTime(), nullable=True),
    sa.ForeignKeyConstraint(['id_cliente'], ['usuarios.id'], ),
    sa.ForeignKeyConstraint(['id_producto'], ['productos.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id_cliente', 'id_producto', name='unique_cliente_producto')
    )
    op.create_table('media',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_producto', sa.Integer(), nullable=False),
    sa.Column('tipo_media', sa.String(length=20), nullable=False),
    sa.Column('url', sa.String(length=255), nullable=False),
    sa.Column('descripcion', sa.Text(), nullable=True),
    sa.Column('orden', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['id_producto'], ['productos.id'], ),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('id_producto', 'orden', name='unique_orden_producto')
    )
    op.create_table('reseñas',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('id_producto', sa.Integer(), nullable=False),
    sa.Column('id_cliente', sa.Integer(), nullable=False),
    sa.Column('calificacion', sa.Integer(), nullable=False),
    sa.Column('texto_resena', sa.Text(), nullable=True),
    sa.Column('fecha_resena', sa.DateTime(), nullable=True),
    sa.CheckConstraint('calificacion BETWEEN 1 AND 5', name='check_calificacion_valida'),
    sa.ForeignKeyConstraint(['id_cliente'], ['usuarios.id'], ),
    sa.ForeignKeyConstraint(['id_producto'], ['productos.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('reseñas')
    op.drop_table('media')
    op.drop_table('carrito')
    op.drop_table('productos')
    op.drop_table('usuarios')
    op.drop_table('marcas')
    op.drop_table('categorias')
    op.drop_table('banners')
    # ### end Alembic commands ###
