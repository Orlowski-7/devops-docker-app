
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

    WAŻNE!! Poniższe w trybie code nie builder 

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

    // Zapamiętaj #27

    Monitoring pokazuje to, co naprawdę wydarzyło się w systemie.
    Nie to, co „mogłoby się wydarzyć”.

    Czyli jeśli nie było:

    400
    500

    to nie będzie danych dla tych statusów.

    // Zapamiętaj #28

    Brak danych w monitoringu może być poprawnym stanem.
    Nie każdy brak wykresu oznacza awarię.

    Zapamiętaj #29

    Aby testować monitoring, czasem trzeba świadomie wygenerować zdarzenie:

    ruch
    błąd
    przeciążenie

    To jest bardzo praktyczne i bardzo „DevOpsowe”.

    // Zapamiętaj #30

    W Grafanie są dwa różne tryby pracy z query:

    Builder

    Dobry do prostych klikanych rzeczy.

    Code

    Lepszy do prawdziwego PromQL.

    Przy regexach, rate, filtrach po labelach:
    👉 Code jest po prostu lepszy.

    // Zapamiętaj #31

    Jeśli metryka ma dużo labeli, to bez filtrowania będziesz widział szum.

    U Ciebie szum robią:

    /metrics
    /health

    Dlatego warto filtrować po:

    endpoint
    status
    czasem method

    // Zapamiętaj #32

    👉 Grafana Builder ≠ pełny PromQL

    Builder → prosty UI
    Code → prawdziwe query

    I w praktyce:

    80% sensownej pracy robisz w Code

    // Zapamiętaj #33

    👉 Debugowanie monitoringu = 3 warstwy

    Czy metryka istnieje? (Prometheus /metrics)
    Czy Prometheus ją widzi? (/targets, query)
    Czy Grafana poprawnie pyta?

    Ty właśnie przeszedłeś cały ten flow.

    WYWOŁANIE BŁĘDU 400: 

    curl.exe -X POST http://localhost:8080/data -H "Content-Type: application/json" -d "{}"

    <<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<WAŻNE DO WYKRESÓW>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    rate(app_request_count_total[1m])

    rate(app_request_latency_seconds_sum[1m]) 
    /
    rate(app_request_latency_seconds_count[1m])

    rate(app_request_count_total[1m])

    rate(app_error_count_total[1m])

    app_request_count_total <-- Istotne do wyświetlenia całokształtu ? 

    WAŻNE!! Poniższe w trybie code nie builder 

    rate(app_response_count_total{status=~"5.."}[1m])

    rate(app_response_count_total{status=~"4..|5.."}[1m])

    -----------------------------------------------------------------------------------------

    Gotowy zestaw monitorowania endpointów na ten moment 27.03

    rate(app_request_count_total{endpoint="/data"}[1m])
    👉 ile requestów trafia do API

    rate(app_request_latency_seconds_sum{endpoint="/data"}[1m]) 
    /
    rate(app_request_latency_seconds_count{endpoint="/data"}[1m])
    👉 ile requestów trafia do API

    rate(app_response_count_total{endpoint="/data",status=~"4..|5.."}[1m])
    👉 jak szybko odpowiada app

    rate(app_response_count_total{endpoint="/data",status=~"2.."}[1m])
    👉 ile requestów kończy się sukcesem

    rate(app_response_count_total{endpoint="/data"}[1m])

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

    // Zapamiętaj #34

    To jest klasyczny zestaw:

    request rate → ruch
    latency → wydajność
    error rate → stabilność
    success rate → zdrowie systemu

    To jest dokładnie to, co się monitoruje w realnych systemach.

    🔥 Mini symulacja (ważne)

    Zrób:

    1️⃣ Spam dobrych requestów
    curl.exe http://localhost:8080/data
    2️⃣ Spam błędnych requestów
    curl.exe -X POST http://localhost:8080/data -H "Content-Type: application/json"

    // Zapamiętaj #35

    👉 Monitoring musi być czytelny

    Nie chodzi o to, żeby:

    - mieć dużo danych

    - Chodzi o to, żeby:

    - widzieć to, co ważne

    // Zapamiętaj #36

    👉 /metrics i /health prawie zawsze trzeba filtrować

    Bo:

    generują szum
    zaburzają analizę
    nie reprezentują realnego ruchu usera

    // Zapamiętaj #37

    👉 Zawsze commituj w momentach „stabilnych milestone’ów”

    Czyli:

    działa ✔
    rozumiesz ✔
    możesz wrócić ✔

    To jest bardzo ważny nawyk.


    --------------------------------------- Monitoring infrastruktury --------------------------


    🚀 NOWY ETAP (i to jest ważne)

    Wchodzimy w:

    🧱 Monitoring infrastruktury (CPU / RAM / kontenery)

    Czyli coś, co:

    👉 bardzo często pada na rozmowach
    👉 bardzo mało ludzi umie dobrze zrobić

    🎯 Cel następnego etapu

    Chcemy widzieć:

    CPU usage kontenerów
    RAM usage
    network
    disk I/O
    🔧 Jak to robimy

    Dodajemy:

    🔹 cAdvisor

    To jest narzędzie od Google, które:

    👉 zbiera metryki kontenerów Dockera

    // Zapamiętaj #38

    👉 Prometheus nie widzi Dockera „sam z siebie”

    On widzi tylko:

    to co wystawisz jako endpoint

    Czyli:

    app → /metrics
    Docker → przez cAdvisor

    // Zapamiętaj #39 (wersja „na rozmowę”)

    Monitoring aplikacji pokazuje objawy,
    monitoring infrastruktury pokazuje przyczynę.

    🎯 Przykład (bardzo ważny)

    Masz:

    latency rośnie
    error rate rośnie

    👉 Monitoring aplikacji mówi:

    „coś jest nie tak”

    Ale dopiero monitoring infra powie:

    CPU = 100% → bottleneck CPU
    RAM = brak → OOM / swap
    DB = przeciążona → wolne query
    network → timeouty

    👉 czyli:

    „dlaczego coś jest nie tak”

    🧠 Zapamiętaj #40

    👉 Bez infra monitoringu jesteś ślepy na przyczynę problemu

    Masz tylko:

    symptomy (slow, error)

    Nie masz:

    root cause
    🔥 I to jest bardzo ważna rzecz

    To co robisz teraz to:

    👉 łączysz:

    aplikację
    metryki
    infrastrukturę

----------------------------- Infra Monitoring ----------------------------------------------

    // Panel 1 — CPU usage

    rate(container_cpu_usage_seconds_total[1m])
    👉 pokazuje użycie CPU w czasie

    // lepsza wersja (per container)
    rate(container_cpu_usage_seconds_total{name=~".+"}[1m])

    // Panel 2 — RAM usage
    
    container_memory_usage_bytes
    👉 ile RAM używa kontener

    // Panel 3 — Network

    rate(container_network_receive_bytes_total[1m])
    👉 ile danych przychodzi

    // Panel 4 — Network OUT

    rate(container_network_transmit_bytes_total[1m])
    👉 ile danych wychodzi

    // MAŁY PRO TIP (ważny)

    cAdvisor zwraca dużo śmieci (systemowe kontenery).

    Dlatego filtruj:

    rate(container_cpu_usage_seconds_total{name=~"devops-docker-app.*"}[1m])

    albo po:

    container_label_com_docker_compose_service

-------------------------------------------------------------------------------------------

    // Zapamiętaj #41

    👉 container metrics ≠ app metrics

    app → requesty, latency
    container → CPU, RAM

