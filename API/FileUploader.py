from flask_restful import Resource
from constants import UPLOAD_FOLDER
from flask import request, make_response
from werkzeug.utils import secure_filename

import os
import logging

log = logging.getLogger(__name__)
logging.basicConfig(level=logging.DEBUG, format="%(levelname)s:%(name)s:%(message)s")

ALLOWED_EXTENSIONS = set(['txt', 'pdf', 'png', 'jpg', 'jpeg', 'gif',"zip", "regenie"])

def allowed_file(filename):
	return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


class FileUploader(Resource):
    def get(self):
        return make_response(("GET NOT ALLOWED, TRY POST", 405))
    
    def post(self):

        # Get Args from request
        file = request.files.get('file')
        id = request.form.get('uuid')
        offset = int(request.form.get("chunkOffset"))
        chunkIndex = int(request.form.get("chunkIndex"))
        totalChunks = int(request.form.get("totalCount"))
        fileSize = int(request.form.get("fileSize") )

        filename =  secure_filename(file.filename)
        save_path = os.path.join(UPLOAD_FOLDER, filename)
        

        # Check if file exsists, if true return
        if os.path.exists(save_path) and chunkIndex == 0:
             return make_response(("File Already exsist", 400))
        
        # Check if file format is acceptable
        if not allowed_file(filename):
             extension = filename.rsplit('.',1)[1]
             return make_response((f"File Type not Allowed. File recieved of type {extension}", 400))
        
        # Open file and write
        try:
            with open(save_path, 'ab') as f:
                f.seek(offset)
                f.write(file.stream.read())
        except OSError:
             
             # Delete the file at path 
             os.remove(save_path)
             log.exception(f'Unable to write file. Error: \n {OSError.with_traceback()}')

             # Return Response
             return make_response(("An unknown error occured. Cannot write file.", 500))

        # Check if file size is equal to intended file
        if chunkIndex + 1 == totalChunks:
             if size := os.path.getsize(save_path) != fileSize:
                  log.error(f'File {filename} completed, but file size does not match. Expected {fileSize}, recieved {size}')
                  os.remove(save_path)
                  return make_response(("Size mismatch, please re-upload", 500))
             else:
                  log.info(f'File {filename} uploaded succesfully')
                  temp_name = filename if len(filename) < 20 else filename[:20] + "..."
                  return  make_response((f"File {temp_name} uploaded Succesfully!", 200))
        else:
             log.debug(f'Uploading chunk {chunkIndex} of {totalChunks}')
             return make_response((f'Uploading chunk {chunkIndex} of {totalChunks}',102))