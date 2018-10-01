function start() {
    
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
