var nodes = new vis.DataSet([{id: 1,label:"Banco de LOJA - Agencia UNL"},
{id: 2,label:"PuntoBB Banco Bolivariano"},
{id: 3,label:"Agencia Banco de Loja"},
{id: 4,label:"CoopMego"},
{id: 5,label:"BanEcuador"},
]);
var edges = new vis.DataSet([{from: 1,to:3,label:"6.409"},
{from: 1,to:2,label:"2.491"},
{from: 2,to:1,label:"2.491"},
{from: 2,to:3,label:"3.924"},
{from: 2,to:4,label:"1.745"},
{from: 3,to:1,label:"6.409"},
{from: 3,to:2,label:"3.924"},
{from: 4,to:2,label:"1.745"},
{from: 4,to:5,label:"0.739"},
{from: 5,to:4,label:"0.739"},
]);
var container = document.getElementById("mynetwork"); var data = {nodes: nodes,edges: edges,};var options = {};var network = new vis.Network(container, data, options);