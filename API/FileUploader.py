from flask_restful import Resource
from constants import UPLOAD_FOLDER
from flask import request, jsonify
from werkzeug.utils import secure_filename


ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif',"zip"])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class FileUploader(Resource):
    def get(self):
        return "Upload"
    
    def post(self):
        # check if the post request has the file part
        if 'files' not in request.files:
            resp = jsonify({'message' : 'No file part in the request'})
            resp.status_code = 400
            return resp
        files = request.files.getlist('files')

        errors = {}
        success = False

        # Check all files and Upload if no errors 
        for file in files:
            
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(UPLOAD_FOLDER + "/" + filename)
                success = True
            else:
                errors[file.filename] = 'File type not allowed'
             

        if success and errors:
            errors['message'] = "Files(s) uploaded succesfully"
            resp = jsonify(errors)
            resp.status_code = 500
            return resp

        if success:
            resp = jsonify({'message':'File(s) Uploaded succesfully'})
            resp.status_code = 201
            return resp
    
        else:
            resp = jsonify(errors)
            resp.status_code = 500
            return resp