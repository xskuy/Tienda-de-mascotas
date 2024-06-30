import os

media_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'media')

if not os.path.exists(media_dir):
    os.makedirs(media_dir)
    print(f"Directorio 'media' creado en {media_dir}")
else:
    print(f"El directorio 'media' ya existe en {media_dir}")