import random

archivo=open("Vocabulario B2.txt", encoding="utf-8")

vocabulario_kanji=[]
vocabulario_no_kanji=[]

for linea in archivo:
  linea_suelta=linea.strip()
  linea_lista=linea_suelta.split(",")
  if linea_lista[0]==linea_lista[1]:
    vocabulario_no_kanji.append(linea_lista)
  else:
    vocabulario_kanji.append(linea_lista)

archivo.close()

hiragana=["あ","い","う","え","お","か","き","く","け","こ","さ","し","す","せ","そ","た","ち","つ","て","と","な","に","ぬ","ね","の","は","ひ","ふ","へ","ほ",   
            "ま","み","む","め","も","や","ゆ","よ","ら","り","る","れ","ろ","わ","を","ん","が","ぎ","ぐ","げ","ご","ざ","じ","ず","ぜ","ぞ","だ","じ","で","ど",
            "ば","び","ぶ","べ","ぼ","ぱ","ぴ","ぷ","ぺ","ぽ","きゃ","きゅ","きょ","ぎゃ","ぎゅ","ぎょ","にゃ","にゅ","にょ","ひゃ","ひゅ","ひょ","びゃ","びゅ","びょ","ぴゃ",
            "ぴゅ","ぴょ","りゃ","りゅ","りょ","じゃ","じゅ","じょ","ちゃ","ちゅ","ちょ","しゃ","しゅ","しょ"]

largo_kanji=len(vocabulario_kanji)

vocabulario=vocabulario_kanji+vocabulario_no_kanji


puntos=0
preguntas=0
tipo_preguntas=0
modo=-1
preguntas_alternativas=0
preguntas_escritas=0
preguntas_kanji_alternativas=0
preguntas_kanji_lectura=0

print("Bienvenid@ al Quiz de Japones")
print("\n")

while modo!=1 and modo!=2 and modo!=3:
    print("Elige un modo")
    print("1. Solo Hiragana/Katakana")
    print("2. Solo Kanji")
    print("3. Kanji y Hiragana/Katakana")
    print("\n")
    modo=int(input())
    print("\n")
    if modo!=1 and modo!=2 and modo!=3:
        print("Debes ingresar 1, 2 o 3")
        print("\n") 

if modo==2 or modo==3:
    while tipo_preguntas!=1 and tipo_preguntas!=2 and tipo_preguntas!=3 and tipo_preguntas!=4 and tipo_preguntas!=5:
        print("¿Qué tipo de preguntas vas a querer?")
        print("1. Vocabulario (alternativas)")
        print("2. Vocabulario (respuestas escritas)")
        print("3. Lectura de kanjis (alternativas)")
        print("4. Lectura de kanjis (respuesta escrita)")
        print("5. Mixto")
        print("\n")
        tipo_preguntas=int(input())
        print("\n")
        if tipo_preguntas!=1 and tipo_preguntas!=2 and tipo_preguntas!=3 and tipo_preguntas!=4 and tipo_preguntas!=5:
            print("Debes ingresar 1, 2, 3, 4 o 5")
            print("\n")  
        elif tipo_preguntas==1:
            preguntas_alternativas=int(input("¿Cuantas preguntas de vocabulario (alternativas) vas a querer?\n"))
            print("\n")
        elif tipo_preguntas==2:
            preguntas_escritas=int(input("¿Cuantas preguntas de vocabulario (respuestas escritas) vas a querer?\n"))
            print("\n")
        elif tipo_preguntas==3:
            preguntas_kanji_alternativas=int(input("¿Cuantas preguntas de lectura de kanji (alternativas) vas a querer?\n"))
            print("\n")
        elif tipo_preguntas==4:
            preguntas_kanji_lectura=int(input("¿Cuantas preguntas de lectura de kanji (respuesta escrita) vas a querer?\n"))
            print("\n")
        elif tipo_preguntas==5:
            preguntas_alternativas=int(input("¿Cuantas preguntas de vocabulario (alternativas) vas a querer?\n"))
            preguntas_escritas=int(input("¿Cuantas preguntas de vocabulario (respuestas escritas) vas a querer?\n"))
            preguntas_kanji_alternativas=int(input("¿Cuantas preguntas de lectura de kanji (alternativas) vas a querer?\n"))
            preguntas_kanji_lectura=int(input("¿Cuantas preguntas de lectura de kanji (respuesta escrita) vas a querer?\n"))
            print("\n")

else:
    while tipo_preguntas!=1 and tipo_preguntas!=2 and tipo_preguntas!=3:
        print("¿Qué tipo de preguntas vas a querer?")
        print("1. Vocabulario (alternativas)")
        print("2. Vocabulario (respuestas escritas)")
        print("3. Mixto")
        print("\n")
        tipo_preguntas=int(input())
        print("\n") 
        if tipo_preguntas!=1 and tipo_preguntas!=2 and tipo_preguntas!=3:
            print("Debes ingresar 1, 2 o 3")
            print("\n")              
        elif tipo_preguntas==1:
            preguntas_alternativas=int(input("¿Cuantas preguntas de vocabulario (alternativas) vas a querer?\n"))
            print("\n")
        elif tipo_preguntas==2:
            preguntas_escritas=int(input("¿Cuantas preguntas de vocabulario (respuestas escritas) vas a querer?\n"))
            print("\n")
        elif tipo_preguntas==3:
            preguntas_alternativas=int(input("¿Cuantas preguntas de vocabulario (alternativas) vas a querer?\n"))
            preguntas_escritas=int(input("¿Cuantas preguntas de vocabulario (respuestas escritas) vas a querer?\n"))
            print("\n")




if modo==2:
    palabras=random.sample(range(0,largo_kanji),preguntas_alternativas+preguntas_escritas+preguntas_kanji_alternativas+preguntas_kanji_lectura)

elif preguntas_kanji_alternativas!=0 or preguntas_kanji_lectura!=0:
    palabras=random.sample(range(0,len(vocabulario)),preguntas_alternativas+preguntas_escritas)
    rango=list(range(0,largo_kanji))
    for i in range(0,len(palabras)):
        if palabras[i] in range (0,largo_kanji-1):
            rango.remove(palabras[i])
    palabras_kanji=random.sample(rango,preguntas_kanji_alternativas+preguntas_kanji_lectura)
    palabras=palabras+palabras_kanji
    
else:
    palabras=random.sample(range(0,len(vocabulario)),preguntas_alternativas+preguntas_escritas+preguntas_kanji_alternativas+preguntas_kanji_lectura)


#vocabulario (alternativas)#

for i in range(1,preguntas_alternativas+1):
    
    palabra_pregunta=vocabulario[palabras[i-1]]
    correcta=palabra_pregunta[random.randint(2,len(palabra_pregunta)-1)]
    
    
    print("Pregunta n° "+str(preguntas+1)+"")
    if modo==1 or modo==2:
        print("¿Cual de las siguientes alternativas corresponde a un posible significado de la palabra "+palabra_pregunta[modo-1]+"?\n\n")
    
    elif modo==3:
        if palabra_pregunta[modo-2]!=palabra_pregunta[modo-3]:
            print("¿Cual de las siguientes alternativas corresponde a un posible significado de la palabra "+palabra_pregunta[modo-2]+" ("+palabra_pregunta[modo-3]+")?\n\n")
        else:
            print("¿Cual de las siguientes alternativas corresponde a un posible significado de la palabra "+palabra_pregunta[modo-3]+"?\n\n")
    
    alternativa=random.randint(1,4)
    
    
    r1A=random.randint(0,len(vocabulario)-1)
    r1B=random.randint(2,len(vocabulario[r1A])-1)
    
    r2A=random.randint(0,len(vocabulario)-1)
    r2B=random.randint(2,len(vocabulario[r2A])-1)
    
    r3A=random.randint(0,len(vocabulario)-1)
    r3B=random.randint(2,len(vocabulario[r3A])-1)
    
    while r1A==palabras[i-1] or vocabulario[r1A][r1B]==palabra_pregunta:
        r1A=random.randint(0,len(vocabulario)-1)
        r1B=random.randint(2,len(vocabulario[r1A])-1)
    
    while r2A==palabras[i-1] or r1A==r2A or vocabulario[r2A][r2B]==palabra_pregunta or vocabulario[r1A][r1B]==vocabulario[r2A][r2B]:
        r2A=random.randint(0,len(vocabulario)-1)
        r2B=random.randint(2,len(vocabulario[r2A])-1)
    
    while r3A==palabras[i-1] or r1A==r3A or r2A==r3A or vocabulario[r3A][r3B]==palabra_pregunta or vocabulario[r1A][r1B]==vocabulario[r3A][r3B] or vocabulario[r2A][r2B]==vocabulario[r3A][r3B]:
        r3A=random.randint(0,len(vocabulario)-1)
        r3B=random.randint(2,len(vocabulario[r3A])-1)
    
    falsa1=vocabulario[r1A][r1B]
    falsa2=vocabulario[r2A][r2B]
    falsa3=vocabulario[r3A][r3B]
    
    
    puesto=0
    
    if alternativa==1:
        print("1. "+correcta+"")
        puesto=puesto+1
        
    print(""+str(1+puesto)+". "+falsa1+"")
    
    if alternativa==2:
        print("2. "+correcta+"")
        puesto=puesto+1
        
    print(""+str(2+puesto)+". "+falsa2+"")
    
    if alternativa==3:
        print("3. "+correcta+"")
        puesto=puesto+1
        
    print(""+str(3+puesto)+". "+falsa3+"")
    
    if alternativa==4:
        print("4. "+correcta+"")
    
    print("\n")
    usuario=input()
    if usuario=="":
        usuario=0
    
    usuario=int(usuario)
    
    if usuario==alternativa:
        print("\n")
        print("CORRECTO!")
        if modo==2:
            print("Y su lectura es "+palabra_pregunta[0]+"")
        print("\n")
        puntos=puntos+1
    else:
        print("\n")
        print("INCORRECTO!")
        print("La respuesta correcta es "+correcta+"")
        if modo==2:
            print("Y su lectura es "+palabra_pregunta[0]+"")
        print("\n")
    
    preguntas=preguntas+1
    print("_________________________________________________________________________________________________________________")
    print("\n")
    print("\n")



#vocabulario(respuestas escritas)#

for i in range(preguntas_alternativas+1,preguntas_alternativas+preguntas_escritas+1):
    
    palabra_pregunta=vocabulario[palabras[i-1]]
    respuesta_correcta=False
      
    print("Pregunta n° "+str(preguntas+1)+"")
    if modo==1 or modo==2:
        print("Escribe (con tildes) alguno de los posibles significados de la palabra "+palabra_pregunta[modo-1]+"\n\n")
    
    elif modo==3:
        if palabra_pregunta[modo-2]!=palabra_pregunta[modo-3]:
            print("Escribe (con tildes) alguno de los posibles significados de la palabra "+palabra_pregunta[modo-2]+" ("+palabra_pregunta[modo-3]+")\n\n")
        else:
            print("Escribe (con tildes) alguno de los posibles significados de la palabra "+palabra_pregunta[modo-3]+"\n\n")
    
    usuario=input()
    
    for j in range(2,len(palabra_pregunta)):
        if usuario==palabra_pregunta[j]:
            respuesta_correcta=True
    
    
    if respuesta_correcta:
        print("\n")
        print("CORRECTO!")
        if modo==2:
            print("Y su lectura es "+palabra_pregunta[0]+"")
        print("\n")
        puntos=puntos+1
    else:
        print("\n")
        print("INCORRECTO!")
        print("Las posibles respuestas son:")
        for j in range(2,len(palabra_pregunta)):
            print(palabra_pregunta[j])
        if modo==2:
            print("Y su lectura es "+palabra_pregunta[0]+"")
        print("\n")
    
    preguntas=preguntas+1
    print("_________________________________________________________________________________________________________________")
    print("\n")
    print("\n")    



#lectura kanji (alternativas)#

for i in range(preguntas_alternativas+preguntas_escritas+1,preguntas_alternativas+preguntas_escritas+preguntas_kanji_alternativas+1):
    
    palabra_pregunta=vocabulario[palabras[i-1]]
    correcta=palabra_pregunta[0]
    
    
    print("Pregunta n° "+str(preguntas+1)+"")
    
    print("¿Cual de las siguientes alternativas corresponde a la lectura en hiragana de "+palabra_pregunta[1]+"?\n\n")
    

    
    alternativa=random.randint(1,4)
    
    
    falsa1=""
    falsa2=""
    falsa3=""


    for i in range(0,len(palabra_pregunta[1])):
        if palabra_pregunta[1][i] in hiragana:
            falsa1=falsa1+palabra_pregunta[1][i]
        else:
            hiragana_random=random.sample(hiragana,random.randint(1,2))
            for j in range(0,len(hiragana_random)):
                falsa1=falsa1+hiragana_random[j]

    for i in range(0,len(palabra_pregunta[1])):
        if palabra_pregunta[1][i] in hiragana:
            falsa2=falsa2+palabra_pregunta[1][i]
        else:
            hiragana_random=random.sample(hiragana,random.randint(1,2))
            for j in range(0,len(hiragana_random)):
                falsa2=falsa2+hiragana_random[j]

    for i in range(0,len(palabra_pregunta[1])):
        if palabra_pregunta[1][i] in hiragana:
            falsa3=falsa3+palabra_pregunta[1][i]
        else:
            hiragana_random=random.sample(hiragana,random.randint(1,2))
            for j in range(0,len(hiragana_random)):
                falsa3=falsa3+hiragana_random[j]   

    
    
    puesto=0
    
    if alternativa==1:
        print("1. "+correcta+"")
        puesto=puesto+1
        
    print(""+str(1+puesto)+". "+falsa1+"")
    
    if alternativa==2:
        print("2. "+correcta+"")
        puesto=puesto+1
        
    print(""+str(2+puesto)+". "+falsa2+"")
    
    if alternativa==3:
        print("3. "+correcta+"")
        puesto=puesto+1
        
    print(""+str(3+puesto)+". "+falsa3+"")
    
    if alternativa==4:
        print("4. "+correcta+"")
    
    print("\n")
    usuario=input()
    if usuario=="":
        usuario=0
    
    usuario=int(usuario)
    
    if usuario==alternativa:
        print("\n")
        print("CORRECTO!")
        print("Y sus posibles significados son:")
        for j in range(2,len(palabra_pregunta)):
            print(palabra_pregunta[j])
        print("\n")
        puntos=puntos+1
    else:
        print("\n")
        print("INCORRECTO!")
        print("La respuesta correcta es "+correcta+"")
        print("Y sus posibles significados son:")
        for j in range(2,len(palabra_pregunta)):
            print(palabra_pregunta[j])
        print("\n")
    
    preguntas=preguntas+1
    print("_________________________________________________________________________________________________________________")
    print("\n")
    print("\n")



#lectura kanji (respuestas escritas)#

for i in range(preguntas_alternativas+preguntas_escritas+preguntas_kanji_alternativas+1,preguntas_alternativas+preguntas_escritas+preguntas_kanji_alternativas+preguntas_kanji_lectura+1):
    
    palabra_pregunta=vocabulario[palabras[i-1]]
      
    print("Pregunta n° "+str(preguntas+1)+"")
    print("Escribe (en hiragana) la lectura de la siguiente palabra/frase "+palabra_pregunta[1]+"\n\n")
    
    usuario=input()
    
    
    if usuario==palabra_pregunta[0]:
        print("\n")
        print("CORRECTO!")
        print("Y sus posibles significados son:")
        for j in range(2,len(palabra_pregunta)):
            print(palabra_pregunta[j])
        print("\n")
        puntos=puntos+1
    else:
        print("\n")
        print("INCORRECTO!")
        print("La lectura es "+palabra_pregunta[0]+"")
        print("Y sus posibles significados son:")
        for j in range(2,len(palabra_pregunta)):
            print(palabra_pregunta[j])
        print("\n")
    
    preguntas=preguntas+1
    print("_________________________________________________________________________________________________________________")
    print("\n")
    print("\n")    



print("Obtuviste "+str(puntos)+"/"+str(preguntas)+" respuesta correctas!")