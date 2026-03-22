
-------------------------------------------------------------------------------
Notatki: 

# DAY 1

docker exec -it web-app bash // przykład wejście do kontenera (terminal)

docker-compose down // Stop kontenerów 

docker system prune -a // Delete wszystkich kontenerów 

docker-compose up --build // Ponowny build

docker-compose logs -f // Logi

docker-compose logs app  // przykład logs dla konteneru app

docker ps // Kontenery

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Endpointy: 

GET  /        → działa serwer
POST /data    → zapis do bazy
GET  /data    → odczyt z bazy

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

docker-compose down -v  // (to usuwa volume bazy) korzystać jeśli baza była tworzona i istnieje

docker-compose config // Sprawdza składnię YAML

Jeśli nie chce zbudować środowiska prune -a i restart !!!

## Git init and push

git init
git add .
git commit -m "Initial DevOps project: Dockerized app with Nginx and PostgreSQL"

git remote add origin https://github.com/TWOJ_LOGIN/devops-docker-app.git
git branch -M main
git push -u origin main

git branch -v // aktualny commit tytuł 

// Komunikacja między kontenerami

    host="db"

    ❌ nie localhost
    ✅ nazwa serwisu

//  init.sql działa tylko raz

    👉 tylko przy pierwszym starcie bazy
    👉 jak masz volume → nie odpali się drugi raz

// Retry connection

    👉 DB nie jest gotowa od razu
    👉 aplikacja musi być odporna

// Healthcheck

   👉 system musi wiedzieć czy działa

 
// Zapamiętaj #1

    Monitoring nie jest po to, żeby mieć wykresy.
    Monitoring jest po to, żeby:

    wykryć problem
    znaleźć bottleneck
    podjąć decyzję

// Zapamiętaj #2

    Najpierw patrzymy na:

        objaw
        metryki
        logi
    Dopiero potem coś zmieniamy.

// Zapamiętaj #3

    W prostym systemie monitorujemy minimum:

        host/kontener
        aplikację
        bazę
    To jest bardzo dobry bazowy model.

// Metryki infrastruktury

    Czyli „czy maszyna / kontener żyje”

    Przykłady:

    CPU
    RAM
    disk usage
    network traffic

    To daje odpowiedź:

    czy system ma zasoby

// Metryki aplikacyjne

    Czyli „czy aplikacja działa poprawnie”

    Przykłady:

    liczba requestów
    czas odpowiedzi
    liczba błędów 4xx/5xx
    liczba requestów na endpoint

    To daje odpowiedź:

    czy użytkownik odczuwa problem

// Metryki bazy danych

    Czyli „czy backend danych nadąża”

    Przykłady:

    liczba połączeń
    liczba zapytań
    czas wykonywania zapytań
    locks / waiting queries

    To daje odpowiedź:

    czy DB jest bottleneckiem

    // Dashboard 1 — App

    Tu chcesz widzieć:

    request count — ile requestów przychodzi
    response time / latency — jak szybko odpowiada app
    error rate — ile jest błędów 4xx/5xx albo wyjątków
    health status — czy /health przechodzi
    opcjonalnie: liczba requestów na endpoint

    To odpowiada na pytanie:

    czy aplikacja działa dobrze z perspektywy użytkownika

    // Dashboard 2 — Infra / DB

    Tu chcesz widzieć:

    CPU
    RAM
    disk usage
    network traffic
    db connections albo podstawowy stan DB

    To odpowiada na pytanie:

    czy środowisko ma zasoby i czy baza/host nie są bottleneckiem

    Co chcę, żebyś zapamiętał z tego etapu

    // Zapamiętaj #4

    Nie wszystko, co się monitoruje, jest równie ważne.

    Priorytet zwykle jest taki:

    czy aplikacja działa
    czy użytkownik ma problem
    czy zasoby się kończą
    dopiero potem bardziej szczegółowe rzeczy
    Zapamiętaj #5

    Response time > samo CPU

    CPU może być niskie, a aplikacja i tak może działać źle.
    Ale jeśli response time rośnie, to użytkownik już to czuje.

    // Zapamiętaj #6

    Monitoring warto układać warstwami:

    aplikacja
    baza
    infrastruktura

    To porządkuje myślenie i debug.
