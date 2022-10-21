<h1>CAPTURAS EN INSOMNIA<h1>

<p>En primer lugar se creó un diccionario con una serie de datos, en mi caso fueron una coleccion de cajas con items cuyos parametros eran su nombre y su tamaño<p>

<h2>Obtencion de datos del diccionario inicial<h2>

<p>En esta primera consulta se le pide al servidor que obtenga los datos existentes actualmente<p>

<img src="/images/getall.png">

<h2>Creacion de una caja nueva<h2>

<p>En primer lugar se define una funcion que obtendrá la informacion de un formato JSON(estos datos se darán desde insomnia) para con estos datos crear una nueva caja y mostrarla en pantalla<p>

<img src="/images/createBox.png">

<h2>Creacion de un item nuevo<h2>

<p>Al igual que con la creacion de una caja se define una opcion que obtendrá los datos para la creacion de un nuevo item, cabe destacar que en la url se agregará la caja a la que fue asignado y el carracter "item" <p>

<img src="/images/createitem.png">

<h2>Obtener datos exclusivamente de una caja<h2>

<p>Como observamos anteriormente podemos mostrar en pantalla la informacion de todas las cajas existentes, pues en este caso mostraremos solamente las de una caja, para eso en la url tendremos la adicion del nombre de la caja a consultar, y en codigo tendremos una condicion con esta url que de cumplirse se mostrará la informacion solicitada<p>

<img src="/images/getmyboxdata.png">

<h2>Obtener solamente los items de una caja<h2>

<p>Podremos de igual forma, siguiendo la logica del ejemplo anterior y con la url con la que añadimos un nuevo item el consultar los datos de estos items<p>

<img src="/images/getitems.png">

<p>Para probar la funcionalidad del codigo recomiendo reinstalar el entorno virtual en caso de problemas y con esto, reinstalar flask. Mil gracias.<p>