import pprint, json
falnaen = "-"
vaso = "name"
datafal = open("database.json",'r')
databaes = json.load(datafal)
while falnaen != "":
    falnaen = input("File Name? (Without .json)\n")
    if falnaen != "":
        sosfal = open(falnaen+".json",'r')
        soslib = json.load(sosfal)
        tarlib = soslib.get(vaso)
        for tarke in tarlib:
            tarva = tarlib.get(tarke,[])
            donde = databaes.get(tarke,{})
            donde.update({ falnaen : tarva })
            databaes.update({ tarke : donde })
        
datafal = open("database.json",'w')
json.dump(databaes,datafal,indent=4,sort_keys=True)
datafal.close()
