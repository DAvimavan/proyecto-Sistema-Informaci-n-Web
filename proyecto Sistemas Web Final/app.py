from fastapi import FastAPI, HTTPException
from typing import Union
from modelo import Product, Usuario
from services import update_product_service,get_all_products_service,delete_product_service,get_product_service
from services import update_usuario_service,get_all_usuario_service,get_usuario_service,delete_usuario_service

app = FastAPI()



@app.get("/") 
def read_index():
    return{"Hola mundo"}

#PRODUCTO encontrar un dato API
@app.get("/products/{product_id}")
def read_product(product_id:int, query: Union[str,int,None]=None):
    product = get_product_service(product_id)
    if product:
        return product
    else:
        raise HTTPException(status_code=404, detail="Producto no encontrado")

#PRODUCTO insertarAPI 
@app.put("/products/:{Product}")
def update_product(product_id: int, product: Product):
    # Llamar a la función de servicio para actualizar el producto
    updated_product = update_product_service(product) 
    return updated_product

#PRODUCTO obtener todos los datosAPI
@app.get("/products/")
def read_all_products():
    return get_all_products_service()

#PRODUCTO eliminar un datoAPI
@app.delete("/products/{product_id}")
def delete_product(product_id:int):
    return delete_product_service(product_id)

#USUARIO insertarAPI
@app.put("/usuarios/:{Usuario}")
def update_usuario(usuario_id: int, usuario: Usuario):
    # Llamar a la función de servicio para actualizar el producto
    updated_usuario= update_usuario_service(usuario)
    return updated_usuario


#Usuario encontrar un dato API
@app.get("/usuarios/{id_usuario}")
def read_usuario(id_usuario:int, query: Union[str,int,None]=None):
    usuario = get_usuario_service(id_usuario)
    if usuario:
        return usuario
    else:
        raise HTTPException(status_code=404, detail="Producto no encontrado")


#USUARIO obtener todos los datosAPI
@app.get("/usuarios/")
def read_all_usuarios():
    return get_all_usuario_service()



#USUARIO eliminar un datoAPI
@app.delete("/usuarios/{id_usuario}")
def delete_usuario(id_usuario:int):
    return delete_usuario_service(id_usuario)