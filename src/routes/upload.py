import os
from flask import request, jsonify
import cloudinary
import cloudinary.uploader
from werkzeug.utils import secure_filename

# Configuração do Cloudinary
cloudinary_cloud_name = os.getenv('CLOUDINARY_CLOUD_NAME')
cloudinary_api_key = os.getenv('CLOUDINARY_API_KEY')
cloudinary_api_secret = os.getenv('CLOUDINARY_API_SECRET')

if cloudinary_cloud_name and cloudinary_api_key and cloudinary_api_secret:
    cloudinary.config(
        cloud_name=cloudinary_cloud_name,
        api_key=cloudinary_api_key,
        api_secret=cloudinary_api_secret,
        secure=True
    )
else:
    raise Exception("Erro: Chaves do Cloudinary não configuradas.")


def upload_route():
    if 'photo' not in request.files:
        return jsonify({"error": "No file part"}), 400

    file = request.files['photo']

    if file.filename == '':
        return jsonify({"error": "No selected file"}), 400

    if file:
        try:
            # Secure the filename
            filename = secure_filename(file.filename)

            # Remove any existing extension from the filename
            filename_without_ext = os.path.splitext(filename)[0]

            # Upload the file to Cloudinary in the 'photos' folder
            upload_result = cloudinary.uploader.upload(
                file,
                folder='photos/',
                public_id=filename_without_ext,
                resource_type="image"
            )
            return jsonify({"url": upload_result["secure_url"]}), 200
        except Exception as e:
            return jsonify({"error": str(e)}), 500

    return jsonify({"error": "Invalid request"}), 400
