from flask import jsonify
import cloudinary


def photos_route():
    try:
        resources = cloudinary.Search().expression('folder:photos').execute()
        urls = [resource['secure_url'] for resource in resources['resources']]
        return jsonify(urls)
    except Exception as e:
        print('Error fetching photos:', e)
        return 'Error fetching photos', 500
