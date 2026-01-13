from fastapi import FastAPI
from routes import router


app = FastAPI()

@app.get('/')
def healthy():
    return {
        'message': 'ok'
    }

app.include_router(router)

if __name__ == '__main__':
    import uvicorn
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)