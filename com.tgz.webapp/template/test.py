import orm, asyncio
from models import User, Blog, Comment
"""

async def test(loop):
    await orm.create_pool(loop=loop, user='root', password='root', database='webapp')
    u = User(name='Test', email='790015081@qq.com', passwd='123123', image='about:blank')
    await u.save()

if __name__ == '__main__':
    loop = asyncio.get_event_loop()
    loop.run_until_complete(test(loop))
    loop.run_forever()
"""