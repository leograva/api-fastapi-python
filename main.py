from fastapi import FastAPI

app = FastAPI()

@app.get('/')
def hello():
  return {"message": "Seja bem vindo à API do Leograva!!!"}

#função que recebe o parâmetro
@app.get('/numeros/{numero}')
async def read_item(numero: int):
    if numero == 1:
        return {"message":"Um"}
    elif numero == 2:
        return {"message":"Dois"}
    elif numero == 3:
        return {"message":"Três"}
    elif numero == 4:
        return {"message":"Quatro"}
    elif numero == 5:
        return {"message":"Cinco"}
    elif numero == 6:
        return {"message":"Seis"}
    elif numero == 7:
        return {"message":"Sete"}
    elif numero == 8:
        return {"message":"Oito"}
    elif numero == 9:
        return {"message":"Nove"}
    elif numero == 10:
        return {"message":"Dez"}
    else:
        return {"message":"Número não encontrado"}