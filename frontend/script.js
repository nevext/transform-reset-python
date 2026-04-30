let vetorInicial = null;
let vetorAtual = null;
let transformado = false;
let eixoSelecionado = 'x';

function selecionarEixo(eixo) {
  eixoSelecionado = eixo;
  document.querySelectorAll('.btn-eixo').forEach(b => b.classList.remove('active'));
  document.getElementById('eixo-' + eixo).classList.add('active');
}

function obterVetorInicial() {
  const x = parseFloat(document.getElementById('input-x').value);
  const y = parseFloat(document.getElementById('input-y').value);
  if (isNaN(x) || isNaN(y)) {
    alert('Digite valores validos para X e Y.');
    return null;
  }
  return [x, y];
}

function verificarBloqueio() {
  if (transformado) {
    document.getElementById('aviso-bloqueio').style.display = 'block';
    return true;
  }
  return false;
}

function aplicarTransformacao(matriz, nomeAcao, descricao) {
  if (verificarBloqueio()) return;

  const v = obterVetorInicial();
  if (!v) return;

  vetorInicial = v;
  const [x, y] = v;
  const [[a, b], [c, d]] = matriz;

  const novoX = a * x + b * y;
  const novoY = c * x + d * y;

  vetorAtual = [
    Math.round(novoX * 100) / 100,
    Math.round(novoY * 100) / 100
  ];

  transformado = true;

  mostrarResultado(nomeAcao, descricao, [a, b, c, d], [x, y], vetorAtual);
  bloquearCards();

  document.getElementById('btn-reset').style.display = 'block';
  document.getElementById('aviso-bloqueio').style.display = 'none';
}

function aplicarGirar() {
  const graus = parseFloat(document.getElementById('input-graus').value);
  if (isNaN(graus)) { alert('Digite um angulo valido.'); return; }
  const rad = graus * Math.PI / 180;
  const cos = Math.cos(rad);
  const sin = Math.sin(rad);
  aplicarTransformacao(
    [[cos, -sin], [sin, cos]],
    `girou ${graus}`,
    `Rotacao de ${graus} graus\n\nMatriz:\n| ${fmt(cos)}  ${fmt(-sin)} |\n| ${fmt(sin)}   ${fmt(cos)} |`
  );
}

function aplicarEsticar() {
  const sx = parseFloat(document.getElementById('input-sx').value);
  const sy = parseFloat(document.getElementById('input-sy').value);
  if (isNaN(sx) || isNaN(sy)) { alert('Digite valores validos para a escala.'); return; }
  aplicarTransformacao(
    [[sx, 0], [0, sy]],
    `foi esticado (${sx}x, ${sy}x)`,
    `Escala: ${sx}x em X e ${sy}x em Y\n\nMatriz:\n| ${sx}  0 |\n| 0  ${sy} |`
  );
}

function aplicarEspelhar() {
  let matriz, nomeEixo;
  if (eixoSelecionado === 'x') {
    matriz = [[1, 0], [0, -1]];
    nomeEixo = 'no eixo X';
  } else if (eixoSelecionado === 'y') {
    matriz = [[-1, 0], [0, 1]];
    nomeEixo = 'no eixo Y';
  } else {
    matriz = [[-1, 0], [0, -1]];
    nomeEixo = 'na origem';
  }
  const [[a, b], [c, d]] = matriz;
  aplicarTransformacao(
    matriz,
    `foi espelhado ${nomeEixo}`,
    `Reflexao ${nomeEixo}\n\nMatriz:\n| ${a}  ${b} |\n| ${c}   ${d} |`
  );
}

function fmt(n) {
  return (Math.round(n * 1000) / 1000).toFixed(2);
}

function mostrarResultado(nomeAcao, descricao, [a, b, c, d], [x, y], resultado) {
  const secao = document.getElementById('section-resultado');
  secao.style.display = 'block';

  const [rx, ry] = resultado;

  document.getElementById('resultado-texto').innerHTML =
    `O ponto (${x}, ${y}) <span class="destaque-acao">${nomeAcao}</span> e virou <span class="destaque-valor">(${rx}, ${ry})</span>`;

  const calculo =
    `x' = (${fmt(a)} x ${x}) + (${fmt(b)} x ${y})\n` +
    `x' = ${rx}\n\n` +
    `y' = (${fmt(c)} x ${x}) + (${fmt(d)} x ${y})\n` +
    `y' = ${ry}\n\n` +
    `Vetor final: (${rx}, ${ry})`;

  document.getElementById('calculo-texto').textContent = descricao + '\n\nCalculo:\n' + calculo;

  desenharCanvas([x, y], resultado);
}

function bloquearCards() {
  document.querySelectorAll('.transform-card').forEach(c => c.classList.add('bloqueado'));
}

function desbloquearCards() {
  document.querySelectorAll('.transform-card').forEach(c => c.classList.remove('bloqueado'));
}

function toggleCalculo() {
  const box = document.getElementById('calculo-box');
  const arrow = document.getElementById('calculo-arrow');
  const visivel = box.style.display !== 'none';
  box.style.display = visivel ? 'none' : 'block';
  arrow.textContent = visivel ? '+' : '-';
}

function resetar() {
  transformado = false;
  vetorInicial = null;
  vetorAtual = null;

  document.getElementById('section-resultado').style.display = 'none';
  document.getElementById('aviso-bloqueio').style.display = 'none';
  document.getElementById('btn-reset').style.display = 'none';
  document.getElementById('calculo-box').style.display = 'none';
  document.getElementById('calculo-arrow').textContent = '+';

  desbloquearCards();
}

function desenharCanvas(original, transformado) {
  const canvas = document.getElementById('canvas');
  const ctx = canvas.getContext('2d');
  const W = canvas.width;
  const H = canvas.height;

  ctx.clearRect(0, 0, W, H);

  const margem = 50;
  const areaW = W - margem * 2;
  const areaH = H - margem * 2;

  const todos = [original, transformado, [0, 0]];
  const xs = todos.map(p => p[0]);
  const ys = todos.map(p => p[1]);
  const maxAbs = Math.max(
    Math.abs(Math.max(...xs)), Math.abs(Math.min(...xs)),
    Math.abs(Math.max(...ys)), Math.abs(Math.min(...ys)),
    1
  ) * 1.3;

  function toCanvas(px, py) {
    return [
      margem + ((px + maxAbs) / (2 * maxAbs)) * areaW,
      margem + ((maxAbs - py) / (2 * maxAbs)) * areaH
    ];
  }

  const origem = toCanvas(0, 0);

  // grade
  ctx.strokeStyle = '#e8eaed';
  ctx.lineWidth = 1;
  const passo = Math.ceil(maxAbs / 4);
  for (let v = -Math.ceil(maxAbs); v <= Math.ceil(maxAbs); v += passo) {
    const [gx] = toCanvas(v, 0);
    const [, gy] = toCanvas(0, v);
    ctx.beginPath(); ctx.moveTo(gx, margem); ctx.lineTo(gx, H - margem); ctx.stroke();
    ctx.beginPath(); ctx.moveTo(margem, gy); ctx.lineTo(W - margem, gy); ctx.stroke();
  }

  // eixos
  ctx.strokeStyle = '#9ca3af';
  ctx.lineWidth = 1.5;
  ctx.beginPath(); ctx.moveTo(margem, origem[1]); ctx.lineTo(W - margem, origem[1]); ctx.stroke();
  ctx.beginPath(); ctx.moveTo(origem[0], margem); ctx.lineTo(origem[0], H - margem); ctx.stroke();

  // labels eixos
  ctx.fillStyle = '#9ca3af';
  ctx.font = '13px DM Sans, sans-serif';
  ctx.fillText('x', W - margem + 6, origem[1] + 4);
  ctx.fillText('y', origem[0] - 14, margem - 6);
  ctx.fillText('0', origem[0] + 5, origem[1] + 14);

  // vetor original (azul)
  desenharVetor(ctx, origem, toCanvas(...original), '#185FA5', `Ponto de partida (${original[0]}, ${original[1]})`);

  // vetor transformado (verde)
  desenharVetor(ctx, origem, toCanvas(...transformado), '#1D9E75', `resultado (${transformado[0]}, ${transformado[1]})`);
}

function desenharVetor(ctx, origem, destino, cor, label) {
  const [ox, oy] = origem;
  const [dx, dy] = destino;

  const angulo = Math.atan2(dy - oy, dx - ox);
  const tamanhoSeta = 10;

  ctx.strokeStyle = cor;
  ctx.fillStyle = cor;
  ctx.lineWidth = 2.5;

  ctx.beginPath();
  ctx.moveTo(ox, oy);
  ctx.lineTo(dx, dy);
  ctx.stroke();

  // seta
  ctx.beginPath();
  ctx.moveTo(dx, dy);
  ctx.lineTo(dx - tamanhoSeta * Math.cos(angulo - 0.4), dy - tamanhoSeta * Math.sin(angulo - 0.4));
  ctx.lineTo(dx - tamanhoSeta * Math.cos(angulo + 0.4), dy - tamanhoSeta * Math.sin(angulo + 0.4));
  ctx.closePath();
  ctx.fill();

  // ponto
  ctx.beginPath();
  ctx.arc(dx, dy, 5, 0, Math.PI * 2);
  ctx.fill();

  // label
  ctx.font = '12px DM Sans, sans-serif';
  ctx.fillText(label, dx + 10, dy - 8);
}