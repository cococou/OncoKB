# OncoKB
oncoKB api
只是个封装程序



# first 
you need to get your own api token  from oncokb website


# usage and keyword
please see it from:
https://api.oncokb.org/oncokb-website/api

# usage
return value is json  string 

```sh
usage: OncoKB.py [-h] [--baseurl BASEURL] --module MODULE
                 [--submodule SUBMODULE [SUBMODULE ...]]
                 [--parameters PARAMETERS [PARAMETERS ...]] [--token TOKEN]

eg:
    byGenomicChange ref is hg19
python ~/bin/OncoKB.py --module  levels --submodule sensitive
python ~/bin/OncoKB.py --module annotate --submodule mutations  byProteinChange --parameters hugoSymbol=BRAF alteration=V600E  tumorType=Melanomi
python ~/bin/OncoKB.py --module annotate --submodule copyNumberAlterations --parameters copyNameAlterationType=GAIN hugoSymbol=EGFR tumorType=Lung
python ~/bin/OncoKB.py --module annotate --submodule mutations byGenomicChange --parameters genomicLocation=chr7,55259515,55259515,T,G tumorType=Lung evidenceType=STANDARD_THERAPEUTIC_IMPLICATIONS_FOR_DRUG_SENSITIVITY
python ~/bin/OncoKB.py --module annotate --submodule structuralVariants --parameters hugoSymbolA=ALK hugoSymbolB=EML4  structuralVariantType=FUSION isFunctionalFusion=True tumorType=Lung


optional arguments:
  -h, --help            show this help message and exit
  --baseurl BASEURL     defualt https://www.oncokb.org/api/v1/ , oncokb api base url
  --module MODULE       oncoKB APIs filter tag including 'annotate utils info levels,detail' in https://www.oncokb.org/api/v1/
  --submodule SUBMODULE [SUBMODULE ...]
                        submodule of the module ,such as copyNumberAlterations in annotate, detail in https://www.oncokb.org/api/v1/
  --parameters PARAMETERS [PARAMETERS ...]
                        --parameters hugoSymbol=BRAF alteration=V600E tumorType=Melanom
  --token TOKEN         token of OncoKB APIs
```
