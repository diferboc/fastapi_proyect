from fastapi import APIRouter, HTTPException
from models import Producto
from services import (
    obtener_todos_los_productos,
    obtener_productos_por_id,
    crear_producto,
    actualizar_producto,
    eliminar_producto)

router = APIRouter()
#obtener todos los productos
@router.get("/productos/")
def obtener_productos():
    return obtener_todos_los_productos

#obtener un producto po id
@router.get("/productos/{producto_id}")
def obtener_producto(producto_id:int):
    Producto=obtener_productos_por_id(producto_id)
    if Producto is None:
        raise HTTPException(status_code=404, detail="producto no encontrado")
    return Producto

#crear un nuevo producto
@router.post("/productos/")
def crear_nuevo_producto(producto: Producto):
    nuevo_id = crear_producto(producto)
    return {"mensaje":"Producto creado exitosamente","id":nuevo_id}

#actualizar un producto
@router.put("/productos/{producto_id}")
def actualizar_un_producto(producto_id:int, producto_actualizado:Producto):
    actualizado = actualizar_producto(producto_id, producto_actualizado)
    if not actualizado:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"mensaje":"Producto actualizado exitosamente"}

#eliminar un producto
@router.delete("/productos/{producto_id}")
def eliminar_un_producto(producto_id:int):
    eliminado = eliminar_producto(producto_id)
    if not eliminado:
        raise HTTPException(status_code=404, detail="Producto no encontrado")
    return {"mensaje":"Producto eliminado exitosamente"}
    
    