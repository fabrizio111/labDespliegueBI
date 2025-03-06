Al final por cuestion de tiempo, se probó el despliegue por consola con el archivo test.py y funcionó correctamente. 

Instrucciones:
- ejecutar uvicorn main:app --reload
- probar python test.py en cmd

**ACTUALIZACIONES**:
1. Se probó con Postman con los siguientes parámetros:
   {
    "u": 3.5, 
    "g": 2.0,
    "class_GALAXY": 1.0,
    "class_STAR": 0.0
}

Dió la siguiente prediccion: 
{
    "prediction": [
        -0.08476745962956798
    ]
}

es decir, está prediciendo un redshift de -0.085 para los parámetros. 
Esto se puede probar con diferentes parámetros y obtener su respectiva predicción.

2. En la primera versión se probó por consola, ahora si se puede realizar la prueba con PostMan.

3. Instrucciones para correr el programa:
   1. Ejecutar: uvicorn main:app --reload
   2. Abrir PostMan, crear una solicitud POST
   3. Copiar el siguiente enlace: http://127.0.0.1:8000/predict/
   4. Ir a la sección Body y copiar en formato raw este JSON:
{
    "u": 3.5, 
    "g": 2.0,
    "class_GALAXY": 1.0,
    "class_STAR": 0.0
  }

  Nota: Puedes probar con diferentes parámetros 

  5. Enviar la petición
