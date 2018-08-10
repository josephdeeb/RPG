websocket = false

function initialize() {
    websocket = new WebSocket("ws://127.0.0.1:6789/");
    websocket.onmessage = function (event) {
        data = JSON.parse(event.data);
        beings = data.beings
        document.getElementsByTagName('body')[0].innerHTML = data
    }
}
