
from MyFirstApi.app import create_app

app = create_app()
app.run(debug=True, port=4545)