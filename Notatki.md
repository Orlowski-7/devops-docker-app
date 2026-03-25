
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

    // Zapamiętaj #5

    Response time > samo CPU

    CPU może być niskie, a aplikacja i tak może działać źle.
    Ale jeśli response time rośnie, to użytkownik już to czuje.

    // Zapamiętaj #6

    Monitoring warto układać warstwami:

    aplikacja
    baza
    infrastruktura

    To porządkuje myślenie i debug.

    // Zapamiętaj #7

    /metrics to standardowy endpoint dla Prometheusa.

    To bardzo częsty wzorzec:

    aplikacja wystawia metryki
    Prometheus je scrapuje
    Grafana je wizualizuje

    // Zapamiętaj #8

    Nie logika aplikacji monitoruje system.
    Aplikacja tylko udostępnia metryki.

    To Prometheus jest tym, który je zbiera.

    // Zapamiętaj #9

    Prometheus nie „wie” sam z siebie, co monitorować.
    Trzeba mu powiedzieć:

    gdzie iść
    jaki endpoint scrapować
    jak często

    Czyli to Ty definiujesz źródła prawdy.

    // Zapamiętaj #10

    Grafana nie zbiera danych.
    Grafana tylko je pokazuje.

    Czyli podział jest taki:

    app wystawia /metrics
    Prometheus zbiera
    Grafana wizualizuje

    To bardzo ważny model.


    <<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>

                    L: admin
                    Hasło Gfana @Admin#
    <<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>

    W środku kontenerów localhost oznacza ten konkretny kontener, a nie Twój komputer.

    // Zapamiętaj #11

    W środku kontenerów localhost oznacza ten konkretny kontener, a nie Twój komputer.

    To dlatego Grafana łączy się do:

    http://prometheus:9090

    a nie do localhost:9090.

    To jest jedna z najważniejszych rzeczy w Dockerze.


    rate(app_request_count_total[1m])

    % ile requestów na sekundę
    % w ostatniej minucie

    rate(app_request_latency_seconds_sum[1m]) 
    /
    rate(app_request_latency_seconds_count[1m]) 

    % średni czas odpowiedzi
        
    app_request_count_total

    % ile requestów było od startu

    // Zapamiętaj #12

    Prometheus NIE przechowuje „średniej”.

    👉 musisz ją policzyć sam:

    sum / count

    To jest klasyczny wzorzec.

    // Zapamiętaj #13

    rate(...) to jedna z najważniejszych funkcji.

    👉 mówi „jak szybko coś rośnie”

    Czyli:

    ile requestów na sekundę
    ile błędów na sekundę

<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>
    CMD: // Test 
    curl.exe http://localhost:8080/data
<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>

    // Zapamiętaj #14

    👉 błędy też są metryką

    To jest jedna z najważniejszych rzeczy w monitoring:

    request count = ruch
    latency = wydajność
    error rate = stabilność

    // Error Rate 

    rate(app_error_count_total[1m])

    // Zapamiętaj #16

    W monitoringu ważniejsze od „czy jest wykres” jest:

    czy metryka naprawdę istnieje
    czy Prometheus ją scrapuje
    czy query odpowiada temu, co naprawdę liczysz

    To jest jedna z najważniejszych praktycznych lekcji w DevOps.

    // Zapamiętaj #17 (bardzo ważne)

    Monitoring czasem „kłamie przez chwilę”, zanim się ustabilizuje

    To NIE znaczy, że system nie działa.

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<WAŻNE DO WYKRESÓW>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

rate(app_request_count_total[1m])

rate(app_request_latency_seconds_sum[1m]) 
/
rate(app_request_latency_seconds_count[1m])

rate(app_request_count_total[1m])

rate(app_error_count_total[1m])

app_request_count_total <-- Istotne do wyświetlenia całokształtu ? 

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    // Zapamiętaj #18

    Labelki (endpoint, method) = mega potężne narzędzie

    To pozwala:

    rozbić ruch
    znaleźć problematyczny endpoint
    analizować system


<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<Skrypt do generowania ruchu>>>>>>>>>>>>>>>>>>>>>>>

            for ($i=0; $i -lt 100; $i++) {
            curl.exe http://localhost:8080/data
            }

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    // Zapamiętaj #19

    Latency nie zawsze musi rosnąć od samej liczby requestów.
    Rośnie wtedy, gdy system zaczyna dochodzić do limitów:

    CPU
    RAM
    połączeń do DB
    czasu odpowiedzi bazy
    blokad / kolejek

    Czyli bardziej precyzyjnie:

    większy ruch może zwiększyć latency, jeśli któryś komponent staje się bottleneckiem

    To ważna różnica, bo na rozmowie takie doprecyzowanie robi bardzo dobre wrażenie.

    // Zapamiętaj #20

    Counter zawsze rośnie
    Poza restartem procesu / kontenera.

    Dlatego do obserwacji ruchu zwykle nie patrzysz na sam counter, tylko na:

    rate(...)

    // Zapamiętaj #21

    Grafana pokazuje to, o co zapytasz.
    Jeśli query jest słabe, dashboard też będzie słaby.

    Czyli:

    metryka może być dobra
    a dashboard bezużyteczny
    bo pytasz o złą rzecz

    To jest bardzo praktyczna lekcja.

    // Zapamiętaj #22

    Monitoring ma odpowiadać na pytania operacyjne, np.:

    czy aplikacja działa?
    czy ruch rośnie?
    czy odpowiedzi są coraz wolniejsze?
    czy użytkownik dostaje błędy?

    Nie chodzi o „ładne wykresy”.

    // Zapamiętaj #23

    W tym projekcie:

    zmiana pliku lokalnie ≠ zmiana w działającym kontenerze
    kontener ma własny filesystem zbudowany z obrazu

    Czyli po zmianach w kodzie robisz:

    docker-compose up --build

    albo bezpieczniej:

    docker-compose down
    docker-compose up --build

    Jeśli chcesz mieć pewność, że naprawdę wstała nowa wersja, to właśnie tak.

    Bardzo ważna uwaga do Twojego handlera błędów:

                @app.errorhandler(Exception)
            def handle_exception(e):
                ERROR_COUNT.labels(endpoint=request.path).inc()
                return {"error": str(e)}, 500
    
    // Zapamiętaj #24

    Ten handler zliczy wyjątki, ale nie zliczy np. świadomie zwróconego:
    
    400
    404 ,bo to nie zawsze są wyjątki.

    Dlatego RESPONSE_COUNT jest tak naprawdę ważniejszą metryką operacyjną niż ERROR_COUNT.

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<WAŻNE DO WYKRESÓW>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    rate(app_request_count_total[1m])

    rate(app_request_latency_seconds_sum[1m]) 
    /
    rate(app_request_latency_seconds_count[1m])

    rate(app_request_count_total[1m])

    rate(app_error_count_total[1m])

    app_request_count_total <-- Istotne do wyświetlenia całokształtu ? 

    rate(app_response_count_total{status=~"5.."}[1m])

    rate(app_response_count_total{status=~"4..|5.."}[1m])

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    // Zapamiętaj #25

    Regex w Prometheus:

    =~  → match regex
    =   → exact match

    Przykłady:

    status="200"        ✔ dokładnie
    status=~"2.."       ✔ wszystkie 2xx
    status=~"4..|5.."   ✔ 4xx i 5xx

    // Zapamiętaj #26

    Brak danych ≠ błąd query

    Często:

    query jest poprawne
    ale metryka jeszcze nie istnieje

    