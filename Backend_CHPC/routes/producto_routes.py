from flask import Blueprint, jsonify, request
from models import db, Producto, Media, Reseña

bp = Blueprint('productos', __name__, url_prefix='/tienda/productos')

# Obtener todos los productos junto con sus imágenes y reseñas
@bp.route('/', methods=['GET'])
def obtener_productos():
    try:
        productos = Producto.query.all()
        productos_data = []

        for producto in productos:
            # Obtener las imágenes asociadas al producto
            media_productos = Media.query.filter_by(id_producto=producto.id).all()
            media_data = [
                {
                    "id": media.id,
                    "tipo_media": media.tipo_media,
                    "url": media.url,
                    "descripcion": media.descripcion,
                    "orden": media.orden
                }
                for media in media_productos
            ]

            # Obtener las reseñas asociadas al producto
            reseñas_producto = Reseña.query.filter_by(id_producto=producto.id).all()
            reseñas_data = [
                {
                    "id": reseña.id,
                    "calificacion": reseña.calificacion,
                    "texto_resena": reseña.texto_resena,
                    "fecha_resena": reseña.fecha_resena.isoformat(),
                    "cliente": {
                        "id": reseña.id_cliente,  # O más detalles si son accesibles
                        "nombre_usuario": reseña.cliente.nombre_usuario if reseña.cliente else "Anónimo"
                    }
                }
                for reseña in reseñas_producto
            ]

            # Construir el diccionario del producto
            producto_dict = {
                "id": producto.id,
                "nombre_producto": producto.nombre_producto,
                "descripcion": producto.descripcion,
                "precio": str(producto.precio),
                "stock": producto.stock,
                "peso": str(producto.peso),
                "color": producto.color,
                "volumen": str(producto.volumen) if producto.volumen else None,
                "id_categoria": producto.id_categoria,
                "id_marca": producto.id_marca,
                "media": media_data,
                "reseñas": reseñas_data  # Agregar las reseñas asociadas
            }
            productos_data.append(producto_dict)

        return jsonify(productos_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Obtener un producto específico por ID junto con sus imágenes y reseñas
@bp.route('/<int:id>', methods=['GET'])
def obtener_producto(id):
    try:
        producto = Producto.query.get_or_404(id)

        # Obtener las imágenes asociadas al producto
        media_productos = Media.query.filter_by(id_producto=producto.id).all()
        media_data = [
            {
                "id": media.id,
                "tipo_media": media.tipo_media,
                "url": media.url,
                "descripcion": media.descripcion,
                "orden": media.orden
            }
            for media in media_productos
        ]

        # Obtener las reseñas asociadas al producto
        reseñas_producto = Reseña.query.filter_by(id_producto=producto.id).all()
        reseñas_data = [
            {
                "id": reseña.id,
                "calificacion": reseña.calificacion,
                "texto_resena": reseña.texto_resena,
                "fecha_resena": reseña.fecha_resena.isoformat(),
                "cliente": {
                    "id": reseña.id_cliente,  # O más detalles si son accesibles
                    "nombre_usuario": reseña.cliente.nombre_usuario if reseña.cliente else "Anónimo"
                }
            }
            for reseña in reseñas_producto
        ]

        # Construir el diccionario del producto
        producto_dict = {
            "id": producto.id,
            "nombre_producto": producto.nombre_producto,
            "descripcion": producto.descripcion,
            "precio": str(producto.precio),
            "stock": producto.stock,
            "peso": str(producto.peso),
            "color": producto.color,
            "volumen": str(producto.volumen) if producto.volumen else None,
            "id_categoria": producto.id_categoria,
            "id_marca": producto.id_marca,
            "media": media_data,
            "reseñas": reseñas_data  # Agregar las reseñas asociadas
        }

        return jsonify(producto_dict), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
