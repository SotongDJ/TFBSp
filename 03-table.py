import pprint, json
datafal = open("database.json",'r')
databaes = json.load(datafal)
primero = list(databaes.keys())
segundo = []
trenado = {}
spito = ','

for prino in databaes.keys():
    segundo.extend(list(databaes.get(prino).keys()))
    numa = 0    
    for tresto in databaes.get(prino).keys():
        numa = numa + len(set(databaes.get(prino).get(tresto)))
#        nuto = len(set(databaes.get(prino).get(tresto)))
#        if nuto > numa:
#            numa = nuto
    trenado.update({ prino + tresto : numa })

segunse = set(segundo)

tanto = sorted(list(segunse))

resut = open('Result.csv','w')
resut.write("Name,Location,"+spito.join(tanto)+'\n')

for prino in sorted(databaes.keys()):
    san = 1
    fin = len(tanto) - 1
    for tan in tanto:
        if databaes.get(prino).get(tan,[]) != []:
            for ta in sorted(set(databaes.get(prino).get(tan))):
                resut.write(prino + spito + ta + spito*san + ta + spito*fin + "\n")
        san = san + 1
        fin = fin - 1

resut.close()
