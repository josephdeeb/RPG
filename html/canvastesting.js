keyUp = false;
keyLeft = false;
keyRight = false;
keyDown = false;
ctx = undefined;
actors = undefined;
canvasWidth = 150;
canvasHeight = 150;
MS_PER_UPDATE = 16;
previous = undefined;
lag = 0.0;

function initializeCtx() {
  var canvas = document.getElementById('canvas');
  if (canvas.getContext) {
    var ctx = canvas.getContext('2d');
    return ctx;
  }
}

function initializeActors() {
  var player = {size: 5, velocity: [0, 0], position: [0, 0], name: "player", color: "rgb(255, 0, 0)"};
  var player2 = {size: 10, velocity: [0, 0], position: [20, 20], name: "player2", color: "rgb(255, 0, 0)"};
  return [player, player2];
}

function init() {
  ctx = initializeCtx();
  actors = initializeActors();
}

function handleInput() {
  if (keyUp) {
    actors[0].velocity[1] += 1
  }
  if (keyLeft) {
    actors[0].velocity[0] -= 1
  }
  if (keyRight) {
    actors[0].velocity[0] += 1
  }
  if (keyDown) {
    actors[1].velocity[1] -= 1
  }
}


function update() {
  for (var i = 0; i < actors.length; i++) {
    alert(actors[i].position);
    actors[i].position[0] += actors[i].velocity[0];
    actors[i].position[1] += actors[i].velocity[1];
    alert(actors[i].position);

    if ((actors[i].position[0] >= (canvasWidth - actors[i].size)) || (actors[i].position[0] < canvasWidth)) {
      actors[i].position[0] = canvasWidth;
      actors[i].velocity[0] = 0;
    }

    if ((actors[i].position[1] >= (canvasHeight - actors[i].size)) || (actors[i].position[1] < canvasWidth)) {
      actors[i].position[1] = canvasHeight;
      actors[i].velocity[1] = 0;
    }
  }
}

/*
function update() {
  actors[0].position[0] += actors[0].velocity[0];
  actors[0].position[1] += actors[0].velocity[1];

  if ((actors[0].position[0] >= (canvasWidth - actors[0].size)) || (actors[i].position[0] < canvasWidth))
}
*/

function gameLoop() {
  handleInput();
  update();
  draw();
  requestAnimationFrame(gameLoop);
}

/*
// Taken from http://gameprogrammingpatterns.com/game-loop.html
function gameLoop(current) {
  var elapsed = current - previous;
  previous = current;
  lag += elapsed;

  handleInput();

  while (lag >= MS_PER_UPDATE) {
    update();
    lag -= MS_PER_UPDATE;
  }

  draw();
  window.requestAnimationFrame(gameLoop);
}
*/

function getCorner(actor) {
  return [Math.floor(actor.position[0] / 2), Math.floor(actor.position[1] / 2)];
}

function draw() {
  for (var i = 0; i < actors.length; i++) {
    ctx.fillStyle = actors[i].color;
    ctx.fillRect(actors[i].position[0], actors[i].position[1], actors[i].size, actors[i].size);
  }
}

function testInitialize() {
  document.addEventListener("keydown", function(event) {
    var key = event.keyCode
    switch(key) {
      case 87:
        keyUp = true;
        break;
      case 65:
        keyLeft = true;
        break;
      case 68:
        keyRight = true;
        break;
      case 83:
        keyDown = true;
        break;
    }
  })

  document.addEventListener("keyup", function(event) {
    var key = event.keyCode
    switch(key) {
      case 87:
        keyUp = false;
        break;
      case 65:
        keyLeft = false;
        break;
      case 68:
        keyRight = false;
        break;
      case 83:
        keyDown = false;
        break;
    }
  })

  ctx = initializeCtx();
  actors = initializeActors();
  previous = Date.now();
  gameLoop();
}
