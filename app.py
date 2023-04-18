my_file = open("/ifs/loni/faculty/njahansh/nerds/iyad/CPcal_UKBB/Genetics/BioGen/rs2/cpcal_baseline.log", "r")
# print(my_file.read())



from flask import Flask
from flask_restful import Api
from flask_cors import CORS, cross_origin
import pandas as pd
from API.FinalData import StatData
from ModuleMunge.MungePrep import Munging
from ModuleLDSC.CommonLDSC import HeritabilityLDSC
from API.CommonStats.AllCommonStats import HeritabilityStats,CellTypeStats

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

api.add_resource(HeritabilityStats, '/file_info')
api.add_resource(CellTypeStats, '/analysis_info')

'''
# file_name="/ifs/loni/faculty/njahansh/nerds/iyad/CPcal_UKBB/Genetics/BioGen/rs2/discovery_chr6_Third_Ventricle_CPcal_log.regenie"
# file_name="/ifs/loni/faculty/njahansh/nerds/ankush/webApplication_Genome/Git_Genome/GenomeAPI/RegenieTextData/test_cc_ukbb_white_Center_Angle.txt"
# file_name="/ifs/loni/faculty/njahansh/nerds/iyad/CPcal_UKBB/Genetics/BioGen/rs2/Total_CPCal_all.txt"

# mng=Munging(file_name)

# filesGZ_name="/ifs/loni/faculty/njahansh/nerds/ankush/webApplication_Genome/Git_Genome/GenomeAPI/dbAccess/"+mng.fileName+".sumstats.gz"
# filesGZ_name="/ifs/loni/faculty/njahansh/nerds/iyad/CPcal_UKBB/Genetics/BioGen/rs2/cpcal_munged.sumstats.gz"
# HeriditySummary=HeritabilityLDSC(filesGZ_name)
# print(HeriditySummary.statFileName)

# resultsFilePath="/ifs/loni/faculty/njahansh/nerds/ankush/webApplication_Genome/Git_Genome/GenomeAPI/LDSC_Stats/LDSC_Stats_discovery_chr6_Third_Ventricle_CPcal_log.sumstats.results"
# df=pd.read_csv(resultsFilePath,sep="\t")
# print(df.columns)
# print(df.to_json(orient="records"))
'''


# HeritVari=HeritabilityStats()
# print(HeritVari.post(file_name))

if __name__ == "__main__":  
    app.run(host="0.0.0.0", debug=True)