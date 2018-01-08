falnaem = "-"
while falnaem != "":
    falname = input("Flie Name? (Without \".gb\")\n")
    if falnaem != "":
        sosfal = open(falname+".gb").read()
        sosfal = sosfal.replace("\n                     ","")
        sosfal = sosfal.replace("    ","/")
        sosfal = sosfal.replace("/ ","/")
        sosfal = sosfal.replace("//","/")
        sosfal = sosfal.replace("\"","")
        resutfal=open(falname+".gs",'w')
        resutfal.write(sosfal)
        resutfal.close()
