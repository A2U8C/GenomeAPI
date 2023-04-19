import pandas as pd
from flask_restful import Resource, abort
from flask import request
from flask_cors import CORS, cross_origin
from collections import OrderedDict
from constants import PROCESSED_FILES

import subprocess

class Munging(Resource):
    def __init__(self, filePathInp:str):
        self.filepath=""
        self.fileName=""
        if filePathInp.split("/")[-1].split(".")[1].lower()=="regenie":
            self.prepFromRegenie(filePathInp)
        else:
            self.filepath=filePathInp
            self.fileName=filePathInp.split("/")[-1].split(".")[0]

        # cmd_line="/ifs/loni/faculty/njahansh/nerds/ankush/software/Anaconda/envs/ldsc/bin/python2.7 \
        #       /ifs/loni/faculty/njahansh/nerds/ankush/webApplication_Genome/Git_Genome/GenomeAPI/ldsc/munge_sumstats.py \
        #     --sumstats "+ self.filepath +" \
        #     --out dbAccess/"+self.fileName+" \
        #     --merge-alleles /ifs/loni/faculty/njahansh/nerds/ravi/genetics/ldsc/eur_w_ld_chr/w_hm3.snplist \
        #     --snp ID \
        #     --a1 ALLELE1 \
        #     --a2 ALLELE0 \
        #     --chunksize 500000"
        
        cmd_line="/ifs/loni/faculty/njahansh/nerds/ankush/software/Anaconda/envs/ldsc/bin/python2.7 \
              /ifs/loni/faculty/njahansh/nerds/ankush/webApplication_Genome/Git_Genome/GenomeAPI/ldsc/munge_sumstats.py \
            --sumstats "+ self.filepath +" \
            --out "+PROCESSED_FILES+"MungedData/"+self.fileName+" \
            --merge-alleles /ifs/loni/faculty/njahansh/nerds/ravi/genetics/ldsc/eur_w_ld_chr/w_hm3.snplist \
            --snp ID \
            --a1 ALLELE1 \
            --a2 ALLELE0 \
            --chunksize 500000"


        subprocess.call(cmd_line, shell=True)

    def prepFromRegenie(self, filePathInp:str):
        df_old= pd.read_csv(filePathInp, sep=" ")
        df_old["P"]=(1/10)**df_old["LOG10P"]
        self.fileName=filePathInp.split("/")[-1].split(".")[0]
        if "EXTRA" in df_old.columns:
            df_old["EXTRA"]=df_old["EXTRA"].fillna("NA")
        # path = r'/ifs/loni/faculty/njahansh/nerds/ankush/webApplication_Genome/Git_Genome/GenomeAPI/RegenieTextData/'+self.fileName+".txt"
        path = PROCESSED_FILES+'/RegenieTextData/'+self.fileName+".txt"
        df_old.to_csv(path, sep="\t",index=False)
        self.filepath=path


        
