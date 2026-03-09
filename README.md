# PrimerosAuxilios_Rasa

- Ejecución
- Bateria de Preguntas

## Ejecución

**Para ejecutar la aplicación hay que seguir los siguientes pasos:**

```
git clone https://github.com/matope1/PrimerosAuxilios_Rasa
cd PrimerosAuxilios_Rasa
```
- Necesario version 3.10.5 (es la version probada) https://www.python.org/downloads/windows/
```
py -3.10 -m venv venv
```
```
venv\Scripts\activate
```
```
python -m pip install --upgrade pip
pip install -r requirements.txt
```
- Igensta
```
python rag/ingest.py
```

Terminal 1 (Terminal para ver loggs en cada pregunta y respuesta)
```
rasa train
```
```
rasa run actions
```
Terminal 2 (en otra terminal, dentro del mismo venv):
*Chat interactivo*
```
venv\Scripts\activate
```
```
rasa shell
```


## Bateria de preguntas para el chatbot:
#### Preguntas sobre desmayos
- que debo hacer si una persona se desmaya
- como ayudar a alguien que perdió el conocimiento
- que pasos debo seguir ante un desmayo

#### Preguntas sobre RCP
- que es la reanimacion cardiopulmonar
- cuando se debe hacer rcp
- como se realiza la rcp en un adulto
- que hago si alguien no respira

#### Emergencias
- que numero debo llamar en caso de accidente
- que numero marco si hay una emergencia
- como contacto con emergencias

#### Hemorragias (sin documentacion, pero es un intent)
- que hacer si una persona tiene una herida que sangra mucho
- como detener un sangrado fuerte

#### Botiquín (sin documentacion, pero es un intent)
- que cosas deberia tener un botiquin de primeros auxilios
- que materiales incluye un botiquin

#### Preguntas fuera de conocimiento (para probar el fallback del RAG)
- como cocinar pasta
- cual es la capital de francia
- quien invento internet
- que hacer si me han robado la cartera

- Despedida
adios
