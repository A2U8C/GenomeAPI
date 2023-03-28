my_file = open("/ifs/loni/faculty/njahansh/nerds/iyad/CPcal_UKBB/Genetics/BioGen/rs2/cpcal_baseline.log", "r")
# print(my_file.read())



from flask import Flask
from flask_restful import Api
from flask_cors import CORS #, cross_origin

from constants import UPLOAD_FOLDER
from API.FileUploader import FileUploader

app = Flask(__name__)
cors = CORS(app)

# Configurations 
app.config['CORS_HEADERS'] = 'Content-Type'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
app.config['MAX_CONTENT_LENGTH'] = 16 * 1024 * 1024


api = Api(app)

# api.add_resource(CohortList,'/cohorts') #Done
api.add_resource(FileUploader,'/upload')

if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)































