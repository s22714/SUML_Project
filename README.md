# SUML_Project

## Spis treści
1. [Opis i cel aplikacji](#opis-i-cel-aplikacji)
2. [Technologie i narzędzia](#technologie-i-narzędzia)
3. [Dane wejściowe](#dane-wejściowe)
4. [Czyszczenie danych](#czyszczenie-danych)
5. [Modelowanie i proces trenowania modelu](#modelowanie-i-proces-trenowania-modelu)
6. [Instrukcja obsługi aplikacji](#instrukcja-obsługi-aplikacji)
7. [Podsumowanie](#podsumowanie)
  
## Opis i cel aplikacji

<p>Aplikacja ma wesprzeć sprzedawców jak i kupujących w sprawdzeniu średniej ceny auta przy określonych parametrach. Pozowoli to na ochrone przed zbyt tanimi/drogimi ofertami.</p>

## Technologie i Narzędzia

Do utworzenia aplikacji został użyty Python z następującymi bibliotekami:

- **Streamlit** - szybki interfejs aplikacji umożliwiający łatwe wprowadzenie zmian.
- **Autogluon** - narzędzie AutoML do automatycznego szkolenia i wyboru najlepszego modelu uczenia maszynowego.
- **Pandas** - do analizy i przetwarzania danych.
- **Scikit-learn** - do czyszczenia, przetwarzania i standaryzacji danych.
- **Kagglehub** - szybki dostęp do datasetów bez potrzeby przechowywania ich lokalnie.


## Dane Wejściowe
Aplikacja korzysta z datasetu: [Belarus Used Cars Prices](https://www.kaggle.com/datasets/lepchenkov/usedcarscatalog).

**Charakterystyka datasetu:**
- Liczba rekordów: około 38,5 tys.
- Liczba kolumn: 30.

**Powody wyboru datasetu:**
- Duża liczba rekordów w porównaniu z innymi datasetami (~10k w większości przypadków).
- Zawiera istotne kolumny, np. typ auta czy rodzaj napędu, pomijane w innych datasetach.
- Niska liczba braków danych (zazwyczaj mniej niż 10%).

**Opis kluczowych kolumn:**

| Nazwa kolumny | Opis |
|:-------------------|:------------------------------------------------|
| manufacturer_name | Nazwa marki samochodu |
| model_name | Nazwa modelu samochodu |
| transmission | Rodzaj skrzyni biegów |
| color | Kolor samochodu |
| odometer_value | Przebieg auta |
| year_produced | Rok produkcji |
| engine_fuel | Rodzaj paliwa |
| engine_has_gas | Czy samochód jest wyposażony w zbiornik propanu? |
| engine_type | Typ silnika |
| engine_capacity | Pojemność silnika |
| body_type | Typ samochodu |
| has_warranty | Czy samochód jest ubezpieczony? |
| state | Stan samochodu |
| drivetrain | Rodzaj napędu |
| price_usd | Cena w dolarach amerykańskich |
| is_exchangeable | Czy właściciel jest gotowy na wymianę auta (z małym bądź brakiem dodatkowego zapłacenia) |
| location_region | Lokacja ogłoszenia |
| number_of_photos | Liczba zdjęć |
| up_counter | Liczba podwyższeń cen auta |
| feature_0 - feature_9 | Dodatkowe wyposażenie auta |
| duration_listed | Ile dni samochód był wystawiony na aukcji |

## Czyszczenie danych
Przed trenowaniem modelu przeprowadzono czyszczenie danych:

1. **Usunięto następujące kolumny:**
   - `drivetrain` (zmieniona nazwa na `drive`).
   - `is_exchangeable` (nie wpływa na cenę pojazdu).
   - `location_region` (lokacja nie jest kluczowa dla predykcji ceny).
   - `feature_0` - `feature_9` (brak szczegółowych informacji).

2. **Przetwarzanie braków danych:**
   - Usunięto rekordy z dużą liczbą braków.
   - Wartości liczbowe uzupełniono średnią.
   - Wartości kategoryczne uzupełniono najczęściej występującymi wartościami.

3. **Standaryzacja danych:**
   - Kolumny numeryczne: standaryzowane na rozkład o średniej 0 i odchyleniu standardowym 1.
   - Kolumny kategoryczne: zakodowane przy użyciu OneHotEncoder.

## <li>Modelowanie i Proces Trenowania Modelu</li>

Do automatycznej analizy modeli zastosowano bibliotekę **Autogluon**, która umożliwia:

- Automatyczny wybór najlepszego modelu na podstawie wyników walidacji.
- Eksport najlepszych modeli do formatu `.pkl` (pickle).
- Wykluczanie niepotrzebnych modeli.
- Automatyczne dostrajanie hiperparametrów.


**Wybrany model:** LightGBMXT

**Charakterystyka modelu LightGBMXT:**
- Wysoka wydajność w uczeniu.
- Obsługa braków danych.
- Przetwarzanie równoległe (wydajność na dużych zbiorach danych).
- Wsparcie dla wartości kategorycznych i liczbowych.
  
### Instrukcja Obsługi Aplikacji
1. Wybierz interesującą markę samochodu z listy (np. Nissan).
2. Wybierz model auta.
3. Wybierz rodzaj skrzyni biegów i kolor.
4. Wpisz przebieg auta.
5. Wybierz rok produkcji za pomocą paska wyboru.
6. Określ rodzaj paliwa. Jeśli samochód ma instalację LPG, zaznacz checkbox.
7. Pojemność silnika wpisz w litrach (np. 1.6). Jeśli nie jesteś pewien, sprawdź w dowodzie rejestracyjnym.
8. Wybierz typ auta (np. sedan, SUV).
9. Zaznacz, czy pojazd posiada OC.
10. Określ stan auta oraz rodzaj napędu.
11. Zaznacz, jeśli sprzedający jest pierwszym właścicielem.
12. Wybierz walutę, w której chcesz otrzymać predykcję, i kliknij "Oblicz cenę".
    
### Wynik:
- Aplikacja poda oszacowaną cenę samochodu.
- Jeśli przewidywana cena < 0, wyświetli komunikat, że auto nie nadaje się do sprzedaży.

  ### Uruchamianie lokalne:
Aby uruchomić aplikację lokalnie:
1. Skopiuj kod źródłowy aplikacji.
2. Zainstaluj wymagane biblioteki, wykonując poniższe polecenie w terminalu:

   ```bash
   pip install -r requirements.txt
   ```

3. W terminalu wpisz:

   ```bash
   streamlit run app.py
   ```

## Podsumowanie
Aplikacja ma duży potencjał zastosowania w realnym świecie. Plany na przyszłość obejmują:

- Obliczanie kosztów napraw i wymian części.
- Analiza ryzyka wymiany rozrządu.
- Szacowanie kosztów ubezpieczenia OC i AC.
- Prognozowanie czasu potrzebnego na sprzedaż auta.
- Dodanie przedziałów cenowych, podobnych do serwisu [Otomoto](https://www.otomoto.pl/osobowe/bmw).
- Analiza popularności marek i modeli.

Dalsze rozwijanie projektu może znacznie zwiększyć jego funkcjonalność i użyteczność.
