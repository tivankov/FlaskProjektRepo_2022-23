# Flask projekt kolegija "Programiranje za web"

## Krati opis
Ovo je web stranica izmišljenog gurmanskog sajma.
Stranica je namijenjena je svim ljubiteljima hrane.
Preko stranice korisnik može vidjeti sve događaje na sajmu i 
napraviti rezervaciju mjesta. Također stranica osigurava
plaćanje kapare/pologa kako bi se potvrdila rezervacija.
Stranica je napisana u Flasku, HTML-u.
Pomoću JINJA templatea je osigurano lakše uređivanje
važnih informacija na stranici


## Upute za pokretanje web stranice
* git clone https://github.com/unizd-sit-web/flask-projekt-tivankov.git
* cd flask-projekt-tivankov
* py -m venv venv
* \venv\Scripts\Activate.ps1
* pip install -r requirements.txt
* $env:FLASK_APP = ”web.py”
* $env:FLASK_DEBUG="1"
* flask run

---

## Zadatak
Potrebno je samostalno osmisliti i isprogramirati Flask web aplikaciju.

Poželjno je primjeniti većinu od dosad naučenih tehnika/tehnologija/jezika:
* Python + Flask
* Komentari u kodu
* HTML, CSS, JavaScript
* Predlošci
* Web forme
* Bootstrap ili sličan CSS framework
* _Opcionalno (samostalno istraživanje i rad): Autentifikacija, autorizacija, logiranje, internacionalizacija, testovi, SQLite, SQLAlchemy, Flask-sqlalchemy, migracije._

## Primjeri web aplikacija (ideje):
* Osobni portal
* Restoran (uvod, ponuda dana, o nama, meni, preporuka chefa, ostale usluge, slike, osoblje, rezervacija…)
* Teretana (uvod, usluge, tjedni raspored, sadržaj, treneri…)
* Događaj (opis, raspored, promo sadržaj, nadolazeći događaj, vijesti, registracija, cijene…)
* Agencija (usluge, marketing, nekretnine, consulting, putovanja, vjenčanja…)
* Proizvodi (popis, detalji, način plaćanja, način isporuke, osvrti kupaca…)
* Ustanova (škola, sveučilište, zapošljavanje, obrazovna institucija)
* Blog
* Ostalo

Izvorni kod je potrebno staviti na GitHub račun, a README.md datoteka projekta mora sadržavati tehničku specifikaciju aplikacije (koja uključuje opis aplikacije, kome je namijenjena, koje tehničke aspekte sadrži i koristi, i sl.)

## Ocijenjivanje
* Korištene tehnike
* Urednost programskog koda
* Vizualni dizajn Web aplikacije i inovativnost
* Ispravnost rada web aplikacija
* Složenost web aplikacije
* Dokumentiranost Web aplikacije
* Rok u kojem se predala Web aplikacija i dokumentacija (postoje 2 roka)

Kad web aplikaciju i popratnu dokumentaciju završite, kreirajte tzv. Pull request kako bi istu mogli pregledati.
Pri pregledu prijave, ukoliko smatramo da su potrebne neke dorade na projektu, evidentirat ćemo "issues" zapise na GitHub-u projekta, koje ćete trebati "zatvoriti".