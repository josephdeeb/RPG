// object has x, y, dx, dy

function defaultGameObjectMove(input) {
    // 0001 is up
    // 0010 is right
    // 0100 is down
    // 1000 is left

    if (input == 0) {
        if (this.velX >= this.frictionFactor) {
            this.velX -= this.frictionFactor;
        } else if (this.velX <= -this.frictionFactor) {
            this.velX += this.frictionFactor;
        } else {
            this.velX = 0;
        }
    }

    if ((input & 1) != 0) {
        if (this.accelY >= maxVel) {

        }
    }
}


function gameObjectConstructor(x = 0, y = 0) {
    this.x = x;
    this.y = y;
    this.velX = 0;
    this.velY = 0;
    this.accelX = 0;
    this.accelY = 0;
    this.accelFactor = 2;
    this.frictionFactor = 1;
    this.maxVel = 6
}
