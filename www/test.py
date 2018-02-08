import www.orm as orm
from www.models import User
import asyncio


async def test(loop):
    await orm.create_pool(loop=loop, user='root', passwd='Phy@hello123', db='awesome', host='39.106.188.182', port=3389)
    u = User(name='Pei', email='pei@163.com', passwd='123456', image='about:blank')
    await u.save()

loop = asyncio.get_event_loop()
loop.run_until_complete(test(loop))
loop.close()



