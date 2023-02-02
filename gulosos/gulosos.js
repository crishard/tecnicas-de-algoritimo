var itens = [
    { id: 1, nome: "item1", peso: 6, valor: 30 },
    { id: 2, nome: "item2", peso: 3, valor: 14 },
    { id: 3, nome: "item3", peso: 4, valor: 16 },
    { id: 4, nome: "item4", peso: 2, valor: 9 },
    { id: 5, nome: "item5", peso: 5, valor: 20 }
];

var contadorMochila = 0;
var selecionados = [];
var max;
var valorMochila = 0;

const capacidade = 12;

var removeByAttr = function (arr, attr, value) {
    var i = arr.length;
    while (i--) {
        if (
            arr[i] &&
            arr[i].hasOwnProperty(attr) &&
            (arguments.length > 2 && arr[i][attr] === value)
        ) {
            arr.splice(i, 1);
        }
    }
};

do {
    max = itens.reduce(function (anterior, atual) {
        return anterior.valor > atual.valor ? anterior : atual;
    });

    if (max.peso + contadorMochila <= capacidade) {
        selecionados.push(max);
        contadorMochila += max.peso;
        valorMochila += max.valor;
        removeByAttr(itens, "id", max.id);
    } else {
        removeByAttr(itens, "id", max.id);
    }
} while (capacidade > contadorMochila && itens.length > 0);

console.log("O valor total na mochila: ",valorMochila);
console.log("itens Selecionados: ",selecionados);