my_file = open("/ifs/loni/faculty/njahansh/nerds/iyad/CPcal_UKBB/Genetics/BioGen/rs2/cpcal_baseline.log", "r")
print(my_file.read())



from flask import Flask
from flask_restful import Api

from flask_cors import CORS, cross_origin


app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'
api = Api(app)

# api.add_resource(CohortList,'/cohorts') #Done

if __name__ == "__main__":
    app.run(debug=True)































