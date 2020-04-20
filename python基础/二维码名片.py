from segno import helpers

qr = helpers.make_mecard(
    name='pyhui',
    email='1111111@qq.com',
    phone='110'
)

qr.save('pyhui电话.png', scale=10)
