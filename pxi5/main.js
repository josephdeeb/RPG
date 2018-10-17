function start() {

}

class Object {
    constructor(collisionBody, velX, velY, sprite) {
        this.collisionBody = collisionBody;
        this.velX = velX;
        this.velY = velY;
        this.sprite = sprite;
    }

    update() {
        this.collisionBody.x += this.velX;
        this.collisionBody.y += this.velY;
    }
}

class Map {
    constructor(width, height, objects=[], system=new Collisions()) {
        this.width = width;
        this.height = height;
        this.objects = objects;

        this.system = new Collisions();
        this.result = system.createResult();
        this.changes = {'REMOVE' = [], 'ADD' = []};
    }

    update() {
        // If we are supposed to remove bodies...
        if (this.changes['REMOVE'].length != 0) {
            // For each body, starting at the top of the stack...
            for (i = changes['REMOVE'].length; i > 0; i--) {
                // Remove the body
                system.remove(changes['REMOVE'][i]);
                // Pop it from the remove stack
                this.changes['REMOVE'].pop()
            }
        }

        // If we are supposed to add bodies...
        if (this.changes['ADD'].length != 0) {
            // For each body, starting at the top of the stack...
            for (i = changes['ADD'].length; i > 0; i--) {
                // Add the body
                system.insert(changes['ADD'][i]);
                // Pop it from the add stack
                this.changes['ADD'].pop()
            }
        }

        // Now any bodies that were supposed to be removed have been removed and any bodies that were supposed to be added have been added

        // Update each object in the Map
        for (i = 0; i < objects.length; i++) {
            objects[i].update();
        }

        // Update the system for each change we've made
        this.system.update();

        // Now check for collisions between all bodies
    }
}


/*
function start() {
    // Aliases
    let Application = PIXI.Application,
        loader = PIXI.loader,
        resources = PIXI.loader.resources,
        Sprite = PIXI.Sprite;

    let app = new Application({width: 256, height: 256});

    document.body.appendChild(app.view);

    // To load more than one image at a time, just "chain" .add() statements. For example, PIXI.loader.add("file1").add("file2").add("file3").load(setup);
    // Alternatively, use an array to load multiple images.  Example, PIXI.loader.add(["file1","file2","file3"]).load(setup);
    // You can also use the loader to load JSON files
    loader.add("assets/smiley.png").load(setup);

    function setup() {
        // this code is run when the loader has finished loading the image
        // This is how you create a sprite (reference the texture in the loader)
        let sprite = new Sprite(resources["assets/smiley.png"].texture);

        // Represents the top left corner of the sprite
        sprite.x = 96;
        sprite.y = 96;

        // Add the sprite to the stage to make it visible
        app.stage.addChild(sprite);
        // To remove a sprite, use app.stage.removeChild(sprite)
        // To simply make it invisible, set its visible property to false.  For example, sprite.visible = false;
    }

    // Textures are stored in PIXI.utils.TextureCachce
    // To reference a loaded texture, use texturecache.  Example, PIXI.utils.TextureCache["assets/smiley.png"];
    // Use an alias to acccess it though.  Example, let TextureCache = PIXI.utils.TextureCache;  then just use TextureCache[file] to access a texture.
    // Default aliases:
    /*
    let Application = PIXI.Application,
        loader = PIXI.loader,
        resources = PIXI.loader.resources,
        Sprite = PIXI.Sprite;
    */
*/


/*
    let type = "WebGL"
    if(!PIXI.utils.isWebGLSupported()){
        type = "canvas"
    }

    PIXI.utils.sayHello(type)
*/
}
