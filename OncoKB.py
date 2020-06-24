#!/usr/bin/env python3

import sys
import os
import requests
from urllib.parse import urljoin
import json
import argparse

token="your token"

__author__      = "cococou"
__copyright__   = "Copyright 2020, cococou"

#curl -X GET "https://demo.oncokb.org/api/v1/annotate/mutations/byProteinChange?hugoSymbol=BRAF&alteration=V600E&tumorType=Melanom" -H "accept: application/json"
#curl -X GET "https://www.oncokb.org/api/v1/annotate/mutations/byProteinChange?hugoSymbol=BRAF&entrezGeneId=673&alteration=V600E&consequence=missense_variant&proteinStart=600&proteinEnd=600&tumorType=Melanoma&evidenceType=GENE_SUMMARY%2C%20MUTATION_SUMMARY" -H "accept: application/json" -H "Authorization: Bearer [token]"


baseurl="https://www.oncokb.org/api/v1/"
testurl="https://demo.oncokb.org/api/v1/"

class OncoAnno():
    def  __init__(self,baseurl="https://www.oncokb.org/api/v1/",module='annotate',submodule=['mutations','byProteinChange'],parameters={'hugoSymbol':'BRAF','alteration':'V600E',"tumorType":'Melanom"'},token="adcf173d-31cb-4266-a8c2-f474f9bec596"):
        self.baseurl = baseurl
        self.module = module
        self.submodule = '/'.join(submodule)
        self.parameters = parameters
        self.token = token
        self.headers = {'Authorization' : 'Bearer {token}'.format(token=self.token),"accept":'application/json' } #requests headers
        #self.headers = {"accept":'application/json'}
    
    def GetUrl(self):
        tmpurl = '/'.join([self.module,self.submodule])
        self.moduleurl = urljoin(self.baseurl,tmpurl)
        #print(self.moduleurl)

    def GetAnno(self):
        self.GetUrl()
        r = requests.get(self.moduleurl,params=self.parameters,timeout=20,headers=self.headers)
        if r.status_code != 200:
            print("connection err!!! return {}".format(r.status_code),file=sys.stderr)
            print(r.url)
            exit(1)
        self.content = r.content
        self.url = r.url

def GetOpt():
    useage="""
eg:
    byGenomicChange ref is hg19
python ~/bin/OncoKB.py --module  levels --submodule sensitive
python ~/bin/OncoKB.py --module annotate --submodule mutations  byProteinChange --parameters hugoSymbol=BRAF alteration=V600E  tumorType=Melanomi
python ~/bin/OncoKB.py --module annotate --submodule copyNumberAlterations --parameters copyNameAlterationType=GAIN hugoSymbol=EGFR tumorType=Lung
python ~/bin/OncoKB.py --module annotate --submodule mutations byGenomicChange --parameters genomicLocation=chr7,55259515,55259515,T,G tumorType=Lung evidenceType=STANDARD_THERAPEUTIC_IMPLICATIONS_FOR_DRUG_SENSITIVITY
python ~/bin/OncoKB.py --module annotate --submodule structuralVariants --parameters hugoSymbolA=ALK hugoSymbolB=EML4  structuralVariantType=FUSION isFunctionalFusion=True tumorType=Lung
    """
    parser = argparse.ArgumentParser(description=useage,formatter_class=argparse.RawTextHelpFormatter)
    parser.add_argument('--baseurl',help="defualt https://www.oncokb.org/api/v1/ , oncokb api base url",default="https://www.oncokb.org/api/v1/")
    parser.add_argument('--module',help="oncoKB APIs filter tag including 'annotate utils info levels,detail' in https://www.oncokb.org/api/v1/",required=True)
    parser.add_argument('--submodule',help = "submodule of the module ,such as copyNumberAlterations in annotate, detail in https://www.oncokb.org/api/v1/",nargs='+',default=None)
    parser.add_argument('--parameters',help = "--parameters hugoSymbol=BRAF alteration=V600E tumorType=Melanom",nargs="+" ,default=None)
    parser.add_argument('--token',help="token of OncoKB APIs",default="adcf173d-31cb-4266-a8c2-f474f9bec596")
    args = parser.parse_args()
    return args

if __name__ == "__main__":
    par = GetOpt()
    if par.parameters:
        par.parameters = {i.split("=")[0]:i.split("=")[1] for i in par.parameters}
    else:
        par.parameters={}
    if not par.submodule:
        par.submodule = []
    print(par)
    ann = OncoAnno(baseurl=par.baseurl,module=par.module,submodule=par.submodule,parameters=par.parameters,token=par.token)
    ann.GetAnno()
    #print(ann.url)
    #print(ann.content)
    print(json.dumps(json.loads(ann.content),indent = 4, sort_keys=True))

#baseurl="https://www.oncokb.org/api/v1/",module='annotate',submodule=['mutations','byProteinChange'],parameters={'hugoSymbol':'BRAF','alteration':'V600E',"tumorType":'Melanom"'},token="adcf173d-31cb-4266-a8c2-f474f9bec596"
#test = OncoAnno()
#test.GetAnno()
