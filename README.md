# Generating maximal outerplanar uniformly at random
[![N|Solid](https://camo.githubusercontent.com/23de01ffa3d1ff0fe57b824cf6f516d96df88d2f/68747470733a2f2f707265766965772e6962622e636f2f645864744c512f696e666f766973646963652e706e67)](https://camo.githubusercontent.com/23de01ffa3d1ff0fe57b824cf6f516d96df88d2f/68747470733a2f2f707265766965772e6962622e636f2f645864744c512f696e666f766973646963652e706e67)
#### Tabella dei contenuti

1. [Obiettivi](#obiettivi)
2. [Approcci](#approcci)
3. [Dagli unrooted binary tree ai grafi planari](#approccio1)
4. [Triangolazione di poligoni convessi](#approccio2)



# Obiettivi

Nella teoria dei grafi si definisce **grafo planare** un grafo che può essere raffigurato in modo che non si abbiano intersezioni di archi. 
I **grafi outerplanari massimali** sono un sottoinsieme dei grafi planari e sono rappresentabili con tutti i vertici sulla faccia esterna del disegno, con il massimo numero di archi che non si intersecano.  
L'obiettivo del progetto proposto in questa pagina è quindi quello di definire un algoritmo che generi grafi outerplanari non etichettati e massimali **uniformly at random**.
# Approcci

  - Il problema è sovrapponnibile a quello della generazione di triangolazioni di un poligono convesso.
  - C'è una relazione diretta tra gli unrooted binary tree ordinati con n foglie e i grafi outerplanari massimali.

Per entrambi gli approcci una possibile soluzione potrebbe essere quella di utilizzare un algoritmo che genera tutti gli elementi della collezione per poi selezionarne randomicamente uno. Tale soluzione, tuttavia,  risulta impraticabile al crescere della dimensione del grafo. In particolare si ha che il numero di possibili outerplanar diversi al crescere di *n* segue la sequenza: 

1, 1, 1, 3, 4, 12, 27, 82, 228, 733, 2282, 7528, 24834, 83898, 285357, 983244, 3412420, 11944614, 42080170, 149197152, 531883768, 1905930975, 6861221666, 24806004996, 90036148954, 327989004892, 1198854697588, 4395801203290, 16165198379984, 59609171366326, 220373278174641

Nel caso particolare della triangolazione dei poligoni convessi il numero risulta invece associato al numero catalano. I risultati di questi algoritmi presentano quindi ripetizioni di possibili configurazioni in termini di rotazioni e mirroring. Nel caso specifico di un esagono risulta che le possibili triangolazioni sono le seguenti:

[![N|Solid](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Catalan-Hexagons-example.svg/680px-Catalan-Hexagons-example.svg.png)](https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Catalan-Hexagons-example.svg/680px-Catalan-Hexagons-example.svg.png)

Si noti tuttavia che gli elementi non isomorfi sono in realtà soltanto 3. Adottando questa strategia è dunque necessario risolvere un problema di isomorfismo, eliminando le copie .


# Approccio 1
## Dagli unrooted binary tree ai grafi planari

Dalla lettura del paper [Generating Outerplanar Graphs Uniformly at Random](https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/generating-outerplanar-graphs-uniformly-at-random/DA7B9E91184052CA32153FC83A4A7ED8) è risultato evidente che il problema di generare tutti i possibili maximal outerplanar graph di *n* lati  è equivalente a quello di generare tutti i possibili unrooted binary tree ordinati con *n* foglie. Questa famiglia di alberi ha la seguente peculiarità: ogni nodo dell’albero o è una foglia o deve avere grado tre.
Procedendo in questa direzione si è pensato ad un algoritmo che potesse generare tutti gli alberi di questa famiglia passato in input il numero di foglie desiderate.
L’idea dietro l’algoritmo è la seguente: volendo generare un unrooted binary tree esiste sicuramente un nodo con grado tre padre di tre sottoalberi binari. Poiché l’albero deve avere esattamente N foglie, fissato questo numero, si crea una lista di triple di addendi che sommati diano esattamente N, ovvero il numero di foglie che ciascuno dei tre sottoalberi binari dovrà avere. Quindi selezionata una tripla della lista, per ogni numero in essa si generano sotto forma di stringa tutti i possibili binary tree di n foglie: questi sottoalberi sono tutti figli del nodo da cui è iniziata la generazione, che di fatto non è una foglia ed ha proprio grado tre. 
Un’implementazione dell’algoritmo descritto è presente nel file binaryTreeUnrooted.py .
Il problema di questo approccio è che vengono generati molti alberi isomorfi difficili da distinguere che ovviamente generano gli stessi outerplanar graph. 

# Approccio 2
## Triangolazione di poligoni convessi

Abbandonata l’idea di generare i grafi outerplanari a partire dagli alberi, si è voluto procedere con l’approccio basato sulle triangolazioni del poligono convesso.
In letteratura sono presenti diversi algoritmi per la generazione di grafi outerplanari etichettati, piuttosto ridotta è invece la documentazione relativa a quelli non etichettati. Dall'articolo presente su  [Garethrees](http://garethrees.org/2013/06/15/triangulation/) abbiamo scelto di adottare la seguente funzione per la generazione di tutte le possibili triangolaizioni:
```sh
def triangulations(p):
    """Generate the triangulations of the convex polygon p.
    The sequence p consists of the vertices of the polygon.
    Each triangulation in the output is a list of triangles, and each
    triangle is a tuple of three vertices.

    >>> list(triangulations(tuple('abcd')))
    [[('a', 'b', 'd'), ('b', 'c', 'd')], [('a', 'b', 'c'), ('a', 'c', 'd')]]
    >>> [sum(1 for _ in triangulations(range(i))) for i in range(3, 8)]
    [1, 2, 5, 14, 42]
    """
    n = len(p)
    if n == 2:
        yield []
    elif n == 3:
        yield [p]
    else:
        for k in range(1, n - 1):
            for u, v in product(triangulations(p[:k + 1]), triangulations(p[k:])):
                yield u + [(p[0], p[k], p[-1])] + v
```
Essenzialmente si tratta della generazione di un albero in cui le foglie costituiscono le possibili triangolazioni. Tali triangolazioni, come specificato nella sezione precedente, sono però etichettate e quindi non c'è una distribuzione uniforme al numero di isomorfismi.
L'algortimo  di generazione randomica in modo uniforme dei grafi in questione si articola quindi nelle seguenti fasi:
- Estrazione di un numero randomico *r* compreso tra *1* e il numero Catalano di *N*.
- Viene generata soltanto l' *r*-esima triangolazione del poligono, senza costruire l'intero albero.
- E' calcolato il numero *I* di isomorfi della triangolazione estratta. Poichè diverse classi possono avere numeri di rotazione e mirroring diversi è necessario normalizzare la probabilità con cui viene estratto un determinato elemento. Per questo vengono estratti due numeri randomici tra *1* e *I* e se questi 2 numeri coincidono allora la triangolazione viene presa altrimenti il processo viene ripetuto.

L'enumerazione delle foglie viene costruita come segue: a ciascun nodo dell'albero di generazione è associata la dimensione dei sottoalberi a lui radicati effettuando il prodotto tra i numeri catalani associati alla triangolazione del nodo di riferimento. Ad ogni iterazione viene quindi selezionato il branch il cui range di valori comprende il numero estratto. 

Per quello che riguarda il calcolo delgli ismorfismi di un determinato elemento si sfrutta una proprietà dei grafi planari riportata in [Rencostruction of maximal outerplanar graphs](http://ac.els-cdn.com/0012365X72900076/1-s2.0-0012365X72900076-main.pdf?_tid=1255f97e-7382-11e7-9d07-00000aab0f01&acdnat=1501238995_2af031d7b204f70c6f758f9a2c8d54f7), per la quale una label degree sequence è associata univocamente ad una configurazione del grafo. E' perciò possibile calcolare il numero di isomorfi genenerando le *n-1*  label degree sequence ottenute tramite rotazione circolare della triangolazione ottenuta e contare il numero *S* di sequenze identiche.
Questo è il numero di isomorfi ruotati generati; per il calcolo del numero di mirror presenti è invece necessario ribaltare la sequenza e vedere se c'è una sovrapposizione con una delle *n-1* sequenze precedentemente generate. In caso affermativo il numero di isomorfi è *Sx2*, altrimenti è pari a *S*.


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
