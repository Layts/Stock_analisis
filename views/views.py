from aiohttp import web


async def index(request):
    return web.Response(text='Hello Aiohttp!')

async def data(request):
    return web.Response(text='Pandas')

async def kanboard(request):
    return render_template('hello.html', name=name)


