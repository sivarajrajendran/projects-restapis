from fastapi import FastAPI

app = FastAPI()

server_info = {'version': '1.0.0', 'launchDate': '21-04-2023' }


@app.get('/info')
def get_server_info():
    return {'info': server_info}
    