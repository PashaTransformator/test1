html = '''<!DOCTYPE html>
<html>
    <head>
        <title>Wep Page from send messages</title>
        <meta http-equiv="Content-Type" content="text/html; charset=utf-8">
    </head>
<body>
    <h1>Отправка сообщений и их подсчет</h1>
    <form action="" onsubmit="sendMessage(event)">
        <input type="text" id="messageText"/>
        <button>Отправить</button>
    </form>
        <ol id='messages'>
        <ol id='messages'>
        </ol>
    <script>
    var ws = new WebSocket("ws://localhost:8000/ws");
    ws.onmessage = function(event) {
        var messages = document.getElementById('messages')
        var message = document.createElement('li')
        var content = document.createTextNode(event.data)
        message.appendChild(content)
        messages.appendChild(message)
        };
        function sendMessage(event) {
           var input = document.getElementById("messageText")
           var msg = {
               type: "message",
               text: input.value,
               date: Date.now()
  };
           ws.send(JSON.stringify(msg))
           input.value = ''
           event.preventDefault()
           }
  </script>
</body>
</html>'''