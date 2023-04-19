import pandas as pd
from flask_restful import Resource, abort
from flask import request
from flask_cors import CORS, cross_origin
from collections import OrderedDict
from constants import PROCESSED_FILES

import subprocess

class HeritabilityLDSC(Resource):
    def __init__(self,filesName:str):
        
        fileNamesList=filesName.split(" ")
        all_files=",".join(fileNamesList)

        if len(fileNamesList)>1:
            fileOutName="MultiFileOut"
        else:
            fileOutName="LDSC_Stats_"+fileNamesList[0].split("/")[-1].split(".gz")[0]
        
        # cmd_line="/ifs/loni/faculty/njahansh/nerds/ankush/software/Anaconda/envs/ldsc/bin/python2.7 \
        #     /ifs/loni/faculty/njahansh/nerds/ankush/webApplication_Genome/Git_Genome/GenomeAPI/ldsc/ldsc.py \
        #     --h2 "+all_files+" --ref-ld-chr /ifs/loni/faculty/njahansh/nerds/ravi/genetics/ldsc/1000G_EUR_Phase3_baseline/baseline.\
        #     --out LDSC_Stats/"+fileOutName+" --overlap-annot \
        #     --frqfile-chr /ifs/loni/faculty/njahansh/nerds/ravi/genetics/ldsc/1000G_Phase3_frq/1000G.EUR.QC. \
        #     --w-ld-chr /ifs/loni/faculty/njahansh/nerds/ravi/genetics/ldsc/weights_hm3_no_hla/weights."
        

        cmd_line="/ifs/loni/faculty/njahansh/nerds/ankush/software/Anaconda/envs/ldsc/bin/python2.7 \
            /ifs/loni/faculty/njahansh/nerds/ankush/webApplication_Genome/Git_Genome/GenomeAPI/ldsc/ldsc.py \
            --h2 "+all_files+" \
            --ref-ld-chr /ifs/loni/faculty/njahansh/nerds/ravi/genetics/ldsc/1000G_EUR_Phase3_baseline/baseline.\
            --out "+PROCESSED_FILES+"LDSC_Stats/"+fileOutName+" \
            --overlap-annot \
            --frqfile-chr /ifs/loni/faculty/njahansh/nerds/ravi/genetics/ldsc/1000G_Phase3_frq/1000G.EUR.QC. \
            --w-ld-chr /ifs/loni/faculty/njahansh/nerds/ravi/genetics/ldsc/weights_hm3_no_hla/weights."
        


#--out /ifs/loni/faculty/njahansh/GAMBIT/genome_WebApplication/static/LDSC_Stats/"+fileOutName+" 


        self.statFileName=fileOutName
        subprocess.call(cmd_line, shell=True)



class CellTypeLDSC(Resource):
    def __init__(self,filesName:str):
        
        fileNamesList=filesName.split(" ")
        all_files=",".join(fileNamesList)

        if len(fileNamesList)>1:
            fileOutName="MultiFileOut"
        else:
            fileOutName="LDSC_CellType_"+fileNamesList[0].split("/")[-1].split(".gz")[0]
        
        # cmd_line_n="/ifs/loni/faculty/njahansh/nerds/ankush/software/Anaconda/envs/ldsc/bin/python2.7 \
        # /ifs/loni/faculty/njahansh/nerds/ankush/webApplication_Genome/Git_Genome/GenomeAPI/ldsc/ldsc.py \
        # --h2-cts "+all_files+" \
        # --ref-ld-chr /ifs/loni/faculty/njahansh/nerds/ravi/genetics/ldsc/1000G_EUR_Phase3_baseline/baseline. \
        # --out LDSC_Stats/"+fileOutName+" \
        # --ref-ld-chr-cts /ifs/loni/faculty/njahansh/nerds/ravi/genetics/ldsc/ldsc_seg_ldscores/Corces_ATAC.ldcts \
        # --w-ld-chr /ifs/loni/faculty/njahansh/nerds/ravi/genetics/ldsc/weights_hm3_no_hla/weights."
        

        cmd_line_n="/ifs/loni/faculty/njahansh/nerds/ankush/software/Anaconda/envs/ldsc/bin/python2.7 \
        /ifs/loni/faculty/njahansh/nerds/ankush/webApplication_Genome/Git_Genome/GenomeAPI/ldsc/ldsc.py \
        --h2-cts "+all_files+" \
        --ref-ld-chr /ifs/loni/faculty/njahansh/nerds/ravi/genetics/ldsc/1000G_EUR_Phase3_baseline/baseline. \
        --out "+PROCESSED_FILES+"LDSC_Stats/"+fileOutName+" \
        --ref-ld-chr-cts /ifs/loni/faculty/njahansh/nerds/ravi/genetics/ldsc/ldsc_seg_ldscores/Corces_ATAC.ldcts \
        --w-ld-chr /ifs/loni/faculty/njahansh/nerds/ravi/genetics/ldsc/weights_hm3_no_hla/weights."

#--out /ifs/loni/faculty/njahansh/GAMBIT/genome_WebApplication/static/LDSC_Stats/"+fileOutName+" 


        print("********************************************************************************",fileOutName)
        self.statFileName=fileOutName
        subprocess.call(cmd_line_n, shell=True)