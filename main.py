from fastapi import FastAPI, HTTPException, status, Path
from models import Time
import requests
from fastapi import Query
from typing import Optional
from fastapi import Header
from time import sleep
from fastapi import Depends
from typing import Any

app = FastAPI()

times = {
    1: {
        "nome": "real madrid",
        "posicao": 1,
        "tecnico": "ancelotti",
        "pontos": 75
    },
    2: {
        "nome": "barcelona",
        "posicao": 2,
        "tecnico": "xavi",
        "pontos": 71
    },
    3: {
        "nome": "sevilla",
        "posicao": 3,
        "tecnico": "lopetegui",
        "pontos": 70
    },
    4: {
        "nome": "real sociedad",
        "posicao": 4,
        "tecnico": "alguacil",
        "pontos": 60
    },
    5: {
        "nome": "atletico de madrid",
        "posicao": 5,
        "tecnico": "simeone",
        "pontos": 60
    },
    6: {
        "nome": "betis",
        "posicao": 6,
        "tecnico": "pellegrini",
        "pontos": 49
    },
    7: {
        "nome": "villarreal",
        "posicao": 7,
        "tecnico": "emery",
        "pontos": 47
    },
    8: {
        "nome": "celta de vigo",
        "posicao": 8,
        "tecnico": "coudet",
        "pontos": 44
    },
    9: {
        "nome": "granada",
        "posicao": 9,
        "tecnico": "martinez",
        "pontos": 43
    },
    10: {
        "nome": "levante",
        "posicao": 10,
        "tecnico": "lopez",
        "pontos": 42
    },
    11: {
        "nome": "athletic bilbao",
        "posicao": 11,
        "tecnico": "marcelino",
        "pontos": 41
    },
    12: {
        "nome": "osasuna",
        "posicao": 12,
        "tecnico": "arrasate",
        "pontos": 41
    },
    13: {
        "nome": "alaves",
        "posicao": 13,
        "tecnico": "lopez muniz",
        "pontos": 30
    },
    14: {
        "nome": "mallorca",
        "posicao": 14,
        "tecnico": "lopez garai",
        "pontos": 29
    },
    15: {
        "nome": "elche",
        "posicao": 15,
        "tecnico": "escriba",
        "pontos": 27
    },
    16: {
        "nome": "getafe",
        "posicao": 16,
        "tecnico": "bordalas",
        "pontos": 25
    },
    17: {
        "nome": "cadiz",
        "posicao": 17,
        "tecnico": "cervera",
        "pontos": 25
    },
    18: {
        "nome": "rayo vallecano",
        "posicao": 18,
        "tecnico": "andoni iraola",
        "pontos": 19
    },
    19: {
        "nome": "valencia",
        "posicao": 19,
        "tecnico": "gracia",
        "pontos": 16
    },
    20: {
        "nome": "eibar",
        "posicao": 20,
        "tecnico": "mendilibar",
        "pontos": 16
    }
}


@app.get('/tradutor')
async def tradutor():
    url = f'https://api.dictionaryapi.dev/api/v2/entries/en/car'
    
    response = requests.get(url)
    
    if response.status_code == 200:
        data = response.json()
        data_1 = dict(data[0])
        word = data_1["word"]
        definition = data_1["meanings"][0]["definitions"][0]["definition"]
        
        result = {
            word : definition
        }
        
        return result
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail='Time não encontrado na API de futebol')



@app.get ('/murilo')
async def get_violoes():
    # url = ("http://10.234.92.47:8000/violoes") 
    response = requests.get("http://10.234.92.47:8000/filmes")
    data = response.json()
    return data



@app.get ('/murilo/{muri_id}')
async def get_violoes(muri_id):
    # url = ("http://10.234.92.47:8000/violoes") 
    response = requests.get(f"http://10.234.92.47:8000/filmes/{muri_id}")
    data = response.json()
    return data



#@app.get('/times')
#async def get_times():
#    return times



@app.get('/time_query_parameter')
async def get_time_query_parameter_funcao(time_1 : str, time_2 : str):
    msg = f"{time_1} x {time_2}"
    resposta = {
        "jogo" : msg
    }
    return resposta




max_value = max(times.keys()) + 1

@app.get('/times/{time_id}')
async def get_time_id(time_id: int):
    if time_id < 1 or time_id >= max_value:
        raise HTTPException(status_code=status.HTTP_422_UNPROCESSABLE_ENTITY, detail="O ID do time deve ser um número inteiro válido entre 1 e {max_value - 1}")
    
    if time_id in times:
        time_data = times[time_id]
        time_data["id"] = time_id
        return time_data
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe um time com o ID {time_id}")







@app.get('/times/{time_id}')
async def get_time(time_id: int):
    if time_id in times:
        time_data = times[time_id]
        time_data["id"] = time_id
        return time_data
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe um time com o ID {time_id}")



@app.post('/times')
async def post_time(time: Time):
    if time.id not in times:
        # Verificar se o ID fornecido é nulo ou vazio
        if time.id is None or time.id == "":
            # Gerar um ID único para o novo time
            time.id = max(times.keys()) + 1
        times[time.id] = time.dict()
        return time
    else:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail=f"Já existe um time com o ID {time.id}")



@app.put('/times/{time_id}')
async def put_time(time_id: int, time: Time):
    if time_id in times:
        times[time_id] = time.dict()
        return times[time_id]
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe um time com o ID {time_id}")



@app.delete('/times/{time_id}')
async def delete_time(time_id: int):
    if time_id in times:
        del times[time_id]
        return {"message": f"Time com ID {time_id} removido com sucesso."}
    else:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail=f"Não existe um time com o ID {time_id}")



if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host='0.0.0.0', port=8000, reload=True)



@app.get('/time_query_parametro_2')
async def calcular(a: int = Query(default=None,gt=5), b: int = Query(default=None,gt=10), c: Optional[int] = 0):
    soma = a + b + c
    return {"soma" : soma}


@app.get('/time_query_parameter_3')
async def calcular(a: int = Query(default=None,gt=5),
                   b: int = Query(default=None,gt=10),
                   test: str = Header(default=None),
                   c: Optional[int] = 0):

    soma = a + b + c
    print(f'TEST: {test}')
    return {"resultado": soma}

def fake_db():
    try:
        print("Abrindo conexão com o banco de dados!")
        sleep(1)
    except:
        pass

    finally:
        print("Fechando conexão com o banco de dados")
        sleep(1)

@app.get('/times')
async def get_times (db: Any = Depends(fake_db)):
    return times




