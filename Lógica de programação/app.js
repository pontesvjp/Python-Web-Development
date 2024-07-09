alert("Boas vindas ao jogo do numero secreto");
let numeroMaximo = 5000;
let numeroSecreto = parseInt(Math.random() * numeroMaximo + 1);
console.log(numeroSecreto);
let chute;
let tentativas = 1;

while (chute != numeroSecreto) {
  chute = prompt(`Escolha um número entre 1 e ${numeroMaximo}`);
  if (chute == numeroSecreto) { 
    break; 
  } else {
    if (chute > numeroSecreto) {
      alert(`o numero secreto eh menor ${chute}`);
    } else {
      alert(`o numero secreto eh maior ${chute}`);
    }
    //tentativas = tentantivas +1
    tentativas++;
  }
}
let palavraTentativa = tentativas > 1 ? "tentativas" : "tentativa";
alert(
  `Isso ai! Você descobriu o número secreto ${numeroSecreto} com ${tentativas} ${palavraTentativa}.`
);
