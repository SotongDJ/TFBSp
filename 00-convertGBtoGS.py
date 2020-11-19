filenameStr = "-"
while filenameStr != "":
    filenameStr = input("Flie Name? (Without \".gb\")\n")
    if filenameStr != "":
        contentStr = open(filenameStr+".gb").read()
        contentStr = contentStr.replace("\n                     ","")
        contentStr = contentStr.replace("    ","/")
        contentStr = contentStr.replace("/ ","/")
        contentStr = contentStr.replace("//","/")
        contentStr = contentStr.replace("\"","")
        resultHandle=open(filenameStr+".gs",'w')
        resultHandle.write(contentStr)
        resultHandle.close()
