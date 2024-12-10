from flask import Blueprint, jsonify, request
from marshmallow import ValidationError
from schemas.reseña_schema import reseña_schema, reseñas_schema
from models import db, Reseña, Producto, Usuario
from datetime import datetime

reseña_routes = Blueprint('reseñas', __name__, url_prefix='/tienda/reseñas')


# Obtener todas las reseñas o filtrar por ID del producto
@reseña_routes.route('/', methods=['GET'])
def obtener_reseñas():
    try:
        id_producto = request.args.get('producto', type=int)  # Parámetro opcional

        if id_producto:
            reseñas = Reseña.query.filter_by(id_producto=id_producto).all()
        else:
            reseñas = Reseña.query.all()

        return jsonify(reseñas_schema.dump(reseñas)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Obtener una reseña específica por ID
@reseña_routes.route('/<int:id>', methods=['GET'])
def obtener_reseña_por_id(id):
    try:
        reseña = Reseña.query.get_or_404(id)
        return jsonify(reseña_schema.dump(reseña)), 200
    except Exception as e:
        return jsonify({"error": str(e)}), 500


# Crear una nueva reseña
@reseña_routes.route('/', methods=['POST'])
def crear_reseña():
    try:
        datos = request.json

        # Validar entrada con el esquema
        datos_validados = reseña_schema.load(datos)

        # Verificar si el producto y cliente existen
        producto = Producto.query.get(datos_validados['id_producto'])
        cliente = Usuario.query.get(datos_validados['id_cliente'])

        if not producto:
            return jsonify({"error": "El producto especificado no existe."}), 404
        if not cliente:
            return jsonify({"error": "El cliente especificado no existe."}), 404

        nueva_reseña = Reseña(
            id_producto=datos_validados['id_producto'],
            id_cliente=datos_validados['id_cliente'],
            calificacion=datos_validados['calificacion'],
            texto_resena=datos_validados.get('texto_resena'),
            fecha_resena=datetime.utcnow()
        )
        db.session.add(nueva_reseña)
        db.session.commit()

        return jsonify(reseña_schema.dump(nueva_reseña)), 201
    except ValidationError as ve:
        return jsonify({"error": ve.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


# Actualizar una reseña existente
@reseña_routes.route('/<int:id>', methods=['PUT'])
def actualizar_reseña(id):
    try:
        datos = request.json

        reseña = Reseña.query.get_or_404(id)

        # Validar entrada con el esquema
        datos_validados = reseña_schema.load(datos, partial=True)

        # Actualizar campos
        reseña.calificacion = datos_validados.get('calificacion', reseña.calificacion)
        reseña.texto_resena = datos_validados.get('texto_resena', reseña.texto_resena)
        reseña.fecha_resena = datetime.utcnow()

        db.session.commit()
        return jsonify(reseña_schema.dump(reseña)), 200
    except ValidationError as ve:
        return jsonify({"error": ve.messages}), 400
    except Exception as e:
        db.session.rollback()
        return jsonify({"error": str(e)}), 500


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
