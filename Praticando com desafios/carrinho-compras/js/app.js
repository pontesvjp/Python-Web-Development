let total = 0;
document.getElementById("lista-produtos").innerHTML = 0;
document.getElementById("valor-total").innerHTML = "R$ 0";

function adicionar() {
  let produto = document.getElementById("produto").value;
  let nomeProduto = produto.split("-")[0];
  let valor = produto.split("R$")[1];
  let quantidade = document.getElementById("quantidade").value;
  let preco = quantidade * valor;
  let carrinho = document.getElementById("lista-produtos");
  carrinho.innerHTML = carrinho.innerHTML + `<section class="carrinho__produtos__produto">
  <span class="texto-azul">${quantidade}x</span> ${nomeProduto}`;

  total = total + preco;
  let campoTotal = document.getElementById("valor-total");
  campoTotal.textContent = `R$ ${total}`;
}
function limpar() {}
