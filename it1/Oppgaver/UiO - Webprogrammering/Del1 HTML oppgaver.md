HTML øvingsoppgaver
===================

Oppgave 1
---------
a) Opprett en fil kalt `index.html`. Sett opp grunnstrukturen for et HTML-dokument, med blant annet head og body. Angi deretter en passende nettside-tittel i title-elementet i head.

b) Lag en passende hovedoverskrift og en informasjonstekst om innholdet på siden. Benytt linjeskift hvor dette er passende.

c) Lag to sider til, `about.html` og `contact.html`. Kopier strukturen du lagde i `index.html` over i disse. Endre overskrifter og tekst slik at det passer til de nye sidene.

Oppgave 2
---------
a) Lag en liste med lenker til disse tre nettsidene i `index.html`. Når du er fornøyd med utseende til listen, kopiér koden inn i de to andre sidene. Dette skal fungere som en meny, og burde derfor ligge rett under hovedoverskriften på nettsiden.

b) Sett inn et bilde av deg selv på siden `index.html`. Juster størrelsen slik at det passer. Husk å legge til et passende “alt”-attributt.

Oppgave 3
---------
a) På siden `about.html`, legg til en tabell med kolonner og rader som presenterer hvilke fag du tar ved Arendal vgs. Hver rad skal innholde informasjon om ett fag. Første rad skal inneholde beskrivelser for hver enkelt kolonne. Kolonnene kan for eksempel være programfag, antall timer i uken, eksamensform. Mere informasjon om prgramfagene finner du her: [Programfag Arendal vgs](https://www.austagderfk.no/skole/vgs/arendal-videregaende-skole/opplaringstilbud/programfag/).

b) Gjør det slik at når man trykker på programfaget, blir man sendt til den respektive emnesiden hos Arendal vgs.

c) Sett inn en passende overskrift over tabellen.

Oppgave 4
---------
a) Opprett en ekstern CSS-fil med navn `style.css`. Se side 125 i kode1-læreboken hvordan du gjør dette. Knytt denne filen med de tre HTML-dokumentene ved å legge til et link-element under head.

b) Gå inn på Google Fonts, og let frem til en font du liker. Følg instruksjonene på nettsiden for å inkludere denne på nettsidene.

c) Sett font-typen for body-elementet til fonten du lastet ned fra Google Fonts.

d) Legg inn en stildefinisjon som fjerner den blå understrekingen til linkene, og setter tekstfargen til sort.

Eksempel:

```css
a {
	text-decoration: none;
}
```