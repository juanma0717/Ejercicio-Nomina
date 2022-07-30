import re
from io import open
IDdocument = str(input("Escriba su numero de documento"))
svIDdocument = re.match(r'[0-9]{8,12}\Z',IDdocument)
if svIDdocument:
    print("Correcto")
else:
    while not svIDdocument:
        print("Incorrecto")
        IDdocument= str(input("Escriba su numero de documento"))
        svIDdocument = re.match(r'[0-9]{8,12}\Z',IDdocument)
        if svIDdocument:
            print("Correcto")

Name = str(input("Escriba su nombre"))
svNAme= re.match(r'[a-zA-Z, ,ñ,á,é,í,ó,ú]{2,30}\Z',Name)
if svNAme:
    print ("Correcto")
    print (Name)
else:
    while not svNAme:
        print ("Incorrecto")
        Name = str(input("Escriba su nombre"))
        svNAme= re.match(r'[a-zA-Z, ,ñ,á,é,í,ó,ú]{2,30}\Z',Name)
        if svNAme:
            print("Correcto")
            print(Name)

lastName = str(input("Escriba sus apellidos"))
svlastName= re.match(r'[a-zA-Z, ,ñ,á,é,í,ó,ú]{0,45}\Z',lastName)
if svlastName:
    print ("Correcto")
    print (lastName)
else:
    while not svlastName:
        print ("Incorrecto")
        lastName = str(input("Escriba sus apellidos"))
        svlastName= re.match(r'[a-zA-Z, ,ñ,á,é,í,ó,ú]{0,45}\Z',lastName)
        if svNAme:
            print("Correcto")
            print(lastName)

salary = str(input("Digite su salario establecido"))
svSalary = re.match(r'[0-9]{6,9}\Z',salary)
if svSalary:
    print("Correcto")
else:
    while not svSalary:
        print("Incorrecto")
        salary= str(input("Escriba su salario establecido"))
        svSalary = re.match(r'[0-9]{6,9}\Z',salary)
        if svSalary:
            print("Correcto")

wkDays = str(input("Escriba los dias trabajados"))
svWkDays = re.match(r'[0-9]{0,2}\Z',wkDays)
if svWkDays:
    print("Correcto")
else:
    while not svWkDays:
        print("Incorrecto")
        wkDays= str(input("Escriba los dias trabajados"))
        svWkDays = re.match(r'[0-9]{0,2}\Z',wkDays)
        if svWkDays:
            print("Correcto")
wkDays1= float(wkDays)
salary1=float(salary)
cashWkDays= float(salary1/30)
cashWkDays= float(cashWkDays*wkDays1)
salarychk=0
if salary1<2000000:
    salarychk=cashWkDays+117200
salarychk1=float(salarychk)
healty=float(salarychk1*0.04)
pension=float(salarychk1*0.04)
finalSalary=float(salarychk1-(healty+pension))
txtArchive=open("nomina.txt","w")
totalDates= (f'Señor/a {Name}{lastName} \n De documrnto {IDdocument}\n Su salario es = {finalSalary}')
txtArchive.write(totalDates)
txtArchive.close()
    
