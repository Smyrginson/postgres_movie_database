Serwis IMDB udostępnia część swojej bazy filmów w postaci plików TSV:

http://www.imdb.com/interfaces/
Przygotuj w Pythonie skrypt, który zaimportuje zawartość title.basics.tsv.gz  (https://www.dropbox.com/s/3do9bu0awq048uh/title.basics.tsv.gz?dl=0)  oraz name.basics.tsv.gz  (https://www.dropbox.com/s/xaidig3yw2viyym/name.basics.tsv.gz?dl=0)  do bazy PostgreSQL. Dane powinny trafić do nie więcej niż 3 tabel. Zatem nie przewidujemy dla pól takich jak genres, primaryProfession  osobnych tabel, ale jednocześnie - inaczej niż jest to napisane w ich dokumentacji - zakładamy, że w przyszłości mogą one zawierać więcej niż te 3 elementy w tablicy (np. 5 lub 7), więc trzeba mieć to w tyle głowy.
Oprócz importera, stwórz w Pythonie zalążek REST API, które teoretycznie można by w przyszłości dalej rozwijać. Podstawowy wymóg to endpointy, które pozwolą:

-Pobrać listę - wg kolejności alfabetycznej - wszystkich tytułów filmów o wskazanej wartości startYear, wraz z powiązanymi z nimi osobami (mechanizm z paginacją wyników).
-Jak wyżej, ale z możliwością wylistowania filmów z wskazanym genre.
-Zwrócić filmy, z którymi związane są osoby pasujące do wyników wyszukiwania (czyli jako parametr przekazujemy frazę - np. z nazwiskiem, na podstawie której szukamy ludzi i dla każdego z nich zwracamy listę tytułów filmów).


Create database:
    extract title.basics.tsv.gz as title_data.tsv in project main tree
    extract name.basics.tsv.gz as name_data.tsv in project main tree

    Postgres create database named "movies"

    Make data migration by flask
        flask db init
        flask db migrate
        flask db upgrade


API request manual:
GET: localhost:5000/loadactors - load actors from file to database
GET: localhost:5000/loadmovies - load movies from file to database
POST: localhost:5000/known (JSON { "name": "actors_name"}) - load actors movie
GET: localhost:5000/year/<int:year> - show movies by year order_by title
POST: localhost:5000/yearandgenre (JSON { "year": "year", "genre": "genre_type"}) - show movies filter by year and genre
POST: localhost:5000/playinmovie (JSON { "name": "actors_name"}) show movies with play actor

