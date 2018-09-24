// object has x, y, dx, dy

function defaultGameObjectMove(input) {
    // 0001 is up
    // 0010 is right
    // 0100 is down
    // 1000 is left
    var newVelY = 0;
    var newVelX = 0;

    if ((input & 1 != 0) | (input == 0)) {
        if ((input & 4 != 0) | (input == 0)) {
            // No force in y plane...
            if (this.velY != 0) {
                // Our Y velocity is not zero so thus we must slow it down
                if (this.velY > 0) {
                    // If our Y velocity is greater than zero than we subtract friction from the Y velocity...
                    newVelY = this.velY - this.friction;
                    if (newVelY < 0) {
                        // If we slow down past zero, just go to zero (if our Y velocity is 0.5 and friction is 1, go to 0 not -0.5)
                        newVelY = 0;
                    }
                    // Set our Y velocity
                    this.velY = newVelY;
                } else if (this.velY < 0) {
                    // If our Y velocity is less than zero, we need to add friction to the Y velocity...
                    newVelY = this.velY + this.friction;
                    if (newVelY > 0) {
                        // If we slow down past zero, just go to zero
                        newVelY = 0;
                    }
                    // Set our Y velocity
                    this.velY = newVelY;
                }
            }
        } else {
            // Force up in y plane
            newVelY = this.velY + this.accel;
            if (newVelY > this.maxVel) {
                // If our new velocity is greater than our max velocity, then don't go past our max velocity
                newVelY = this.maxVel;
            }
            this.velY = newVelY;
        }
    } else if (input & 4 != 0) {
        // force down in Y plane
        newVelY = self.velY - self.accel;
        if (newVelY = -self.maxSpeed) {
            newVelY = -self.maxSpeed;
        }
        self.velY = newVelY;
    }

    if ((input & 2 != 0) | (input == 0)) {
        if ((input & 8 != 0) | (input == 0)) {
            // No force in X plane...
            if (this.velX != 0) {
                if (this.velX > 0) {
                    newVelX = this.velX - this.friction;
                    if (newVelX < 0) {
                        newVelX = 0;
                    }
                    this.velX = newVelX;
                } else if (this.velX < 0) {
                    newVelX = this.velX + this.friction;
                    if (newVelX > 0) {
                        newVelX = 0;
                    }
                    this.velX = newVelX;
                }
            }
        } else {
            // Force right in X plane
            newVelX = this.velX + this.accel;
            if (newVelX > this.maxVel) {
                newVelX = this.maxVel;
            }
            this.velX = newVelX;
        }
    } else if (input & 8 != 0) {
        // force left in X plane
        newVelX = self.velX - self.accel;
        if (newVelX = -self.maxSpeed) {
            newVelX = -self.maxSpeed;
        }
        self.velX = newVelX;
    }


}


function gameObjectConstructor(x = 0, y = 0) {
    this.x = x;
    this.y = y;
    this.velX = 0;
    this.velY = 0;
    this.accel = 2;
    this.friction = 1;
    this.maxVel = 5
}
