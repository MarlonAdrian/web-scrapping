# Web scrapping, tiktok, facebook, track

Con el archvio track se necesitó la ayuda de la herramienta de la página web que permite tener una localización exacta de algún lugar en específico, se escogió una ciudad del Ecuador, es la ciudad de quito y para la otra búsqueda se implementó la frase de juegos olímpicos, y Tokio, generando una amplia información
Con tik tok se utilizó la consola de windows en base a una librería que me permite acceder a dos cuentas en específico, estos deportistas son olympicteamisrael y steffy.aradillas.
Por otra parte en para el web scrapping me guié de una pagina web que es "https://resultados.elpais.com/deportivos/juegos-olimpicos/medallero/", el tema elegido fue de la cantidad de medallas obtenidas en esta competencia, tantas de oro, plata y bronce. Creando despues una conexion con mongodbCompass. Tomando en cuenta el puerto que este mantiene
Para Facebook se navegó en la pagina oficial de los juegos olimpicos, estos datos de likes, comentarios, etc., se guardarán en un archivo tipo json y serán enviados a couchdb, utlizando librerias como lo son couchd,json, time.
