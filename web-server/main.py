import store
from fastapi import FastAPI # type: ignore
from fastapi.responses import HTMLResponse #type: ignore

app = FastAPI()

@app.get('/')
def getList():
    return ['1,2,3']

@app.get('/contact', response_class=HTMLResponse)
def get_list():
    return """
        <h1>Hola soy una pagina</h1>
        <p>soy un parrafo</p>
    """

def Run():
    store.GetCategories()

if __name__ == '__main__':
    Run()