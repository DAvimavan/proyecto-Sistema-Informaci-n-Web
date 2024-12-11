from modelo import Product, Usuario
from dao import insert_or_update_product, get_product,get_all_products,delete_product
from dao import insert_or_update_Usuario,get_Usuario,get_all_Usuarios,delete_usuario


#CAPA DE NEGOCIOS

#PRODUCTO update SERVICIO
def update_product_service(product: Product):
    # en este punto se puede agregar logica de control de esta operacion
    insert_or_update_product(product) 
    return {"product": product} 


#PRODUCTO obtener un dato SERVICIO
def get_product_service(product_id:int):
    product=get_product(product_id)
    if product:
        return(product)
    else:
        return None
    

# PRODUCTO obtener todos los productos SERVICIO
def get_all_products_service():
    return get_all_products()


# PRODUCTO eliminar un dato SERVICIO
def delete_product_service(product_id:int):
    delete_product(product_id)
    return {"message" : f"Product ID = {product_id} ha sido eliminado de manera correcta"}


#USUARIO update SERVICIO
def update_usuario_service(usuario: Usuario):
    # en este punto se puede agregar logica de control de esta operacion
    insert_or_update_Usuario(usuario) 
    return {"usuario": usuario} 

#USUARIO obtener un dato SERVICIO
def get_usuario_service(id_usuario:int):
    usuario=get_Usuario(id_usuario)
    if usuario:
        return(usuario)
    else:
        return None
    

# USUARIO obtener todos los productos SERVICIO
def get_all_usuario_service():
    return get_all_Usuarios()





# USUARIO eliminar un dato SERVICIO
def delete_usuario_service(id_usuario:int):
    delete_usuario(id_usuario)
    return {"message" : f"ID Usuario = {id_usuario} ha sido eliminado de manera correcta"}