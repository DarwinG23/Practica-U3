var nodes = new vis.DataSet([{id: 1,label:"Banco de LOJA - Agencia UNL"},
{id: 2,label:"PuntoBB Banco Bolivariano"},
{id: 3,label:"Agencia Banco de Loja"},
]);
var edges = new vis.DataSet([{from: 1,to:3,label:"6.409"},
{from: 1,to:2,label:"2.491"},
{from: 2,to:1,label:"2.491"},
{from: 2,to:3,label:"3.924"},
{from: 3,to:1,label:"6.409"},
{from: 3,to:2,label:"3.924"},
]);
var container = document.getElementById("mynetwork"); var data = {nodes: nodes,edges: edges,};var options = {};var network = new vis.Network(container, data, options);