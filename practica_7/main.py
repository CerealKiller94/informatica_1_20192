# Funciones de Tkinter para la GUI
from tkinter import *
from tkinter.ttk import Separator
from tkinter.filedialog import askopenfilename 
from time import *

# Funciones de matplotlib para graficar datos
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

# Funciones propias
from sortfunc import loadFromFile, sortBurbuja, sortSeleccion, createRandomList

def popup_msg(msg):
    pop_up = Tk()
    pop_up.wm_title("Error")
    label = ttk.Label(pop_up, text=msg, font=("Helvetica",12))
    label.pack(side="top", fill="x", pady=10)
    exit_button = Button(pop_up, text="Aceptar", command=pop_up.destroy)
    exit_button.pack()
    pop_up.mainloop()

L_sin_ordenar=[]
# Metodos de ordenamiento
def animacionBurbuja():    
    global graficaDatos, L_sin_ordenar, sel_mayor_menor
    L = L_sin_ordenar.copy()
    orden = sel_mayor_menor.get()
    abscisas = range(1,len(L)+1)
    
    is_unordered = True
    iter_number = 0
    final = 0
    tamanho = len(L)
    while is_unordered:
        iter_number += 1
        is_unordered = False
        i = 0
        final += 1
        while i < tamanho-final:
            iter_number += 1
            if orden == 1:
                if L[i] < L[i+1]:
                    L[i], L[i+1] = L[i+1], L[i]
                    is_unordered = True
            else:
                if L[i] > L[i+1]:
                    L[i], L[i+1] = L[i+1], L[i]
                    is_unordered = True
            i += 1
        
        graficaDatos.clear()
        plt.pause(0.2)
        graficaDatos.stem(abscisas, L, use_line_collection = True)
        graficaDatos.grid() # Grid on
        canvas.draw()  
    

def animacionSeleccion():
    global graficaDatos, L_sin_ordenar, sel_mayor_menor
    L = L_sin_ordenar.copy()
    orden = sel_mayor_menor.get()
    abscisas = range(1,len(L)+1)
    
    inicio = 0
    tamanho = len(L)
    iter_number = 0
    
    while inicio < tamanho-1:
        
        iter_number += 1
        i = inicio + 1
        indx = inicio
        while i < tamanho:
            iter_number += 1
            if orden == 1:
                if L[indx] < L[i]:
                    indx = i
            else:
                if L[indx] > L[i]:
                    indx = i
            i += 1
        L[inicio], L[indx] = L[indx], L[inicio]
        inicio += 1
        
        graficaDatos.clear()
        plt.pause(0.2)
        graficaDatos.stem(abscisas, L, use_line_collection=True)
        graficaDatos.grid()        
        canvas.draw()
    
        
# Funciones handler

def generarLista():
    global L_sin_ordenar, minimo, maximo, nMuestras
    
    '''
    Obtener los valores de las variables lowest y highest
    simiar a como se obtuvo el valor de n
    Tener en cuenta posibles errores de usuario (ingreso de letras, por ejemplo)
    '''
    
    try:
        n = int(nMuestras.get())
        if n < 0:
            msg = "Cantidad negativa de numeros a generar"
            print(msg)
            popup_msg(msg)
            return
        
    except ValueError:
        msg = "Cantidad de muestras no valido"
        print(msg)
        popup_msg(msg)
        return 
    try:
        lowest = float(minimo.get())
    except ValueError:
        msg = "El valor del límite inferior no es un número valido "
        print(msg)
        popup_msg(msg)
        return
    try:
        highest = float(maximo.get())
        if lowest > highest:
            msg = "El valor del límite superior no puede ser menor que el limite inferior"
            print(msg)
            popup_msg(msg)
            return
    except ValueError:
        msg = "El valor del límite superior no es un número valido "
        print(msg)
        popup_msg(msg)
        return
 
    
    L_sin_ordenar = createRandomList(n, lowest, highest)
    x_axis = range(1,len(L_sin_ordenar)+1)        
    graficaDatos.clear()
    graficaDatos.stem(x_axis, L_sin_ordenar, use_line_collection=True)
    graficaDatos.grid()
    canvas.draw()

def loadInputData():
    global source_selection
    global L_sin_ordenar
    global minimo, maximo, nMuestras
	
    if source_selection.get() == 1:
        # Ventana para la seleccion del archivo
        fname = askopenfilename()        
        L_sin_ordenar = loadFromFile(fname)
        if type(L_sin_ordenar) is str:
            popup_msg(L_sin_ordenar)
            return
        x_axis = range(1,len(L_sin_ordenar)+1)        
        graficaDatos.clear()
        graficaDatos.stem(x_axis, L_sin_ordenar, use_line_collection=True)
        graficaDatos.grid()
        canvas.draw()
    elif source_selection.get() == 2:
		# Ventana para la generación aleatoria de la lista
        ventanaGenerador = Tk()

        # Frame superior 
        f1 = Frame(ventanaGenerador)
        labelSuperior = Label(f1, text = "Límite superior:     ",justify = LEFT)        
        labelSuperior.pack(side=LEFT)
        entrySuperior = Entry(f1, text="",justify = LEFT)
        entrySuperior.pack(side=LEFT)
        f1.pack(anchor=W, fill=X, expand=YES)
               
        # Frame mitad
        f2 = Frame(ventanaGenerador)
        labelInferior = Label(f2, text = "Límite inferior:       ",justify = LEFT)
        labelInferior.pack(side=LEFT)
        entryInferior = Entry(f2, text="",justify = LEFT)
        entryInferior.pack(side=LEFT)
        f2.pack(anchor=W, fill=X, expand=YES)
        
        # Frame inferior
        f3 = Frame(ventanaGenerador)
        labelMuestras = Label(f3, text = "Número de datos: ",justify = LEFT)
        labelMuestras.pack(side=LEFT)
        entryMuestras = Entry(f3, text="",justify = LEFT)
        entryMuestras.pack(side=LEFT)
        f3.pack(anchor=W, fill=X, expand=YES)
                
        botonGenerar = Button(ventanaGenerador, text = "Generar",command = generarLista)
        botonGenerar.pack()
        
        minimo = entryInferior
        maximo = entrySuperior
        nMuestras = entryMuestras
        ventanaGenerador.mainloop()
    else:
        msg = "No hay datos de entrada validos"
        popup_msg(msg)
        return


def sortHandler():
    try:
        from time import time
        global L_sin_ordenar, met, selPaso, box_value, graficaRendimiento, sel_mayor_menor
        # Ejecucion animada
        L_burbuja = L_sin_ordenar.copy()
        L_seleccion = L_sin_ordenar.copy()     
        L_py = L_sin_ordenar.copy()
        abscisas = range(1,len(L_sin_ordenar)+1)
        graficaDatos.clear()
        # Ejecucion de los metodos elegidos
        if met.get() == 1:
            if selPaso.get() == 1:
                animacionBurbuja()
            ''' Tomar medida inicial de tiempo '''
            start = time()
            cycles = sortBurbuja(L_burbuja, sel_mayor_menor.get())
            ''' Tomar medida final de tiempo
                Calcular tiempo de ejecución (t_elapsed)'''
            t_elapsed = time()-start
            graficaDatos.stem(abscisas, L_burbuja, use_line_collection=True)
        elif met.get() == 2:
            if selPaso.get() == 1:
                animacionSeleccion()
            ''' Tomar medida inicial de tiempo '''
            start = time()
            cycles = sortSeleccion(L_seleccion, sel_mayor_menor.get())
            ''' Tomar medida final de tiempo
                Calcular tiempo de ejecución (t_elapsed)'''
            t_elapsed = time()-start
            graficaDatos.stem(abscisas, L_seleccion, use_line_collection=True)
        elif met.get() == 3:
            ''' Tomar medida inicial de tiempo '''
            start = time()
            ''' Aplicar método sort de Python a L_py '''
            if sel_mayor_menor.get() == 1:
                L_py.sort(reverse=True)
            else:
                L_py.sort()
            ''' Tomar medida final de tiempo
                Calcular tiempo de ejecución (t_elapsed)'''
            t_elapsed = time()-start
            cycles = 'No disponible'
            graficaDatos.stem(abscisas, L_py, use_line_collection=True)
            
        print('Time in us: ', t_elapsed)
        print('Algorithm iterations: ', cycles)    
            
        graficaDatos.grid() # Grid on
        canvas.draw()
        res_time.config(text = 'Tiempo: %.2f us' %(t_elapsed*10**6))
        res_cycles.config(text = 'Iteraciones: '+str(cycles))
    except UnboundLocalError:
        popup_msg("No seleccionó un método de ordenamiento")
        return
    except AttributeError:
        popup_msg("No hay valores validos para ordenar")
        return
    except ValueError:
        popup_msg("Verifique los valores a ordenar")
    
'''**** Interfaz grafica ****'''

ANCHO =650
ALTO = 380
ANCHO_DI = 200
ALTO_DI = 150
ANCHO_M = 200
ALTO_M = 200
ANCHO_R = 200
ANCHO_COMBO_SEL = 21
COLUMNAS = ANCHO/8
FILAS = ALTO/6
L_sin_ordenar = []

# Ventana principal
root = Tk() 
root.geometry(str(ANCHO)+'x'+str(ALTO))
root.title("PRACTICA 8")
root.grid(widthInc=ANCHO, heightInc = ALTO)
print(root.grid_size())
root.resizable(width=False, height=False)

# Elementos de la ventana (widgets)

# 1. Frame para entrada de datos
fDataSource = LabelFrame(root, text=" Entrada de datos ")
fDataSource.place(x = ANCHO - ANCHO_DI - 15,y = 15, width = ANCHO_M)
# 1.1. Radio Button para la seleccion de archivo
source_selection = IntVar()
R1 = Radiobutton(fDataSource, text="Desde un archivo", variable = source_selection, value = 1)
R1.pack(side=TOP, anchor=W, expand=YES)
# 1.2. Radio Button para generar elementos aleatoriamente
R2 = Radiobutton(fDataSource, text="Generados aleatoriamente", variable = source_selection, value = 2)
R2.pack(side=TOP, anchor=W, expand=YES)
# 1.3. Separador horizontal
sep = Separator(fDataSource,orient=HORIZONTAL)
sep.pack(side=TOP,fill=X, expand=False)
# 1.4. Boton Select
bSelect = Button(fDataSource,text="Aceptar",width = 17,command = loadInputData)
bSelect.pack(padx = 5, pady = 5, fill = X)

# 2. Frame para la seleccion del método
fMethod = LabelFrame(root, text=" Metodo de ordenamiento ")
fMethod.place(x = ANCHO - ANCHO_M - 15,y = ALTO_DI, width = ANCHO_M)
# 2.1. Radio Button para escoger Burbuja
met = IntVar()
bur = Radiobutton(fMethod, text="Burbuja", variable = met, value = 1)
bur.pack(side=TOP, anchor=W, expand=YES)
# 2.2. Radio Button para escoger Selection sort
sel = Radiobutton(fMethod, text="Selección", variable = met, value = 2)
sel.pack(side=TOP, anchor=W, expand=YES)
# 2.3. Radio Button para escoger Python sort
sel = Radiobutton(fMethod, text="Python", variable = met, value = 3)
sel.pack(side=TOP, anchor=W, expand=YES)
# 2.4. Separador horizontal
sep3 = Separator(fMethod,orient=HORIZONTAL)
sep3.pack(side=TOP,fill=X, expand=False)
# 2.6. Checkbox para seleccionar mayor a menor
sel_mayor_menor = IntVar()
paso = Checkbutton(fMethod, text="Mayor a menor", variable=sel_mayor_menor)
paso.pack(side=TOP, anchor=W, expand=YES)
# 2.5. Checkbox ejecucion paso a paso
selPaso = IntVar()
paso = Checkbutton(fMethod, text="Ver lento", variable=selPaso)
paso.pack(side=RIGHT, anchor=W, expand=YES)
# 2.6. Boton ejecucion de los metodos de ordenacion
bMethod = Button(fMethod,text="Ordenar",command = sortHandler)
bMethod.pack(padx = 5, pady = 5, fill = X)

# 3. Frame con la grafica
f = Figure(figsize=(8,7), dpi=50)
graficaDatos = f.add_subplot(111)
graficaDatos.plot(range(1,len(L_sin_ordenar)+1),L_sin_ordenar)

# 4 Frame resultados
fres = LabelFrame(root, text=" Resultados de rendimiento ")
fres.place(x = ANCHO - ANCHO_DI - 15,y = ALTO_DI+150, width = ANCHO_M)
frame1 = Frame(fres)
res_time = Label(frame1, text = 'Tiempo: ', anchor='w')
res_time.pack(side = LEFT)
frame2 = Frame(fres)
res_cycles = Label(frame2, text = 'Iteraciones: ', anchor='w') 
res_cycles.pack(side = LEFT)
frame1.pack()
frame2.pack()

canvas = FigureCanvasTkAgg(f, master = root) 
canvas._tkcanvas.config(background='white',highlightthickness=1)    
canvas.get_tk_widget().grid(row = 0,column = 0, padx = 10, pady = 10)

root.mainloop()