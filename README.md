# Generating maximal outerplanar graphs uniformly at random
<p align="center">
  <img width="460" height="300" src="https://camo.githubusercontent.com/23de01ffa3d1ff0fe57b824cf6f516d96df88d2f/68747470733a2f2f707265766965772e6962622e636f2f645864744c512f696e666f766973646963652e706e67">
</p>

#### Tabella dei contenuti

1. [Obiettivi](#obiettivi)
2. [Approcci](#approcci)
3. [Dagli unrooted binary tree ai grafi planari]( #approccio1)
4. [Triangolazione di poligoni convessi]( #approccio2)
5. [Validazione]( #validazione)
6. [Esecuzione]( #esecuzione)
7. [Autori]( #autori)




# Obiettivi

Nella teoria dei grafi si definisce **grafo planare** un grafo che può essere raffigurato in modo che non si abbiano intersezioni di archi. 
I **grafi outerplanari massimali** sono un sottoinsieme dei grafi planari e sono rappresentabili con tutti i vertici sulla faccia esterna del disegno, con il massimo numero di archi che non si intersecano.  
L'obiettivo del progetto proposto in questa pagina è quindi quello di definire un algoritmo che generi grafi outerplanari non etichettati e massimali **uniformly at random**.
# Approcci
Sono possibibili diverse interpretazioni del problema e in particolare, dalla letteratura esistente, si ha che:

  - Il problema è sovrapponnibile a quello della generazione di triangolazioni di un poligono convesso.
  - C'è una relazione diretta tra gli unrooted binary tree ordinati con n foglie e i grafi outerplanari massimali.

Per entrambi gli approcci una possibile soluzione potrebbe essere quella di utilizzare un algoritmo che genera tutti gli elementi della collezione per poi selezionarne randomicamente uno. Tale soluzione, tuttavia,  risulta impraticabile al crescere della dimensione del grafo. In particolare si ha che il numero di possibili outerplanar non etichettati  e massimali al crescere di *n*, con *n* pari al numero di nodi, segue la sequenza: 

> 1, 1, 1, 3, 4, 12, 27, 82, 228, 733, 2282, 7528, 24834, 83898, 285357, 983244, 3412420, 11944614, 42080170, 149197152, 531883768, 1905930975, 6861221666, 24806004996, 90036148954, 327989004892, 1198854697588, 4395801203290, 16165198379984, 59609171366326, 220373278174641

Per ulteriori informazioni sulla sequenza, cliccare [qui](https://oeis.org/A000207).

Nel caso particolare della triangolazione dei poligoni convessi il numero risulta invece associato al numero catalano. I risultati dei principali algoritmi per la triangolazione dei poligoni presentano infatti ripetizioni di possibili configurazioni in termini di rotazioni e mirroring. Nel caso specifico di un esagono risulta che le possibili triangolazioni sono le seguenti:

<p align="center">
  <img width="460" height="300" src="https://upload.wikimedia.org/wikipedia/commons/thumb/a/a8/Catalan-Hexagons-example.svg/680px-Catalan-Hexagons-example.svg.png">
</p>

Si noti tuttavia che gli elementi non isomorfi sono in realtà soltanto 3. Adottando questa strategia è dunque necessario risolvere un problema di isomorfismo, eliminando le copie .


# Approccio1
## Dagli unrooted binary tree ai grafi planari

Dalla lettura del paper [Generating Outerplanar Graphs Uniformly at Random](https://www.cambridge.org/core/journals/combinatorics-probability-and-computing/article/generating-outerplanar-graphs-uniformly-at-random/DA7B9E91184052CA32153FC83A4A7ED8) è risultato evidente che il problema di generare tutti i possibili maximal outerplanar graph di *n* lati  è equivalente a quello di generare tutti i possibili unrooted binary tree ordinati con *n* foglie. Questa famiglia di alberi ha la seguente peculiarità: ogni nodo dell’albero o è una foglia o deve avere grado tre.
Procedendo in questa direzione si è pensato ad un algoritmo che potesse generare tutti gli alberi di questa famiglia passato in input il numero di foglie desiderate.
L’idea dietro l’algoritmo è la seguente: volendo generare un unrooted binary tree esiste sicuramente un nodo con grado tre padre di tre sottoalberi binari. Poiché l’albero deve avere esattamente N foglie, fissato questo numero, si crea una lista di triple di addendi che sommati diano esattamente N, ovvero il numero di foglie che ciascuno dei tre sottoalberi binari dovrà avere. Quindi selezionata una tripla della lista, per ogni numero in essa si generano sotto forma di stringa tutti i possibili binary tree di n foglie: questi sottoalberi sono tutti figli del nodo da cui è iniziata la generazione, che di fatto non è una foglia ed ha proprio grado tre. 
Un’implementazione dell’algoritmo descritto è presente nel file binaryTreeUnrooted.py .
Il problema di questo approccio è che vengono generati molti alberi isomorfi difficili da distinguere che ovviamente generano gli stessi outerplanar graph. Per questo motivo, questa prima strategia non è stata portata avanti.

# Approccio2
## Triangolazione di poligoni convessi

Scartata l’idea di generare i grafi outerplanari a partire dagli alberi, si è voluto procedere con l’approccio basato sulle triangolazioni del poligono convesso.
In letteratura sono presenti diversi algoritmi per la generazione di grafi outerplanari etichettati, piuttosto ridotta è invece la documentazione relativa a quelli non etichettati. Dall'articolo presente su  [Garethrees](http://garethrees.org/2013/06/15/triangulation/) si è scelto quindi di adottare la seguente funzione per la generazione di tutte le possibili triangolaizioni:
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
Essenzialmente si tratta della generazione di un albero in cui le foglie costituiscono tutte le possibili triangolazioni etichettate. Il proccesso è ricorsivo e viene eseguito e a partire da un nodo radice che corrisponde al poligono senza triangolazioni interne.  Ogni nodo viene quindi espanso generando i figli che corrispondono a tutti i possibili triangoli che hanno come vertici uno degli angoli del poligono con il primo e ultimo angolo di esso. Il triangolo definito andrà quindi a suddividere il poligono padre in due poligoni di dimensioni diverse, il procedimento quindi continuerà cercando di triangolare in tutti i modi possibili i sottopoligoni appena generati.

Tali triangolazioni, come specificato nella sezione precedente, sono però etichettate e quindi non c'è una distribuzione uniforme al numero di isomorfismi. Si noti, appunto, come nella figura precedente relativa alle triangolazioni dell'esagono, sono presenti soltanto due possibili triangolazioni per una determinata classe di triangolazioni isomorfe, mentre sono ben 6 per ciascuna delle altre due. Per risolvere questo problema ed assicurare  un'estrazione *uniformly at  random* l'algortimo si articola quindi nelle seguenti fasi:
- Estrazione di un numero randomico *r* compreso tra *1* e il numero Catalano di *N*. L'idea di questo passaggio è di associare in modo univoco ciascuna foglia a uno di questi numeri e viceversa.
- E' generata soltanto l' *r*-esima triangolazione del poligono e il relativo sottoalbero, senza costruire l'intero albero di generazione.
- E' calcolato il numero *I* di isomorfi della triangolazione estratta. Poichè diverse classi possono avere numeri di rotazione e mirroring diversi è necessario normalizzare la probabilità con cui viene estratto un determinato elemento. Ottenuta dunque una determinata triangolazione viene estratto  un numero random tra *1* e *I* e se questo numero coincide con *a* la triangolazione viene presa altrimenti viene scartata e il processo viene ripetuto.

I primi due passi dell'algoritmo assicurano due caratteristiche fondamentali: è definita un'enumerazione per la quale non è necessario generare l'intero albero per l'accesso alla k-esima triangolazione e la generazione di un elemento è uniformly at random rispetto al totale delle triangolazioni etichettate. Questa strategia è possibile perchè si può stimare facilmente la dimensione del sotttoalbero radicato a ciascun nodo dell'albero di generazione. In particolare, è sufficicente effettuare il prodotto tra i numeri catalani associati alla triangolazione del nodo di riferimento. In questo modo, del nodo radice verrà espanso solo il figlio il cui sottoalbero comprende il range di valori nel quale è presente il numero *r* estratto. Il processo viene quindi ripetuto e ad ogni iterazione  è selezionato soltanto il nodo con la dimensione  del sottoalbero di interesse.
Sia ad esempio *N=5* e il numero *r* estratto=2. I figli del pentagono iniziale sono 3:
- (1,2,5,1)-(2,3,4,5,2)
- (1,2,3,1)-(1,3,5,1)-(3,4,5,3)
- (1,2,3,4,1)-(1,4,5,1)

che corrispondono appunto alle possibili combinazioni che si ottengono inserendo una triangolazione avente come base i vertici adiacenti (1,5)  e come terzo vertice gli altri possibili vertici. I tre figli risultano quindi così strutturati:
- 1 triangolo + 1 quadrato  (1*2)   [2]
- 3 triangoli               (1)     [3]
- 1 triangolo + 1 quadrato (1*2)    [5]

Tra parentesi tonde è mostrato il prodotto tra i numeri catalani dei poligoni ottenuti, tra le quadre la conta incrementale. A questo punto è sufficiente espandere il nodo che comprende *r*, ovvero il primo. Il processo viene ripetuto fino al raggiungimento della triangolazione massimale, che  coincide con la triangolazione di riferimento.

Per quello che riguarda il calcolo delgli ismorfismi di un determinato elemento si sfrutta una proprietà dei grafi planari riportata in [Rencostruction of maximal outerplanar graphs](http://ac.els-cdn.com/0012365X72900076/1-s2.0-0012365X72900076-main.pdf?_tid=1255f97e-7382-11e7-9d07-00000aab0f01&acdnat=1501238995_2af031d7b204f70c6f758f9a2c8d54f7), per la quale una label degree sequence è associata univocamente ad una configurazione del grafo. E' perciò possibile calcolare il numero di isomorfi genenerando le *n-1*  label degree sequence ottenute tramite rotazione circolare della triangolazione ottenuta e contare il numero *S* di sequenze identiche.
Questo è il numero di isomorfi ruotati generati; per il calcolo del numero di mirror presenti è invece necessario ribaltare la sequenza e vedere se c'è una sovrapposizione con una delle *n-1* sequenze precedentemente generate. In caso affermativo il numero di isomorfi è *Sx2*, altrimenti è pari a *S*. Questo perchè una delle triangolazioni mirror potrebbe in realtà coincedere con una delle rotazioni.

# Validazione

Il processo di validazione dell’algoritmo sopra descritto presenta diverse analogie con la verificare della non-contraffazione di un dado da gioco. Nel caso in questione il dado *F* facce, dove *F* è il numero delle possibili rappresentazioni di un grafo planare massimale non etichettato; mentre la probabilità che esca una configurazione piuttosto che un’altra è data da *1/F*. Similmente a quanto viene fatto per la verifica dei dadi, si è quindi effettuato un test del Chi quadro, ampiamente utilizzato per verificare che le frequenze dei valori osservati si adattino alle frequenze teoriche di una distribuzione di probabilità prefissata.

Similmente a quanto viene fatto per la verifica dei dadi, si è quindi effettuato un test del Chi quadro, ampiamente utilizzato per verificare che le frequenze dei valori osservati si adattino alle frequenze teoriche di una distribuzione di probabilità prefissata. Fissato l'errore tollerato al 5% (p-value = 0.05), dando uno sguardo alle tavole della distribuzione chi quadrato con *F-1* gradi di libertà  è risultato molto semplice verificare se rifiutare l'ipotesi nulla o meno. 
Il test del chi quadro è stato eseguito per  poligoni con *n* lati, con n compreso tra 6 e 13. Nella tabella sottostante sono riportati i risultati del test ottenuti:

| Lati del poligono | Estrazioni effettive/Grafi generati | Triangolazioni non isomorfe | Chi square ottenuto | Limite  |
|-------------------|-------------------------------------|-----------------------|---------------------|---------|
| 6                 | 232490/50000                        | 3                     | 0.00312             | 5.991   |
| 7                 | 526009/50000                        | 4                     | 5.752               | 7.815   |
| 8                 | 548027/50000                        | 12                    | 9.161               | 19.675  |
| 9                 | 802363/50000                        | 27                    | 21.4840             | 38.885  |
| 10                | 874090/50000                        | 82                    | 78.807              | 103.010 |
| 11                | 1058893/50000                       | 228                   | 223.2968            | 263.147 |
| 12                | 1144664/50000                       | 733                   | 672.499             | ~796    |
| 13                | 1287160/50000                       | 2282                  | 2339.5238           | ~2393   |

Per ogni poligono di n lati sono state eseguite 50000 estrazioni; nella seconda colonna è riportato il numero di estrazioni effettive sul numero di grafi generati.
Sempre nella tabella è mostrato il chi square ottenuto dal nostro test e qil valore limite presente nella tavole di distribuzione  chi quadrato (gradi di libertà  a(n) -1 e p-value=0.05). 
Osservando le ultime due colonne si può apprezzare il fatto che sia sempre possibile accettare l'ipotesi nulla per ogni poligono di n lati: la penultima colonna della tabella (il risultato del nostro test) contiene per ogni riga valori della statistica test inferiori a quelli contenuti nell’ultima (risultato atteso).

Possiamo concludere che il nostro “dado” è equilibrato.

# Esecuzione 
Per eseguire il software è sufficiente scaricare la repository, installare i moduli richiesti e digitare i seguenti comandi:
- per generare un grafo outerplanare massimale di *n* nodi *'python MainGenerator.py S n'*. L'output è l'insieme di triangolazioni espresse come triple di vertici.
- per generare *K* grafi outerplanari massimali per ciascun grafo di *n* nodi con *n* compreso tra *i* e *j* *'python MainGenerator.py M i j K'*. L'output sono i grafi outerplanari massimali espressi come  label degree sequence e la relativa conta. Viene anche fornito il valore del chi quadro.

NB: è possibile specificare al massimo un grafo di dimensione *255*, perchè viene sfruttata la corrispondenza tra interi e simboli ASCII.

# Autori
Valerio GregoriRamsesXVII

Mattia Iodice: [GitHub: [RamsesXVII](https://github.com/RamsesXVII)]

Alessandro Oddi: [GitHub: [adixia](https://github.com/adixia)]

Alessandro Sgaraglia: [GitHub: [AlexSgar](https://github.com/AlexSgar)]
