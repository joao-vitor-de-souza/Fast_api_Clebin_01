from fastapi import FastAPI
import times_routes, usuario_routes
app = FastAPI()
app.include_router(times_routes.router, tags=['times'])
app.include_router(usuario_routes.router, tags=['usuarios'])
if __name__ == '__main__':
    import uvicorn
    uvicorn.run ("PrinMain:app", host='0.0.0.0', port=8000, reload=True)
