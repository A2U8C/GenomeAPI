from flask_restful import Resource, abort
from flask import request
from flask_cors import CORS, cross_origin

from collections import OrderedDict

class StatData(Resource):
    def get(self):
        json_info=dict()
        file_name=""
        my_file = open("/ifs/loni/faculty/njahansh/nerds/iyad/CPcal_UKBB/Genetics/BioGen/rs2/cpcal_baseline.log", "r")

        with my_file as f:
            for line in f:
                if line.startswith(("Lambda GC:","Mean Chi^2:","Intercept:","Ratio:")):
                    key_val=line.split(":")
                    json_info[key_val[0]]=key_val[1].rstrip("\n")
                if line.startswith("Results printed to"):
                    file_name=line.split("printed to ")[1]
                    json_info["File_name"]=file_name

        return json_info 

    def post(self):
        json_info=dict()
        file_name=""
        my_file = open("/ifs/loni/faculty/njahansh/nerds/iyad/CPcal_UKBB/Genetics/BioGen/rs2/cpcal_baseline.log", "r")

        with my_file as f:
            for line in f:
                if line.startswith(("Lambda GC:","Mean Chi^2:","Intercept:","Ratio:")):
                    key_val=line.split(":")
                    json_info[key_val[0]]=key_val[1].rstrip("\n")
                if line.startswith("Results printed to"):
                    file_name=line.split("printed to ")[1]
                    json_info["File_name"]=file_name

        return json_info