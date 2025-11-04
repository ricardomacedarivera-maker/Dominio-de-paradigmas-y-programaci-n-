nombres = ["ANGEL MAURICIO","MARCO ANTONIO","EDGAR DANIEL","BETHZY ALEYDIZ","FABIOLA MICHEL","FRIDA VISTORIA","ERNESTO YAIR","ANGEL YAEL","AMBAR NAHOMI","URIEL","LUIS ENRIQUE","BRAYAN ALEXANDER","ERICK","FERNANDA ABIGAIL","ESTEFANI SARAHI","YUMIKO JATZERY","HANSEL DANIEL","JULIO ALBERTO","ENRIQUE UCIEL","YOJAN JOEL","PEDO EDUARDO","MIRELLA YAMILE","ALISON DAYANA","PRISCILA","SERGIO ALEXIS","RICARDO","SAMUEL JESHUA","VANESSA ISABEL","SARAHI VALERIA","DAVID GERSSAYN","JOSE ANGEL","GABRIEL","CRISTIAN YUREM","ARTURO AZAEL","ARMANDO"]

vocales=("A","E","I","O","U")
inicio_vocal=0
for nombre in nombres:
    if nombre[0] in vocales:
        inicio_vocal+=1
        print("nombres que inician con vocal",inicio_vocal)

mas_de_10=0
for nombre in nombres:
    if len(nombre.replace("",""))>10:
        mas_de_10+=1
        print("nombres con mas de 10 caracteres (sin espacios):",mas_de_10)

nombres_ordenados = sorted(nombres)
print("Primeros 3 nombres en orden alfabético:")
for nombre in nombres_ordenados[:3]:
    print(nombre)

con_y=[]
for nombre in nombres:
    if "Y" in nombre:
        con_y.append(nombre)
print("nombres que contienen la letra Y:")
for nombre in con_y:
    print(nombre)