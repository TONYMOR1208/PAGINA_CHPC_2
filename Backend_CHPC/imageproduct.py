import os
from app import app, db
from models import Media, Producto  # Asegúrate de importar el modelo Producto si lo necesitas

# Ruta donde están almacenadas las imágenes (dentro de 'static/AimaPro')
static_folder = os.path.join(app.root_path, 'static', 'AimaPro')

# Asegurarse de que la carpeta existe
if not os.path.exists(static_folder):
    print(f"La carpeta {static_folder} no existe. Creándola...")
    os.makedirs(static_folder)

# Filtrar solo archivos de imágenes válidas
imagenes = [img for img in os.listdir(static_folder) if img.lower().endswith(('.png', '.jpg', '.jpeg', '.gif'))]

try:
    with app.app_context():
        # Obtener las URLs de imágenes ya existentes en la base de datos
        urls_existentes = {media.url for media in db.session.query(Media.url).all()}
        
        # Identificar nuevas imágenes para insertar
        nuevas_imagenes = [img for img in imagenes if f"/AimaPro/{img}" not in urls_existentes]
        
        if nuevas_imagenes:
            for idx, imagen in enumerate(nuevas_imagenes):
                print(f"\nProcesando la imagen: {imagen}")
                
                # Solicitar datos al usuario
                try:
                    id_producto = int(input("Ingrese el ID del producto al que pertenece esta imagen: "))
                    
                    # Validar que el producto exista
                    producto = db.session.query(Producto).filter_by(id=id_producto).first()
                    if not producto:
                        print(f"El producto con ID {id_producto} no existe. Saltando esta imagen.")
                        continue
                    
                    tipo_media = input("Ingrese el tipo de media (imagen/video): ").strip().lower()
                    if tipo_media not in ["imagen", "video"]:
                        print("Tipo de media no válido. Debe ser 'imagen' o 'video'. Saltando esta imagen.")
                        continue
                    
                    descripcion = input(f"Ingrese una descripción para '{imagen}' (opcional): ").strip() or None
                    orden = input(f"Ingrese el orden para '{imagen}' (opcional, predeterminado 0): ").strip()
                    orden = int(orden) if orden.isdigit() else 0

                    # Crear la URL relativa para la base de datos
                    imagen_url = f"/AimaPro/{imagen}"
                    
                    # Crear un nuevo registro de media
                    nueva_media = Media(
                        id_producto=id_producto,
                        tipo_media=tipo_media,
                        url=imagen_url,
                        descripcion=descripcion,
                        orden=orden
                    )
                    
                    # Insertar en la base de datos
                    db.session.add(nueva_media)
                
                except ValueError as e:
                    print(f"Entrada inválida: {e}. Saltando esta imagen.")
                except Exception as e:
                    print(f"Error procesando la imagen '{imagen}': {e}")
            
            # Confirmar los cambios en la base de datos
            db.session.commit()
            print(f"\nSe han insertado {len(nuevas_imagenes)} nuevas imágenes en la base de datos.")
        else:
            print("No hay nuevas imágenes para insertar.")
except Exception as e:
    print(f"Error al procesar las entradas en Media: {e}")
