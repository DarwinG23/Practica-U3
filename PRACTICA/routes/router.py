from flask import Blueprint, jsonify, abort , request, render_template, redirect, Flask, flash, url_for


from controls.tda.graph.graphNoManagedLabelledDos import GraphNoManagedLabelledDos


from controls.banco.bancoControl import BancoControl
from controls.banco.bancoGrafo import BancoGrafo
from flask_cors import CORS
router = Blueprint('router', __name__)




#CORS(api)
cors = CORS(router, resource={
    r"/*":{
        "origins":"*"
    }
})

#GET: PARA PRESENTAR DATOS
#POST: GUARDA DATOS, MODIFICA DATOS Y EL INICIO DE SESION, EVIAR DATOS AL SERVIDOR

@router.route('/') #SON GETS
def home():
    return render_template('templateP.html')

@router.route('/bancos')
def lista_bancos():
    bc = BancoControl()
    return render_template('bancos/lista.html', lista = bc.to_dic())


@router.route('/grafo')
def grafo():
    return render_template("d3/grafo.html")


@router.route('/bancos/agregar')
def ver_guardar_bancos():
    return render_template('bancos/guardar.html')


@router.route('/bancos/guardar', methods=["POST"])
def guardar_bancos():
    bc = BancoControl()
    data = request.form
    
    bc._banco._nombre = data["nombre"]
    bc._banco._direccion = data["direccion"]
    bc._banco._horario = data["horario"]
    bc._banco._telefono = data["telefono"]
    bc._banco._latitud = data["latitud"]
    bc._banco._longitud = data["longitud"]
    bc.save
        
    return redirect("/bancos", code=302)

@router.route('/bancos/grafo_banco')
def grafo_banco():
    bg = BancoGrafo()
    bg.create_graph()
    return render_template("d3/grafo.html")

@router.route('/grafo_banco/ver')
def ver_grafo_banco():
    return render_template("d3/grafo.html")

@router.route('/bancos/grafo_ver_admin')
def grafo_ver_admin():
    bc = BancoControl()
    grafo = BancoGrafo()._grafo
    
    arrayBancos = bc.to_dic()
    matriz_ady = []

    for i in range(len(arrayBancos)):
        fila = ["-----"] * len(arrayBancos)
        matriz_ady.append(fila)
        
    for i in range(len(arrayBancos)):
        for j in range(len(arrayBancos)):
            if grafo.exist_edge_E(arrayBancos[i]["nombre"], arrayBancos[j]["nombre"]):
                matriz_ady[i][j] = grafo.weight_edges_E(arrayBancos[i]["nombre"], arrayBancos[j]["nombre"])
    
    return render_template("bancos/grafo.html",  lista = bc.to_dic(), matris = matriz_ady)


@router.route('/bancos/crear_ady', methods=["POST"])
def crear_ady():
    bc = BancoControl()
    grafo = BancoGrafo()._grafo
    data = request.form
    origen = data["origen"]
    destino = data["destino"]
    
    if origen == destino:
        flash('Por favor, selecione un destino y origen distintos', 'error')
        return redirect(url_for('router.grafo_ver_admin'))
    

    if grafo.exist_edges(int(origen)-1, int(destino)-1):
        flash('Ya existe una adyacencia entre estos dos bancos', 'error')
    else:
        bancoOrigen = bc._list().binary_search_models(int(origen), "_id")
        bancoDestino = bc._list().binary_search_models(int(destino), "_id")
        
        bg = BancoGrafo()
        bg.create_graph(bancoOrigen, bancoDestino)
       
    
    return redirect("/bancos/grafo_ver_admin", code=302)

@router.route('/bancos/reiniciar')
def reiniciar_grafo():
    bg = BancoGrafo()
    bg.create_graph(None,None,True)
    return redirect("/bancos/grafo_ver_admin", code=302)


@router.route('/bancos/ruta/<origen>/<destino>/<metodo>')
def encontrar_ruta(origen, destino, metodo):
    bg = BancoGrafo()
    bg.create_graph()
    
    if origen == destino:
        flash('Por favor, selecione un destino y origen distintos', 'error')
        return redirect(url_for('router.grafo_ver_admin'))
        
    if bg.BFS():
        if metodo == "1":
            camino = bg.floyd(origen, destino)
        else:
            camino = bg.dijkstra(origen, destino)
        flash(camino, 'error')
        return redirect("/bancos/grafo_ver_admin", code=302)
    else:
        flash('El grafo no está conectado', 'error')
        return redirect("/bancos/grafo_ver_admin", code=302)
    

