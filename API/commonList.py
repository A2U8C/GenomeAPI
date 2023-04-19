import pandas as pd
from flask_restful import Resource, abort
from flask import request
from flask_cors import CORS, cross_origin
from collections import OrderedDict
from ModuleMunge.MungePrep import Munging
from ModuleLDSC.CommonLDSC import HeritabilityLDSC,CellTypeLDSC
from constants import PROCESSED_FILES
import pandas as pd
import numpy as np
import statsmodels.stats.multitest as multi
from flask import request
import glob


class listLDSCFiles(Resource):
    def get(self):
        abort(403, message="No results for GET, try using POST")

    def post(self):
        
        files = glob.glob('/ifs/loni/faculty/njahansh/GAMBIT/genome_WebApplication/static/LDSC_Stats/*_*.sumstats.cell_type_results.txt')
        
        return files


        # LDSCCellTypeFiles = glob.glob('/ifs/loni/faculty/njahansh/GAMBIT/genome_WebApplication/static/LDSC_Stats/[a-zA-z]_*.sumstats.cell_type_results.txt')
        # return LDSCCellTypeFiles
    

class plotLDSC(Resource):
    def get(self):
        abort(403, message="No results for GET, try using POST")

    def post(self):
        
        body=request.get_json()
        AnalysisFilePath=body["file_path"]
        fName=AnalysisFilePath.split("/")[-1]

        if fName.split("_")[0]=="chromatin":
            df=pd.read_csv(AnalysisFilePath,sep="\t")
            df.rename(columns={"Name":"Name__Mark"},inplace=True)
            df[["Name","Mark"]]=df["Name__Mark"].str.split("__", expand=True)
            df["Entex"]=df["Name"].str.contains("ENTEX").map({True:"Yes",False:"No"})
            _,df["FDRCorrectP"]=multi.fdrcorrection(df["Coefficient_P_value"])
            df["-LOG10P"]=-1*np.log10(df["Coefficient_P_value"])

            df_key=pd.read_csv("/ifs/loni/faculty/njahansh/nerds/ankush/webApplication_Genome/Git_Genome/GenomeAPI/ldsc/ldsc/chromatin_key.csv")
            df_merged=pd.merge(df,df_key,on=['Name',"Mark","Entex"],how='inner').sort_values(by=["Tissue"]).to_dict(orient="list")
            return df_merged

        elif fName.split("_")[0]=="gene":
            df_gene=pd.read_csv(AnalysisFilePath,sep="\t")
            df_gene["-LOG10P"]=-1*np.log10(df_gene["Coefficient_P_value"])
            _,df_gene["FDRCorrectP"]=multi.fdrcorrection(df_gene["Coefficient_P_value"])
            df_gene["-LOG10P"]=-1*np.log10(df_gene["Coefficient_P_value"])
            df_gene_key=pd.read_csv("/ifs/loni/faculty/njahansh/nerds/ankush/webApplication_Genome/Git_Genome/GenomeAPI/ldsc/ldsc/gene_expr.csv")
            df_gene_key.rename(columns={"x":"Name"},inplace=True)
            df_merged_gene=pd.merge(df_gene,df_gene_key,left_on=['Name'],right_on=["Name"],how='inner').sort_values(by=["Tissue"])
            df_merged_gene["Marker_size"]=df_merged_gene['FDRCorrectP'].apply(lambda y: 2 if y < 0.05 else 1)
            
            return df_merged_gene.to_dict(orient="list")
        
        elif fName.split("_")[0]=="cahoy":
            df_cahoy=pd.read_csv(AnalysisFilePath,sep="\t")
            df_cahoy["-LOG10P"]=-1*np.log10(df_cahoy["Coefficient_P_value"])

            _,df_cahoy["FDRCorrectP"]=multi.fdrcorrection(df_cahoy["Coefficient_P_value"])
            df_cahoy["Marker_size"]=df_cahoy['FDRCorrectP'].apply(lambda y: 2 if y < 0.05 else 1)
            
            return df_cahoy.to_dict(orient="list")
        
        elif fName.split("_")[0]=="gtexbrain":
            df_brain=pd.read_csv(AnalysisFilePath,sep="\t")
            df_brain["Name"]=df_brain["Name"].str.lstrip("Brain_")
            df_brain["Name"]=df_brain["Name"].str.replace("_"," ")
            df_brain["-LOG10P"]=-1*np.log10(df_brain["Coefficient_P_value"])
            _,df_brain["FDRCorrectP"]=multi.fdrcorrection(df_brain["Coefficient_P_value"])
            df_brain["Marker_size"]=df_brain['FDRCorrectP'].apply(lambda y: 2 if y < 0.05 else 1)
            return df_brain.to_dict(orient="list")
        

        elif fName.split("_")[0]=="immgen":
            df_immgen=pd.read_csv(AnalysisFilePath,sep="\t")
            df_immgen_key=pd.read_csv("ldsc/ldsc/immune_key.csv")
            df_immgen_key.rename(columns={"Cell type":"Name"},inplace=True)
            df_immgen_merged=pd.merge(df_immgen,df_immgen_key,on=['Name'],how='inner').sort_values(by=["Cell type category for display"])
            df_immgen_merged=df_immgen_merged.drop_duplicates()
            df_immgen_merged.rename(columns={"Cell type category for t-statistic":"celltype1","Cell type category for display":"celltype2"},inplace=True)
            df_immgen_merged["-LOG10P"]=-1*np.log10(df_immgen_merged["Coefficient_P_value"])
            df_immgen_merged["celltype1"]=df_immgen_merged["celltype1"].str.replace("_"," ")
            _,df_immgen_merged["FDRCorrectP"]=multi.fdrcorrection(df_immgen_merged["Coefficient_P_value"])
            df_immgen_merged["Marker_size"]=df_immgen_merged['FDRCorrectP'].apply(lambda y: 2 if y < 0.05 else 1)

            return df_immgen_merged.to_dict(orient="list")

        elif fName.split("_")[0]=="corces":
            df_corces=pd.read_csv(AnalysisFilePath,sep="\t")
            df_corces["-LOG10P"]=-1*np.log10(df_corces["Coefficient_P_value"])
            _,df_corces["FDRCorrectP"]=multi.fdrcorrection(df_corces["Coefficient_P_value"])
            df_corces["Marker_size"]=df_corces['FDRCorrectP'].apply(lambda y: 2 if y < 0.05 else 1)

            
            return df_corces.to_dict(orient="list")
        

        else:
            return []


        # LDSCCellTypeFiles = glob.glob('/ifs/loni/faculty/njahansh/GAMBIT/genome_WebApplication/static/LDSC_Stats/[a-zA-z]_*.sumstats.cell_type_results.txt')
        # return LDSCCellTypeFiles