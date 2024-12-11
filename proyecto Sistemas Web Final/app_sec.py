from datetime import datetime, timedelta,timezone
from typing import Annotated
import jwt
from fastapi import Depends, FastAPI, HTTPException, status
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm
from pydantic import BaseModel
from jwt.exceptions import InvalidTokenError
from passlib.context import CryptContext
from typing import Union
from modelo import Product, Usuario
from services import update_product_service,get_all_products_service,delete_product_service,get_product_service
from services import update_usuario_service,get_all_usuario_service,get_usuario_service, delete_usuario_service


SECRET_KEY = "f342a2ee63169563779e75cad2fc3f81423b8f4623fd34ab19d1d7ea6cdad2cc"
ALGORITHM = "HS256"
ACCESS_TOKEN_EXPIRE_MINUTES = 30

fake_users_db = {
    "johndoe": {
        "username": "johndoe",
        "full_name": "John Doe",
        "email": "johndoe@example.com",
        "hashed_password": "$2b$12$EixZaYVK1fsbw1ZfbX30XePaWxn96p36WQoeG6Lruj3vjPGga31lW",
        "disabled": False,
    },
}

class Token (BaseModel):
    access_token: str
    token_type : str


class TokenData (BaseModel):
    username: str | None = None


class User(BaseModel):
    username: str
    email: str  | None = None
    full_name: str | None = None
    disabled: bool  | None = None 

class UserInDB(User):
    hashed_password: str


pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")
oauth2_scheme = OAuth2PasswordBearer(tokenUrl= "token")

app = FastAPI()

def get_user(db,username:str):
    print("Pasa por modulo get user")
    if username in db:
        print("Pasa por username in db, que tengo un nombre de usuario en db")
        user_dict = db[username]
        return UserInDB(**user_dict)


def authenticate_user(fake_db,username:str, password: str):
    print("Pasa authenticate user")
    user = get_user(fake_db, username)
    if not user:
        print("pasa por el no user")
        return False
    if not verify_password(password, user.hashed_password):
        print("pasa por el no password")
        return False
    return user






def get_password_hash(password):
    return pwd_context.hash(password)


def verify_password(plain_password, hashed_password):
    return pwd_context.verify(plain_password, hashed_password)



def create_access_token(data:dict, expires_delta : timedelta | None = None):
    to_encode = data.copy()
    if expires_delta:
        expire = datetime.now(timedelta.utc)+ expires_delta
    else:
        expire = datetime.now(timezone.utc) + timedelta(minutes=15)
    to_encode.update({"exp":expire})
    encoded_jwt = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded_jwt




async def get_current_user(token: Annotated[str, Depends(oauth2_scheme)]):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail = "Could not validate credentials",
        headers= {"WWW-Authenticate": "Bearer"},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        username : str = payload.get("sub")
        if username is None:
            raise credentials_exception
        token_data = TokenData(username=username)
    except InvalidTokenError:
        raise credentials_exception
    user = get_user(fake_users_db, username=token_data.username)
    if user is None:
        raise credentials_exception
    return token_data



async def get_current_active_user(current_user: Annotated[User,Depends(get_current_user)]):
    if current_user.disabled:
        raise HTTPException(status_code=400, detail="Inactive user")
    return current_user


@app.post("/token")
async def login_for_acess_token( form_data: Annotated [OAuth2PasswordRequestForm, Depends()]) -> Token:
    user = authenticate_user(fake_users_db, form_data.username, form_data.password)
    print("Pasa por modulo login for access token")
    if not user:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Incorrect username or password QUE HE FALLADO",
            headers={"WWW-Authenticate": "Bearer"},
        )
    print("Pasa por el if")
    access_token_expires = timedelta(minutes=ACCESS_TOKEN_EXPIRE_MINUTES)
    access_token = create_access_token(data={"sub":user.username}, expires_delta=access_token_expires)
    return {"access_token": access_token, "token_type":"bearer"}



  

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
