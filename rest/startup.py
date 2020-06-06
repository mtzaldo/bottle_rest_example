from bottle import Bottle, run

from apps import TodoApp, PostApp, UserApp

app = Bottle()

app.mount('v1/todos', TodoApp())
app.mount('v1/posts', PostApp())
app.mount('v1/users', UserApp())

run(app, host='0.0.0.0', port=8080)