from aiohttp import web
import aiohttp_jinja2
from ds import stock as ds
from PIL import Image, ImageDraw
import base64

@aiohttp_jinja2.template('test.html')
async def index(request):
    return {'name':ds.Stocks(ds.ticker, ds.start_date).plot()}



async def data(request):
    # figfile = BytesIO()
    # plt.savefig(figfile, format='png')
    # figfile.seek(0)
    # figdata_png = base64.b64encode(figfile.getvalue())
    image = ds.Stocks(ds.ticker,ds.start_date).plot()
    print(image)
    img = base64.b64encode(image)
    response = aiohttp_jinja2.render_template('test.html',
                                              request,
                                              {'result': img})
    return response
    # return web.Response(body=image, content_type='image/jpg')

# @aiohttp_jinja2.template('test.html')
# async def kanboard(request):
#     return render_template('hello.html', name=name)


