
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

