from views.views import index, data

def setup_routes(app):
    app.router.add_get('/', index)
    app.router.add_get('/1', data)

