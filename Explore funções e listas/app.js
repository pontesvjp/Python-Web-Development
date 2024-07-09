let listaDeNumeroSorteados = [];
let limiteMaximo = 10;
let numeroCorreto = gerarNumeroAleatorio();
let tentativas = 1;

function exibirTextoNaTela(tag, texto) {
  let campo = document.querySelector(tag);
  campo.innerHTML = texto;
  // responsiveVoice.speak(texto, "Brazilian Portuguese Female", { rate: 1.2 });
}
function exibirMensagemInicial() {
  exibirTextoNaTela("h1", "Jogo do numero secreto");
  exibirTextoNaTela("p", `Escolha um numero entre 1 e ${limiteMaximo}`);
}

exibirMensagemInicial();
function verificarChute() {
  let chute = document.querySelector("input").value;

  if (chute == numeroCorreto) {
    exibirTextoNaTela("h1", "Parabéns, você acertou!");
    let palavraTentativa = tentativas > 1 ? "tentativas" : "tentativa";
    let mensagem = `Voce descobriu o número secreto com ${tentativas} ${palavraTentativa}! `;
    exibirTextoNaTela("p", mensagem);
    document.getElementById("reiniciar").removeAttribute("disabled");
  } else {
    if (chute > numeroCorreto) {
      exibirTextoNaTela("h1", "Errou");
      exibirTextoNaTela("p", `O número secreto é menor que ${chute}`);
    } else {
      exibirTextoNaTela("h1", "Errou");
      exibirTextoNaTela("p", `O número secreto é maior que ${chute}`);
    }
    tentativas++;
    limparCampo();
  }
}

function gerarNumeroAleatorio() {
  let numeroEscolhido = parseInt(Math.random() * limiteMaximo + 1);
  let quantidadeDeElementosNaLista = listaDeNumeroSorteados.length;

  if (quantidadeDeElementosNaLista == limiteMaximo) {
    listaDeNumeroSorteados = [];
  }

  if (listaDeNumeroSorteados.includes(numeroEscolhido)) {
    return gerarNumeroAleatorio();
  } else listaDeNumeroSorteados.push(numeroEscolhido);
  console.log(listaDeNumeroSorteados);
  return numeroEscolhido;
}

function limparCampo() {
  chute = document.querySelector("input");
  chute.value = "";
}

function reiniciarJogo() {
  numeroCorreto = gerarNumeroAleatorio();
  limparCampo();
  tentativas = 1;
  exibirMensagemInicial();
  document.getElementById("reiniciar").setAttribute("disabled", true);
}
