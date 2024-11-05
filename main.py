from fastapi import FastAPI
from controllers import router
app = FastAPI()
#registrar rutas
app.include_router(router)
#correr la aplicacion
if __name__== "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8000, reload=True)