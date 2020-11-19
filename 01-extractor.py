import pprint,json
filenameStr = "-"
while filenameStr != "":
    filenameStr = input("File name? (without gs)\n")
    if filenameStr != "":    
        contentList = open(filenameStr+'.gs').read().splitlines()
        keyList = ["name","Weight_matrix_model","class","id","family","ugene_group","pazar_tf_id"]
        resultDict = {'uuid':{}}
        uuidList = []
        for keyStr in keyList:
            resultDict.update({keyStr:{}})

        for contentLineStr in contentList:
            detailList = []
            if "misc_binding" in contentLineStr:
                detailList=contentLineStr.split('/')
                #pprint.pprint(detailList)
                for pairStr in detailList:
                    if '..' in pairStr:
                        uuid = pairStr
                        resultDict.get('uuid').update({ uuid : {} })
                        uuidList.append(uuid)
                for uuid in uuidList:
                    if uuid in contentLineStr:
                        for pairStr in detailList:
                            for keyStr in keyList:
                                if keyStr == pairStr[0:len(keyStr)]:
                                    if uuid == "":
                                        print("uuid=\"\"")
                                        break
                                    valueStr = pairStr.replace(keyStr+"=","")
                                    resultDict.get('uuid').get(uuid).update({ keyStr : valueStr })
                                    resultList = resultDict.get(keyStr).get(valueStr,[])
                                    resultList.append(uuid)
                                    resultDict.get(keyStr).update({ valueStr : resultList })
        resultHandle = open(filenameStr+'.json','w')
        json.dump(resultDict,resultHandle,indent=4,sort_keys=True)
        resultHandle.close()
