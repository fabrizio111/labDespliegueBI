from pydantic import BaseModel

class DataModel(BaseModel):

# Estas varibles permiten que la librería pydantic haga el parseo entre el Json recibido y el modelo declarado.
    #year: float
    #km_driven: float
    u: float
    g: float
    class_GALAXY: float
    class_STAR: float

#Esta función retorna los nombres de las columnas correspondientes con el modelo exportado en joblib.
    def columns(self):
        return ["u", "g", "class_GALAXY", "class_STAR"]
