from flask import Blueprint, request, jsonify
from models import Marca
from schemas.marca_schema import MarcaSchema
from app import db

bp = Blueprint('marca_routes', __name__, url_prefix='/marcas')

marca_schema = MarcaSchema()
marcas_schema = MarcaSchema(many=True)

@bp.route('/', methods=['GET'])
def obtener_marcas():
    marcas = Marca.query.all()
    marcas_data = [
        {
            "nombre_marca": marca.nombre_marca,
            "imagen_url": marca.imagen_url
        }
        for marca in marcas
    ]
    return jsonify(marcas_data), 200

@bp.route('/<int:id>', methods=['GET'])
def obtener_marca(id):
    marca = Marca.query.get_or_404(id)
    marca_data = {
        "nombre_marca": marca.nombre_marca,
        "imagen_url": marca.imagen_url
    }
    return jsonify(marca_data), 200

@bp.route('/', methods=['POST'])
def crear_marca():
    data = request.json
    errors = marca_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    nueva_marca = Marca(
        nombre_marca=data['nombre_marca'],
        descripcion=data.get('descripcion'),
        sitio_web=data.get('sitio_web'),
        imagen_url=data.get('imagen_url')  # Nuevo campo para la URL de la imagen
    )
    db.session.add(nueva_marca)
    db.session.commit()
    return jsonify(marca_schema.dump(nueva_marca)), 201

@bp.route('/<int:id>', methods=['PUT'])
def actualizar_marca(id):
    marca = Marca.query.get_or_404(id)
    data = request.json
    errors = marca_schema.validate(data)
    if errors:
        return jsonify(errors), 400

    marca.nombre_marca = data.get('nombre_marca', marca.nombre_marca)
    marca.descripcion = data.get('descripcion', marca.descripcion)
    marca.sitio_web = data.get('sitio_web', marca.sitio_web)
    marca.imagen_url = data.get('imagen_url', marca.imagen_url)  # Actualización del campo de imagen
    db.session.commit()
    return jsonify(marca_schema.dump(marca)), 200

@bp.route('/<int:id>', methods=['DELETE'])
def eliminar_marca(id):
    marca = Marca.query.get_or_404(id)
    db.session.delete(marca)
    db.session.commit()
    return jsonify({"mensaje": "Marca eliminada exitosamente"}), 200