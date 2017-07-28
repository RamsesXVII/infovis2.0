# Generating maximal outerplanar uniformly at random
#### Tabella dei contenuti

1. [Obiettivi](#obiettivi)
2. [Applicazione](#applicazione)
    * [Descrizione](#applicazione)
    * [Tecnologie utilizzate](#applicazione)
3. [Configurazione VM](#configurazione)
4. [Provisioning](#provisioning)
    * [Apache TomEE](#apache-tomee)
      * [Il ruolo della cartella condivisa](#cartella-condivisa)
    * [Postgres](#postgres)
      * [Setup](#setup)
      * [Creazione di un database](#creazione-di-un-database)
5. [Installazione](#installazione)
6. [Script di Test](#script-di-test)
7. [Comandi utili](#comandi-utili)
8. [Todo](#todo)
9. [Bug e problemi noti](#bug-e-problemi-noti)
10. [Realizzatori](#realizzatori)

[![N|Solid](https://camo.githubusercontent.com/23de01ffa3d1ff0fe57b824cf6f516d96df88d2f/68747470733a2f2f707265766965772e6962622e636f2f645864744c512f696e666f766973646963652e706e67)](https://camo.githubusercontent.com/23de01ffa3d1ff0fe57b824cf6f516d96df88d2f/68747470733a2f2f707265766965772e6962622e636f2f645864744c512f696e666f766973646963652e706e67)
# Obiettivi

Nella teoria dei grafi si definisce **grafo planare** un grafo che può essere raffigurato in modo che non si abbiano intersezioni di archi. 
I **grafi outerplanari massimali** sono un sottoinsieme dei grafi planari e sono rappresentabili con tutti i vertici sulla faccia esterna del disegno, con il massimo numero di archi che non si intersecano.  
L'obiettivo del progetto proposto in questa pagina è quindi quello di definire un algoritmo che generi grafi outerplanari non etichettati e massimali **uniformly at random**.
# Possibili strategie

  - Il problema è sovrapponnibile a quello della generazione di triangolazioni di un poligono convesso.
  - C'è una relazione diretta tra gli unrooted binary tree ordinati con n foglie e i grafi outerplanari massimali.

Per entrambi gli approcci una possibile soluzione potrebbe essere quella di utilizzare un algoritmo che genera tutti gli elementi della collezione per poi selezionarne randomicamente uno. Tale soluzione, tuttavia,  risulta impraticabile al crescere della dimensione del grafo. In particolare si ha che il numero di possibili outerplanar diversi al crescere di *n* segue la sequenza: 

1, 1, 1, 3, 4, 12, 27, 82, 228, 733, 2282, 7528, 24834, 83898, 285357, 983244, 3412420, 11944614, 42080170, 149197152, 531883768, 1905930975, 6861221666, 24806004996, 90036148954, 327989004892, 1198854697588, 4395801203290, 16165198379984, 59609171366326, 220373278174641

Nel caso particolare della triangolazione dei poligoni convessi il numero risulta invece associato al numero catalano. I risultati di questi algoritmi presentano quindi ripetizioni di possibili configurazioni in termini di rotazioni e mirroring. Nel caso specifico di un esagono risulta che le possibili triangolazioni sono le seguenti:

[![N|Solid](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Catalan-Hexagons-example.svg/680px-Catalan-Hexagons-example.svg.png)](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Catalan-Hexagons-example.svg/680px-Catalan-Hexagons-example.svg.png)

Si noti tuttavia che gli elementi non isomorfi sono in realtà soltanto 3. Adottando questa strategia è dunque necessario risolvere un problema di isomorfismo, eliminando le copie .


# Dagli unrooted binary tree ai grafi planari

Dalla lettura del paper [Generating Outerplanar Graphs Uniformly at Random](https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/generating-outerplanar-graphs-uniformly-at-random/DA7B9E91184052CA32153FC83A4A7ED8) è risultato evidente che il problema di generare tutti i possibili maximal outerplanar graph di *n* lati  è equivalente a quello di generare tutti i possibili unrooted binary tree ordinati con *n* foglie. Questa famiglia di alberi ha la seguente peculiarità: ogni nodo dell’albero o è una foglia o deve avere grado tre.
Procedendo in questa direzione si è pensato ad un algoritmo che potesse generare tutti gli alberi di questa famiglia passato in input il numero di foglie desiderate.
L’idea dietro l’algoritmo è la seguente: volendo generare un unrooted binary tree esiste sicuramente un nodo con grado tre padre di tre sottoalberi binari. Poiché l’albero deve avere esattamente N foglie, fissato questo numero, si crea una lista di triple di addendi che sommati diano esattamente N, ovvero il numero di foglie che ciascuno dei tre sottoalberi binari dovrà avere. Quindi selezionata una tripla della lista, per ogni numero in essa si generano sotto forma di stringa tutti i possibili binary tree di n foglie: questi sottoalberi sono tutti figli del nodo da cui è iniziata la generazione, che di fatto non è una foglia ed ha proprio grado tre. 
Un’implementazione dell’algoritmo descritto è presente nel file binaryTreeUnrooted.py .
Il problema di questo approccio è che vengono generati molti alberi isomorfi difficili da distinguere che ovviamente generano gli stessi outerplanar graph. 





You can also:
  - Import and save files from GitHub, Dropbox, Google Drive and One Drive
  - Drag and drop markdown and HTML files into Dillinger
  - Export documents as Markdown, HTML and PDF

Markdown is a lightweight markup language based on the formatting conventions that people naturally use in email.  As [John Gruber] writes on the [Markdown site][df1]

> The overriding design goal for Markdown's
> formatting syntax is to make it as readable
> as possible. The idea is that a
> Markdown-formatted document should be
> publishable as-is, as plain text, without
> looking like it's been marked up with tags
> or formatting instructions.

This text you see here is *actually* written in Markdown! To get a feel for Markdown's syntax, type some text into the left window and watch the results in the right.

### Tech

Dillinger uses a number of open source projects to work properly:

* [AngularJS] - HTML enhanced for web apps!
* [Ace Editor] - awesome web-based text editor
* [markdown-it] - Markdown parser done right. Fast and easy to extend.
* [Twitter Bootstrap] - great UI boilerplate for modern web apps
* [node.js] - evented I/O for the backend
* [Express] - fast node.js network app framework [@tjholowaychuk]
* [Gulp] - the streaming build system
* [Breakdance](http://breakdance.io) - HTML to Markdown converter
* [jQuery] - duh

And of course Dillinger itself is open source with a [public repository][dill]
 on GitHub.

### Installation

Dillinger requires [Node.js](https://nodejs.org/) v4+ to run.

Install the dependencies and devDependencies and start the server.

```sh
$ cd dillinger
$ npm install -d
$ node app
```

For production environments...

```sh
$ npm install --production
$ npm run predeploy
$ NODE_ENV=production node app
```

### Plugins

Dillinger is currently extended with the following plugins. Instructions on how to use them in your own application are linked below.

| Plugin | README |
| ------ | ------ |
| Dropbox | [plugins/dropbox/README.md] [PlDb] |
| Github | [plugins/github/README.md] [PlGh] |
| Google Drive | [plugins/googledrive/README.md] [PlGd] |
| OneDrive | [plugins/onedrive/README.md] [PlOd] |
| Medium | [plugins/medium/README.md] [PlMe] |
| Google Analytics | [plugins/googleanalytics/README.md] [PlGa] |


### Development

Want to contribute? Great!

Dillinger uses Gulp + Webpack for fast developing.
Make a change in your file and instantanously see your updates!

Open your favorite Terminal and run these commands.

First Tab:
```sh
$ node app
```

Second Tab:
```sh
$ gulp watch
```

(optional) Third:
```sh
$ karma test
```
#### Building for source
For production release:
```sh
$ gulp build --prod
```
Generating pre-built zip archives for distribution:
```sh
$ gulp build dist --prod
```
### Docker
Dillinger is very easy to install and deploy in a Docker container.

By default, the Docker will expose port 80, so change this within the Dockerfile if necessary. When ready, simply use the Dockerfile to build the image.

```sh
cd dillinger
docker build -t joemccann/dillinger:${package.json.version}
```
This will create the dillinger image and pull in the necessary dependencies. Be sure to swap out `${package.json.version}` with the actual version of Dillinger.

Once done, run the Docker image and map the port to whatever you wish on your host. In this example, we simply map port 8000 of the host to port 80 of the Docker (or whatever port was exposed in the Dockerfile):

```sh
docker run -d -p 8000:8080 --restart="always" <youruser>/dillinger:${package.json.version}
```

Verify the deployment by navigating to your server address in your preferred browser.

```sh
127.0.0.1:8000
```

#### Kubernetes + Google Cloud

See [KUBERNETES.md](https://github.com/joemccann/dillinger/blob/master/KUBERNETES.md)


### Todos

 - Write MOAR Tests
 - Add Night Mode

License
----

MIT


**Free Software, Hell Yeah!**

[//]: # (These are reference links used in the body of this note and get stripped out when the markdown processor does its job. There is no need to format nicely because it shouldn't be seen. Thanks SO - http://stackoverflow.com/questions/4823468/store-comments-in-markdown-syntax)


   [dill]: <https://github.com/joemccann/dillinger>
   [git-repo-url]: <https://github.com/joemccann/dillinger.git>
   [john gruber]: <http://daringfireball.net>
   [df1]: <http://daringfireball.net/projects/markdown/>
   [markdown-it]: <https://github.com/markdown-it/markdown-it>
   [Ace Editor]: <http://ace.ajax.org>
   [node.js]: <http://nodejs.org>
   [Twitter Bootstrap]: <http://twitter.github.com/bootstrap/>
   [jQuery]: <http://jquery.com>
   [@tjholowaychuk]: <http://twitter.com/tjholowaychuk>
   [express]: <http://expressjs.com>
   [AngularJS]: <http://angularjs.org>
   [Gulp]: <http://gulpjs.com>

   [PlDb]: <https://github.com/joemccann/dillinger/tree/master/plugins/dropbox/README.md>
   [PlGh]: <https://github.com/joemccann/dillinger/tree/master/plugins/github/README.md>
   [PlGd]: <https://github.com/joemccann/dillinger/tree/master/plugins/googledrive/README.md>
   [PlOd]: <https://github.com/joemccann/dillinger/tree/master/plugins/onedrive/README.md>
   [PlMe]: <https://github.com/joemccann/dillinger/tree/master/plugins/medium/README.md>
   [PlGa]: <https://github.com/RahulHP/dillinger/blob/master/plugins/googleanalytics/README.md>
