# project_b_sprint_2

Dit programma sorteert een lijst van Steam games (opgehaald door de SteamAPI), en geeft statistieke data over de games.
Het programma maakt gebruik van meerdere sorting algorithms, die allemaal gekozen kunnen worden om de lijst te sorteren.
 - Insertion sort neemt een voor een elementen uit de lijst, en voegt ze in het resultaat in op de correcte plek.
 - Merge sort splitst de lijst op in kleinere en kleinere delen, en voegt die delen dan op volgorde samen tot een gesorteerd geheel.
 - De Binary Search Tree vervormt de lijst tot een grafische boom en klapt die boom daarna in tot een gesorteerde lijst.
Om de statistiek te weergeven wordt er gebruik gemaakt van Chart.js.

Verder hebben wij nog een extra pagina die de top 100 games van 2 weken ophaalt. Elke 2 weken komt er dus nieuwe data erin te staan.

Hoe kan ik dit runnen?
Allereerst moet u Django geinstalleerd hebben. Dit kan doormiddel van "pip install Django" te doen in uw terminal.
Vervolgens, als u het bestand download en uitpakt kunt in de root van het bestand in uw terminal "python manage.py runserver" doen en uw project zal op uw localhost gestart worden.
Als dit al niet gebeurd kunt u in uw browser (bij voorkeur Google Chrome) in de url-bar uw localhost:8000 intypen en het project staat daar voor u om gebruikt te worden.
