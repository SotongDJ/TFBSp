import pprint,json
falnaem = "-"
while falnaem != "":
    falnaem = input("File name? (without gs)\n")
    if falnaem != "":    
        sos = open(falnaem+'.gs').read().splitlines()
        vara = ["name","Weight_matrix_model","class","id","family","ugene_group","pazar_tf_id"]
        resut = {'uuid':{}}
        uset = []
        for vaso in vara:
            resut.update({vaso:{}})

        for kechap in sos:
            dada = []
            if "misc_binding" in kechap:
                dada=kechap.split('/')
                #pprint.pprint(dada)
                for ran in dada:
                    if '..' in ran:
                        uuid = ran
                        resut.get('uuid').update({ uuid : {} })
                        uset.append(uuid)
                for uuid in uset:
                    if uuid in kechap:
                        for ran in dada:
                            for vaso in vara:
                                if vaso == ran[0:len(vaso)]:
                                    if uuid == "":
                                        print("uuid=\"\"")
                                        break
                                    valuo = ran.replace(vaso+"=","")
                                    resut.get('uuid').get(uuid).update({ vaso : valuo })
                                    donde = resut.get(vaso).get(valuo,[])
                                    donde.append(uuid)
                                    resut.get(vaso).update({ valuo : donde })
        resutfal = open(falnaem+'.json','w')
        json.dump(resut,resutfal,indent=4,sort_keys=True)
        resutfal.close()
