from SimpleCV import Image, Display, Camera, DrawingLayer
import time
print "Seleccione una de las siguientes aplicaciones de seguimiento: "
print "\t1.- Deteccion y seguimiento de un rectangulo blanco" ##Creamos menu para realizar la eleccion de la aplicacion requerida
print "\t2.- Deteccion y seguimiento de varios rectangulos blancos"
print "\t3.- Aplicacion Medica"
print "\t4.- Salir" 

while True:
    opc=raw_input("Ingrese el numero de una opcion: ")
    if opc=="1":
        d=Display() ## Se le asigna una variable al display para posteriormente controlarlo mediante un ciclo while
        c=Camera() ## Se le asigna una variable a la camara
        while d.isNotDone(): ## Se crea un ciclo infinito hasta que se cierre la ventana del display por el usuario
            img=c.getImage() ## Se captura la imagen con la camara
            dis=img.colorDistance((0,0,0)) ## Se calcula la distancia de colores con respecto al negro 
            seg=dis.stretch(220,255) ## se realiza un estiramiento de histograma para dejar solamente los pixeles en donde se encuentra el objeto de interes y se mejora el contraste
            blobs=seg.findBlobs() ## se buscan grupos de pixeles
            blobs.sortArea() ## se ordenan los grupos por el area de cada uno en forma ascendente
            if blobs:
                rect=blobs.filter([b.isRectangle(0.15) for b in blobs]) ## se filtran los grupos por aquellos que se asemejan a un rectangulo con cierta tolerancia
                if rect:
                    fl=DrawingLayer((img.width,img.height)) ## Se crea una mascara para dibujar los rectangulos
                    fbd=(rect[-1].width(),rect[-1].height()) ## Se guarda la dimension del rectangulo de mayor area
                    tlc=rect[-1].topLeftCorner() ## Se obtiene la coordenada de la esquina superior izquierda del rectangulo
                    fb=fl.rectangle(tlc,fbd,(0,200,0),3) ## se dibuja el rectangulo con los datos nombrados
                    img.addDrawingLayer(fl) ## se agrega la mascara sobre la imagen original
                    img.applyLayers()           
            img.show() ## Se muestra la imagen en tiempo "real"
    elif opc=="2":
        d=Display() ## Se le asigna una variable al display para posteriormente controlarlo mediante un ciclo while
        c=Camera() ## Se le asigna una variable a la camara
        while d.isNotDone():
            img=c.getImage()## Se captura la imagen con la camara
            dis=img.colorDistance((0,0,0)) ## Se calcula la distancia de colores con respecto al negro 
            seg=dis.stretch(220,255)## se realiza un estiramiento de histograma para dejar solamente los pixeles en donde se encuentra el objeto de interes y se mejora el contraste
            blobs=seg.findBlobs()## se buscan grupos de pixeles
            blobs.sortArea()## se ordenan los grupos por el area de cada uno en forma ascendente
            if blobs:
                rect=blobs.filter([b.isRectangle(0.15) for b in blobs])## se filtran los grupos por aquellos que se asemejan a un rectangulo con cierta tolerancia
                if rect:
                    for i in range (1,len(rect)): ## Se realiza el procedimiento para varios rectangulos de igual manera a como se realiza para uno
                        fl=DrawingLayer((img.width,img.height))
                        fbd=(rect[-i].width(),rect[-i].height())
                        tlc=rect[-i].topLeftCorner()
                        fb=fl.rectangle(tlc,fbd,(0,200,0),3)
                        img.addDrawingLayer(fl)
                        img.applyLayers()           
            img.show() ## Se muestra la imagen resultante    
    elif opc=="3":
        d=Display() ## Se le asigna una variable al display para posteriormente controlarlo mediante un ciclo while
        c=Camera() ## Se le asigna una variable a la camara
        while d.isNotDone():
            img=c.getImage()## Se captura la imagen con la camara
            dis=img.colorDistance((255,255,255))## Se calcula la distancia de colores con respecto al blanco
            seg=dis.stretch(50,100) ## se realiza un estiramiento de histograma para dejar solamente los pixeles en donde se encuentra el objeto de interes y se mejora el contraste
            blobs=seg.findBlobs() ## se buscan grupos de pixeles
            blobs.sortArea()## se ordenan los grupos por el area de cada uno en forma ascendente
            if blobs:
                rect=blobs.filter([b.isRectangle(0.15) for b in blobs])## se filtran los grupos por aquellos que se asemejan a un rectangulo con cierta tolerancia
                if len(rect)>1:
                    fl=DrawingLayer((img.width,img.height)) ## Se crea una mascara para dibujar los rectangulos
                    fbd=(rect[-2].width(),rect[-2].height()) ## Se guarda la dimension del segundo rectangulo mas grande
                    tlc=rect[-2].topLeftCorner() ## se guarda la coordenada de la esquina superior izquierda del segundo rectangulo de mayor area
                    fb=fl.rectangle(tlc,fbd,(0,200,0),3) ## se dibujan los rectangulos en la mascara
                    img.addDrawingLayer(fl) ## se aplica la mascara sobre la imagen original
                    img.applyLayers()
            img.show() ## se muestra la imagen resultante
    elif opc=="4":
        break
    else:
        print "opcion no valida"
