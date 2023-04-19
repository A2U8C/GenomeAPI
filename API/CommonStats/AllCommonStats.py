import pandas as pd
from flask_restful import Resource, abort
from flask import request
from flask_cors import CORS, cross_origin
from collections import OrderedDict
from ModuleMunge.MungePrep import Munging
from ModuleLDSC.CommonLDSC import HeritabilityLDSC,CellTypeLDSC



class HeritabilityStats(Resource):
    
    def get(self):
        abort(403, message="No results for GET, try using POST")

    def post(self):
        MainFilePath=request.get_json()["file_path"]
        mng=Munging(MainFilePath)
        filesGZ_name="/ifs/loni/faculty/njahansh/nerds/ankush/webApplication_Genome/Git_Genome/GenomeAPI/dbAccess/"+mng.fileName+".sumstats.gz"
        HeriditySummary=HeritabilityLDSC(filesGZ_name)
        
        resultsFilePath="/ifs/loni/faculty/njahansh/nerds/ankush/webApplication_Genome/Git_Genome/GenomeAPI/LDSC_Stats/"+HeriditySummary.statFileName+".results"
        df=pd.read_csv(resultsFilePath,sep="\t").to_json(orient="records")
        
        return df
    

class CellTypeStats(Resource):
    
    def get(self):
        abort(403, message="No results for GET, try using POST")

    def post(self):
        MainFilePath= request.get_json()["file_path"]
        #mng=Munging(MainFilePath)
        #filesGZ_name="/ifs/loni/faculty/njahansh/nerds/ankush/webApplication_Genome/Git_Genome/GenomeAPI/dbAccess/"+mng.fileName+".sumstats.gz"
        filesGZ_name=MainFilePath
        HeriditySummary=CellTypeLDSC(filesGZ_name)

        print("********************************************************************************",HeriditySummary.statFileName)
        
        
        # resultsFilePath="/ifs/loni/faculty/njahansh/nerds/ankush/webApplication_Genome/Git_Genome/GenomeAPI/LDSC_Stats/"+HeriditySummary.statFileName+".results"
        # df=pd.read_csv(resultsFilePath,sep="\t").to_json(orient="records")
        
        # return df

        return r"{'value':'ans'}"