from fastapi import FastAPI

app = FastAPI()


@app.get("/inicio")
async def ruta_prueba():
    return "Hola"
