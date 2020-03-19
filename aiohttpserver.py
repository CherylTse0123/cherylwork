#!/usr/bin/env python 
# -*- coding:utf-8 -*-
import asyncio

from aiohttp import web

async def index(request):
    await asyncio.sleep(0.5)
    return web.Response(text='<h1>Index</h1>',content_type='text/html')

async def hello(request):
    await asyncio.sleep(0.5)
    text = '<h1>hello, %s!</h1>' % request.match_info['name']
    return web.Response(text=text,content_type='text/html')


if __name__ == '__main__':

    app = web.Application()
    app.router.add_route('GET', '/', index)
    app.router.add_route('GET', '/hello/{name}', hello)
    web.run_app(app)

