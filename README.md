# API para servir modelos de ML

Dos modelos, un API, un dashboard (fiero fierito), tres alternativas para probar como le pegamos, millones de chance de romper cosas


Brevemente, este repositorio tiene las partes básicas de como servir un modelo de ML a través de un API, aunque el foco está en saber como testear el API y, de yapa, vemos que es posible tener un ""servidor"" gratis usando Deepnote.

El código principal está en la Jupyter Notebook y existen dos .py con el código para sacar andando local y Deepnotemente este experimento.

Algunos links relevantes:

Para levantar esto mismo en AWS:
https://aws.amazon.com/es/blogs/machine-learning/creating-a-machine-learning-powered-rest-api-with-amazon-api-gateway-mapping-templates-and-amazon-sagemaker/


Sobre las rutas de Flask:
https://hackersandslackers.com/flask-routes/


Enjoy!


TO DO:

-[] 1. Agregar versión con predicción batcheada (que se mande ID y vuelva predicción)
-[] 2. Agregar A/B testing sobre algún modelo
-[] 3. Agregar A/B testing con thompson sampling
-[] 4. Guardar Request enviada y el Response obtenido
-[] 5. Agregar feedback (que llegue la clase real)
-[] 6. Agregar Online Learning (yapa: ttps://github.com/online-ml/awesome-online-machine-learning)
-[] 7. Agregar endpoint de reinicio de modelos (para arrancar del escenario base, sin los modelos que aprendan online)
