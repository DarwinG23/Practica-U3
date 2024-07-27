from flask import Blueprint, jsonify, abort , request, render_template, redirect, Flask, flash, url_for
from controls.personaDaoControl import PersonaDaoControl
from controls.liquido.negocioControl import NegocioControl
from controls.tda.graph.graphNoManagedLabelledDos import GraphNoManagedLabelledDos
from controls.liquido.negocioGrafo import NegocioGrafo
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
    return render_template('template.html')


#LISTA PERSONAS
@router.route('/personas')
def lista_personas():
    pc = PersonaDaoControl()
    return render_template('nene/lista.html', lista=pc.to_dic())

#LISTA PERSONAS
@router.route('/personas/ver')
def ver_personas():
    return render_template('nene/guardar.html')


@router.route('/personas/editar/<pos>')
def ver_editar(pos):
    pd = PersonaDaoControl()
    nene = pd._list().getNode(int(pos)-1)
    print(nene)
    return render_template("nene/editar.html", data = nene )


#GUARDAR PERSONAS
@router.route('/personas/guardar', methods=["POST"])
def guardar_personas():
    pd = PersonaDaoControl()
    data = request.form
    
    if not "apellidos" in data.keys():
        abort(400)
        
    #TODO ...Validar
    pd._persona._apellidos = data["apellidos"]
    pd._persona._nombres = data["nombres"]
    pd._persona._direccion = data["direccion"]
    pd._persona._dni = data["dni"]
    pd._persona._telefono = data["telefono"]
    pd._persona._tipoIdentificacion = "CEDULA"
    pd.save
    return redirect("/personas", code=302)


#MODIFICAR PERSONAS
@router.route('/personas/modificar', methods=["POST"])
def modificar_personas():
    pd = PersonaDaoControl()
    data = request.form
    pos = data["id"]
    print(pos)
    nene = pd._list().getNode(int(pos)-1)   #nene = pd._list().getNode(int(data["id"]) -1)
    
    if not "apellidos" in data.keys():
        abort(400)
        
    #TODO ...Validar
    pd._persona = nene
    pd._persona._apellidos = data["apellidos"]
    pd._persona._nombres = data["nombres"]
    pd._persona._direccion = data["direccion"]
    pd._persona._dni = data["dni"]
    pd._persona._telefono = data["telefono"]
    pd._persona._tipoIdentificacion = "CEDULA"

    pd.merge(int(pos)-1)
    return redirect("/personas", code=302)



@router.route('/grafo')
def grafo():
    return render_template("d3/grafo.html")


#LISTA PERSONAS
@router.route('/negocios')
def lista_negocios():
    nc = NegocioControl()
    return render_template('liquido/lista.html', lista=nc.to_dic())


@router.route('/negocios/agregar')
def ver_guardar_negocios():
    return render_template('liquido/guardar.html')


@router.route('/negocios/guardar', methods=["POST"])
def guardar_negocios():
    nc = NegocioControl()
    data = request.form
    
    nc._negocio._nombre = data["nombre"]
    nc._negocio._direccion = data["direccion"]
    nc._negocio._horario = data["horario"]
    nc._negocio._longitud = data["longitud"]
    nc._negocio._latitud = data["latitud"]
    nc.save
        
    return redirect("/negocios", code=302)

@router.route('/negocios/grafo_negocio')
def grafo_negocio():
    ng = NegocioGrafo()
    ng.create_graph()
    return render_template("d3/grafo.html")

@router.route('/grafo_negocio/ver')
def ver_grafo_negocio():
    return render_template("d3/grafo.html")

@router.route('/negocios/grafo_ver_admin')
def grafo_ver_admin():
    nc = NegocioControl()
    grafo = NegocioGrafo()._grafo
    
    arrayNegocios = nc.to_dic()
    matriz_ady = []

    for i in range(len(arrayNegocios)):
        fila = ["-----"] * len(arrayNegocios)
        matriz_ady.append(fila)
        
    for i in range(len(arrayNegocios)):
        for j in range(len(arrayNegocios)):
            if grafo.exist_edge_E(arrayNegocios[i]["nombre"], arrayNegocios[j]["nombre"]):
                matriz_ady[i][j] = grafo.weight_edges_E(arrayNegocios[i]["nombre"], arrayNegocios[j]["nombre"])
    
    return render_template("liquido/grafo.html",  lista = nc.to_dic(), matris = matriz_ady)

@router.route('/negocios/crear_ady', methods=["POST"])
def crear_ady():
    nc = NegocioControl()
    grafo = NegocioGrafo()._grafo
    data = request.form
    origen = data["origen"]
    destino = data["destino"]
    
    if origen == destino:
        flash('Por favor, selecione un destino y origen distintos', 'error')
        return redirect(url_for('router.grafo_ver_admin'))
    

    if grafo.exist_edges(int(origen)-1, int(destino)-1):
        flash('Ya existe una adyacencia entre estos dos negocios', 'error')
    else:
        negocioOrigen = nc._list().binary_search_models(int(origen), "_id")
        negocioDestino = nc._list().binary_search_models(int(destino), "_id")
        
        ng = NegocioGrafo()
        ng.create_graph(negocioOrigen, negocioDestino)
       
    
    return redirect("/negocios/grafo_ver_admin", code=302)

@router.route('/negocios/reiniciar')
def reiniciar_grafo():
    ng = NegocioGrafo()
    ng.create_graph(None,None,True)
    return redirect("/negocios/grafo_ver_admin", code=302)
