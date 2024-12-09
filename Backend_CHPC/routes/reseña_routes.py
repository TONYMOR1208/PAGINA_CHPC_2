from flask import Blueprint, jsonify, request
from models import db, Reseña, Producto, Usuario
from datetime import datetime

reseña_routes = Blueprint('reseñas', __name__, url_prefix='/tienda/reseñas')

# Obtener reseñas filtradas por ID del producto con información del cliente y producto
@reseña_routes.route('/', methods=['GET'])
def obtener_reseñas_por_producto():
    try:
        id_producto = request.args.get('producto', type=int)  # Obtener el ID del producto desde los parámetros
        if not id_producto:
            return jsonify({"error": "Falta el parámetro 'producto'."}), 400

        # Filtrar reseñas por ID del producto
        reseñas = Reseña.query.filter_by(id_producto=id_producto).all()
        reseñas_data = [
            {
                "id": reseña.id,
                "calificacion": reseña.calificacion,
                "texto_resena": reseña.texto_resena,
                "fecha_resena": reseña.fecha_resena.isoformat(),
                "cliente": {
                    "id": reseña.cliente.id,
                    "nombre_usuario": reseña.cliente.nombre_usuario
                } if reseña.cliente else {"id": None, "nombre_usuario": "Anónimo"}
            }
            for reseña in reseñas
        ]
        return jsonify(reseñas_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Obtener una reseña específica por su ID con información del cliente y producto
@reseña_routes.route('/<int:id>', methods=['GET'])
def obtener_reseña(id):
    try:
        reseña = Reseña.query.get_or_404(id)
        reseña_data = {
            "id": reseña.id,
            "calificacion": reseña.calificacion,
            "texto_resena": reseña.texto_resena,
            "fecha_resena": reseña.fecha_resena.isoformat(),
            "cliente": {
                "id": reseña.cliente.id,
                "nombre_usuario": reseña.cliente.nombre_usuario
            } if reseña.cliente else {"id": None, "nombre_usuario": "Anónimo"},
            "producto": {
                "id": reseña.producto.id,
                "nombre_producto": reseña.producto.nombre_producto
            } if reseña.producto else {"id": None, "nombre_producto": "Desconocido"}
        }
        return jsonify(reseña_data), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Crear una nueva reseña
@reseña_routes.route('/', methods=['POST'])
def crear_reseña():
    try:
        datos = request.json

        # Validar datos recibidos
        if not datos.get('id_producto') or not datos.get('id_cliente'):
            return jsonify({"error": "Faltan campos obligatorios (id_producto, id_cliente)."}), 400

        if not datos.get('calificacion') or not isinstance(datos['calificacion'], (int, float)):
            return jsonify({"error": "El campo 'calificacion' es obligatorio y debe ser un número."}), 400

        # Verificar si el producto y cliente existen
        producto = Producto.query.get(datos['id_producto'])
        cliente = Usuario.query.get(datos['id_cliente'])

        if not producto:
            return jsonify({"error": "El producto especificado no existe."}), 404
        if not cliente:
            return jsonify({"error": "El cliente especificado no existe."}), 404

        nueva_reseña = Reseña(
            id_producto=datos['id_producto'],
            id_cliente=datos['id_cliente'],
            calificacion=datos['calificacion'],
            texto_resena=datos.get('texto_resena'),  # Campo opcional
            fecha_resena=datetime.utcnow()
        )
        db.session.add(nueva_reseña)
        db.session.commit()

        return jsonify({
            "message": "Reseña creada exitosamente",
            "id": nueva_reseña.id,
            "calificacion": nueva_reseña.calificacion,
            "texto_resena": nueva_reseña.texto_resena,
            "fecha_resena": nueva_reseña.fecha_resena.isoformat()
        }), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400


# Actualizar una reseña existente
@reseña_routes.route('/<int:id>', methods=['PUT'])
def actualizar_reseña(id):
    try:
        datos = request.json
        reseña = Reseña.query.get_or_404(id)

        # Actualizar solo los campos válidos
        reseña.calificacion = datos.get('calificacion', reseña.calificacion)
        reseña.texto_resena = datos.get('texto_resena', reseña.texto_resena)
        reseña.fecha_resena = datetime.utcnow()  # Actualiza la fecha de modificación

        db.session.commit()
        return jsonify({"message": "Reseña actualizada exitosamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 400


# Eliminar una reseña
@reseña_routes.route('/<int:id>', methods=['DELETE'])
def eliminar_reseña(id):
    try:
        reseña = Reseña.query.get_or_404(id)
        db.session.delete(reseña)
        db.session.commit()
        return jsonify({"message": "Reseña eliminada exitosamente"}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500
