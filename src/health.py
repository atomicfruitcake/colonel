"""!
@author atomicfruitcake

@date 2019
"""

async def health_check(req):
    req.response(200, b'OK')
