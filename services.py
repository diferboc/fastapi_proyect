from models import Producto
fake_db = {
    1 : Producto(nombre="manzana",precio=1000),
    2 : Producto(nombre="banana",precio=1000),
    3 : Producto(nombre="naranja",precio=1000)
}

def obtener_todos_los_productos():
    return fake_db

def obtener_productos_por_id(product_id:int):
    return fake_db.get(product_id)

def crear_producto(producto: Producto):
    nuevo_id = max(fake_db.keys()) + 1
    fake_db[nuevo_id] = producto
    return nuevo_id    

def actualizar_producto(producto_id:int, producto_actualizado: Producto):
    if producto_id in fake_db:
        fake_db[producto_id]=producto_actualizado
        return True
    return False

def eliminar_producto(producto_id:int):
    if producto_id in fake_db:
        del fake_db[producto_id]
        return True
    return False
    