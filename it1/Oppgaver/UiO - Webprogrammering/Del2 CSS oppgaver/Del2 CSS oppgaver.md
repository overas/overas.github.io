CSS øvingsoppgaver
==================
Du skal nå bygge videre på sidene vi jobbet med sist. Oppgavene legger opp til en del eksperimentering på egenhånd.

Oppgave 1
---------
Her skal vi trene litt på blokk-struktur før vi går løs på siden vi startet på sist.

a) Opprett en html-fil med navn `test.html`. Legg inn standard html-struktur med head og body. Fyll inn alt som hører til i head. Opprett en css-fil med navn `test-style.css` . Koble denne til html-dokumentet.

b) Legg inn et main-element i body. Definer følgende stil-regler for elementet i `test-style.css`.

* En passende bredde i enheten vw (forslag: 75vw)
* En passende minimums-høyde (forslag: 70vh)
* En bakgrunnsfarge
* Sentrer elementet

c) Legg til et section-element inne i main. Gi den klasseattributten `content_box`. I `test-style.css`; definer følgende:

* En bakgrunnsfarge som gjør det mulig å lese sort tekst som ligger over.
* Definer elementet som et inline-block -element slik at det vil flyte på linje med søsken-elementer.
* En passende bredde i % (forslag: 20%). Pass på at elementet ikke er bredere enn at man kan ha flere elementer med samme bredde ved siden av hverandre i main-elementet.
* En passende minimums-bredde i px eller em.
* Minimumshøyde på ca 200px i px eller em.
* Passende indre og ytre marger (margin og padding)

d) Putt en eksempel-tekst inne i `content-box` -elementet i html-filen. Kopier deretter hele koden for content-box og opprett flere slike elementer under hverandre i main.

Lek litt med farger, størrelser og indre og ytre marger. Prøv å gjøre nettleser-vinduet bredere og smalere for å se om siden skalerer på en pen måte.

Oppgave 2
---------
Vi skal nå gå løs på siden vi jobbet med sist gang. Vi begynner med å endre strukturen i `index.html, slik at vi enkelt kan kopiere over endringene i de andre sidene.

a) Lag et header-element som omslutter h1-elementet som inneholder overskriften på siden. Endre overskriften til å være en generisk tittel som vi kan benytte på alle sidene på nettsiden vår. Gi header-elementet identifikatoren `main_header`.

Kode:

```html
<header id="main_header"><h1>Min side</h1></header>
```
		  
I css-filen vi opprettet sist legger vi inn en definisjon som spesifiserer følgende for hashtag-selektoren med id `main_header`:

* Sentrer innholdet
* h1-elementer i elementet skal ha en passende font-størrelse.

Eksempel:

```css
#main_header {
    text-align: center;
    }

#main_header h1 {
    font-size: 1.8em;
    }
```


b) Lag et nav-element som omslutter den usorterte listen vi laget sist. Gi den identifikatoren `main_nav` i `style.css`, definer følgende for main_nav:

* Sentrer innholdet.

Definer så følgende for alle `li-elementer` i main_nav:

* Sett display slik at elementet oppfører seg som et inline-block -element
* Sett passende indre marger (padding) (forslag: 20px)
* Sett en passende bakgrunnsfarge
* Juster ytre marger (margin) slik at det ser ut som du ønsker.

c) Legg til en definisjon som endrer bakgrunnsfargen på et element i listen dersom vi holder musen over. Dette gjøres med pseudoklassen hover.

Eksempel:

```css
#main_nav li:hover {
    background-color: #F0F0F0;
    }
```
	
Se om du kan lage en pen meny ut av en liste.

Oppgave 3
---------
Du skal nå definere stiler for hovedinnholdet på siden, slik at det får et penere utseende.

a) Lag et main-element som omslutter innholdet på siden din. Vi snakker her om innholdet som ligger etter menyen. Definer passende stiler for main-elementet og eksperimenter med å sette inn blokk-elementer inni main for å skape et pent design.

b) Kopier over den nye stukturen vår til de andre nettsidene, og sørg for at innhold og tekst passer sammen.

Oppgave 4
---------
Vi skal nå lage en ny underside for nettsiden vår. Siden skal fungere som et bildegalleri, og skal skalere pent til alle skjermstørrelser.

Se dette [eksempelet](https://folk.uio.no/magl/undervisning/webprogrammering/eksempler/responsiveBilder/) for inspirasjon 

a) Start med å opprette en fil med navn `pictures.html`. Kopier så strukturen fra `index.html` over i denne, og fjern alt innholdet i main-elementet. Lag et section-element inni main-elementet. Gi elementet klassenavn `thumbnails_container`.

b) Finn noen eksempelbilder med et noenlunde likt forhold mellom høyde og bredde.
Evt: Last ned en pakke med bilder [her](https://folk.uio.no/magl/undervisning/webprogrammering/losningsforslag/Webprog%20-%20eksempelbilder%20oppgave%204.zip).
Legg disse bildene inn på siden ved hjelp av img-elementet. Ikke definer bredde og høyde her, da vi vil gjøre dette i css senere.

c) Definer så en stil for alle img-elementer som ligger i `thumbnails_container` i `style.css`.

Eksempel:

```css
.thumbnails_container img {
    /*din kode*/
    }
```
	    
Definer følgende:

* Display som inline-block
* Passende bredde og høyde
* Passende minimum- og maksimum-bredde og høyde.
* Ytre marger (margin)

Prøv deg frem med ulike css-definisjoner, og se hvordan bildene automatisk tilpasser seg skjermbredden.