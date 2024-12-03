from flask import Blueprint, jsonify, request
from models import db, Producto, Media

bp = Blueprint('productos', __name__, url_prefix='/tienda/productos')

# Obtener todos los productos junto con sus imágenes
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
                "media": media_data  # Agregar las imágenes asociadas
            }
            productos_data.append(producto_dict)

        return jsonify(productos_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Obtener un producto específico por ID junto con sus imágenes
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
            "media": media_data  # Agregar las imágenes asociadas
        }

        return jsonify(producto_dict), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Crear un nuevo producto
@bp.route('/', methods=['POST'])
def crear_producto():
    try:
        data = request.get_json()

        nuevo_producto = Producto(
            nombre_producto=data.get("nombre_producto"),
            descripcion=data.get("descripcion"),
            precio=data.get("precio"),
            stock=data.get("stock"),
            peso=data.get("peso"),
            color=data.get("color"),
            volumen=data.get("volumen"),
            id_categoria=data.get("id_categoria"),
            id_marca=data.get("id_marca")
        )
        db.session.add(nuevo_producto)
        db.session.commit()

        return jsonify({"mensaje": "Producto creado exitosamente", "id": nuevo_producto.id}), 201
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Actualizar un producto existente
@bp.route('/<int:id>', methods=['PUT'])
def actualizar_producto(id):
    try:
        producto = Producto.query.get_or_404(id)
        data = request.get_json()

        producto.nombre_producto = data.get("nombre_producto", producto.nombre_producto)
        producto.descripcion = data.get("descripcion", producto.descripcion)
        producto.precio = data.get("precio", producto.precio)
        producto.stock = data.get("stock", producto.stock)
        producto.peso = data.get("peso", producto.peso)
        producto.color = data.get("color", producto.color)
        producto.volumen = data.get("volumen", producto.volumen)
        producto.id_categoria = data.get("id_categoria", producto.id_categoria)
        producto.id_marca = data.get("id_marca", producto.id_marca)

        db.session.commit()

        return jsonify({"mensaje": "Producto actualizado exitosamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Eliminar un producto
@bp.route('/<int:id>', methods=['DELETE'])
def eliminar_producto(id):
    try:
        producto = Producto.query.get_or_404(id)
        db.session.delete(producto)
        db.session.commit()

        return jsonify({"mensaje": "Producto eliminado exitosamente"}), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500
