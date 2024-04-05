# DISTRIBUCIÓ DE TASQUES:

- **Exercici 1**: Ramon Canal Fort
- **Exercici 2**: Carlota Fernández Pensado i Emma Juanico Sala
- **Exercici 3**: Emma Juanico Sala i Carlota Fernández Pensado

# RESOLUCIONS EXERCICIS:

## Exercici 1:

Per a convertir el model ER proposat a un conjunt de col·leccions, hem pensat en la següent estructura:

### Col·leccions:

1. **Clients**: On guardem tota la informació del client.

2. **Tiquets**: On guardem tota la informació del tiquet (incloent el nom del producte) i l'associem al client que fa la compra. També enregistrem si el client ha vingut en cotxe o no.

3. **Productes**: On guardem tota la informació del producte i, en cas que tingui subproductes, utilitzem un diccionari on les claus són els noms dels subproductes i els valors indiquen la quantitat de cada un.

4. **Cotxes**: On guardem tota la informació del cotxe i el nom i cognoms del seu propietari. També registrem les estades amb tota la informació corresponent, i a les estades, hi associem la plaça de pàrquing.

5. **Places**: On guardem tota la informació sobre les places de pàrquing.

### Decisions de Disseny:

- Hem optat per encastar clients i tiquets perquè els dos són nombrosos i per la primera consulta.
- Encastem els clients als tiquets per reduir la redundància i no omplir massa la col·lecció de clients.
- Pel productes compostos, hem optat per referenciar els subproductes en un diccionari dins del producte compost per reduir redundàncies.
- Hem decidit encastar totes les estades a cotxes i no fer-li una col·lecció, ja que estades és entitat feble de cotxe. Hem encastat la plaça de pàrquing a les estades per simplificar la visualització i perquè només hi ha un pàrquing per estada.

## Exercici 2:

S'han creat les col·leccions en un document JSON seguint el format esmentat a l'exercici anterior.

## Exercici 3:

1. Nombre de clients atesos durant un mes/any en concret amb tiquet superior a 500€.
2. Mostra la informació del client de Barcelona amb major edat.
3. Valor màxim, mínim i mitjà dels preus dels productes.
4. Mostra 5 clients que mai venen en cotxe a la tenda.
5. Foto actual del pàrquing (o en una data concreta). Mostrar plaça, dades del vehicle estacionat i el nom i cognom del client.
6. Productes formats per més de 4 subproductes (pack).
7. Llistat de productes agrupats per categoria.
8. Nombre de tiquets segons el tipus de pagament.
9. Mostrar el nom i cognom dels clients que han comprat un producte específic.
