from aiohttp import web
import aiohttp_jinja2
from ds import stock as ds

@aiohttp_jinja2.template('test.html')
async def index(request):
    return {'name':ds.Stocks(ds.ticker, ds.start_date).plot()}



@aiohttp_jinja2.template('test.html')
async def data(request):
    return web.Response(text='Pandas')

# @aiohttp_jinja2.template('test.html')
# async def kanboard(request):
#     return render_template('hello.html', name=name)


