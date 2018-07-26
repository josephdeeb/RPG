box = {
  size: 5,
  positionX: 0.0,
  positionY: 0.0,
  velocityX: 0.0,
  velocityY: 0.0,
};
ctx = undefined;
canvas = undefined;
MS_PER_UPDATE = 16;
actors = undefined;
canvasWidth = 150;
canvasHeight = 150;
keyUp = false;
keyLeft = false;
keyRight = false;
keyDown = false;

function draw() {
  ctx.fillStyle = "rgb(255, 255, 255)";
  ctx.fillRect(0, 0, canvasWidth, canvasHeight);
  ctx.fillStyle = "rgb(255, 0, 0)";
  ctx.fillRect(Math.round(box.positionX), Math.round(box.positionY), box.size, box.size);
}

function handleInputMovement() {
  if (keyUp && !keyDown) {
    if (box.velocityY <= -2) {
      box.velocityY = -2
    }
    else {
      box.velocityY -= 1;
    }
  }
  else if (keyDown && !keyUp) {
    if (box.velocityY >= 2) {
      box.velocityY = 2;
    }
    else {
      box.velocityY += 1;
    }
  }
  else {
    if (box.velocityY < -1) {
      box.velocityY += 1
    }
    else if (box.velocityY > 1) {
      box.velocityY -= 1
    }
    else {
      box.velocityY = 0
    }
  }

  if (keyLeft && !keyRight) {
    if (box.velocityX <= -2) {
      box.velocityX = -2
    }
    else {
      box.velocityX -= 1;
    }
  }
  else if (keyRight && !keyLeft) {
    if (box.velocityX >= 2) {
      box.velocityX = 2;
    }
    else {
      box.velocityX += 1;
    }
  }
  else {
    if (box.velocityX < -1) {
      box.velocityX += 1
    }
    else if (box.velocityX > 1) {
      box.velocityX -= 1
    }
    else {
      box.velocityX = 0
    }
  }
}

function update() {
  /*
  if (keyUp && !keyDown) {
    if (box.velocity)
    box.velocityY -= 1;
  }

  else if (keyDown && !keyUp) {
    box.velocityY += 1;
  }

  else if (box.velocityY > 0) {
    if (box.velocityY > 0.15) {
      box.velocityY = 0;
    }

    else {
      box.velocityY -= 0.15;
    }
  }

  else if (box.velocityY < 0) {
    if (box.velocityY < -0.15) {
      box.velocityY = 0;
    }

    else {
      box.velocityY += 0.15;
    }
  }

  if (keyLeft && !keyRight) {
    box.velocityX -= 0.10;
  }

  else if (keyRight && !keyLeft) {
    box.velocityX += 0.10;
  }

  else if (box.velocityX > 0) {
    if (box.velocityX > 0.15) {
      box.velocityX = 0;
    }

    else {
      box.velocityX -= 0.15;
    }
  }

  else if (box.velocityX < 0) {
    if (box.velocityX < -0.15) {
      box.velocityX = 0;
    }

    else {
      box.velocityX += 0.15;
    }
  }
  */
  handleInputMovement();

  box.positionX += box.velocityX;
  if (box.positionX > 145) {
    box.positionX = 145;
    box.velocityX = -box.velocityX;
  }
  else if (box.positionX < 0) {
    box.positionX = 0;
    box.velocityX = -box.velocityX;
  }

  box.positionY += box.velocityY;
  if (box.positionY > 145) {
    box.positionY = 145;
    box.velocityY = -box.velocityY;
  }
  else if (box.positionY < 0) {
    box.positionY = 0;
    box.velocityY = -box.velocityY;
  }
}

function start() {
  canvas = document.getElementById('canvas');
  if (canvas.getContext) {
    ctx = canvas.getContext('2d');
  }
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
  requestAnimationFrame(mainLoop);
}

previous = 0
lag = 0

function mainLoop(current) {
  var elapsed = current - previous;
  previous = current;
  lag += elapsed;

  while (lag >= MS_PER_UPDATE) {
    update();
    lag -= MS_PER_UPDATE;
  }

  draw();
  requestAnimationFrame(mainLoop);
}

/*
function mainLoop() {
  update();
  draw();
  requestAnimationFrame(mainLoop);
}
*/
