from fastapi import FastAPI
import uvicorn

app = FastAPI()

@app.get('/')
def index():
    return {'data': 'Hello FastAPI!'}

@app.get('/message')
def index():
    return {'data': 'FastAPI is great!'}
    
@app.get('/log')
def index():
    return {'data': 'FastAPI Logs'}

@app.get('/app')
def index():
    return {'data': 'FastAPI app'}

if __name__ == "__main__":
    uvicorn.run(app, host='0.0.0.0', port=8080)
