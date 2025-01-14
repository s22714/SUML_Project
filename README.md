# SUML_Project

## Spis treści
<ol>
  
## <li>Opis i cel aplikacji</li>

<p>Aplikacja ma wesprzeć sprzedawców jak i kupujących w sprawdzeniu średniej ceny auta przy określonych parametrach. Pozowoli to na ochrone przed zbyt tanimi/drogimi ofertami.</p>

## <li>Technologie i Narzędzia</li>

Do utworzenia aplikacji został użyty Python z następującymi bibliotekami:
<ul>
  <li>Streamlit - jako szybki interfejs aplikacji. Jego prostota umożliwia szybkie wprowadzenia zmian.</li>
  <li>Autogluon - jeden z paru modeli automatycznego szkolenia ML.</li>
  <li>Pandas - do analizy danych.</li>
  <li>Scikit-learn - do przetwarzania, oczyszczania i normalizacji danych</li>
  <li>Kagglehub - do szybkiego dostępu do datasetu bez potrzeby trzymania go w plikach</li>
</ul>

## <li>Dane Wejściowe</li>
<p>Do aplikacji zostały użyte poniższy dataset <a href=https://www.kaggle.com/datasets/lepchenkov/usedcarscatalog>Belarus Used Cars Prices</a></p>
</a>
<p>Dataset posiada:
<ul>
  <li>około 38.5k rekordów oraz,</li>
  <li>30 kolumn.</li>
</ul></p>
<p>Poniżej znajduje się opis zawartych kolumn:</p>

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


## <li>Modelowanie i Proces Trenowania Modelu</li>

<p>Do przeprowadzenia automatycznej analizy modeli, została zastosowana biblioteka Autogluon. Pozwala ona na wybranie najlepszych modeli wraz z odpowiednio ustawionymi parametrami. Dodatkowymi plusami tego narzędzia AutoML są:
  <ul>
    <li>Eksport najelpszych rozwiązań do formatu .pkl (pickle).</li>
    <li>Możliwość wykluczania konkretnych modeli (Przy założeniu, że są one nam niepotrzebne.).</li>
    <li>Automatyczne przypisywanie hiperparametrów.</li>
  </ul></p>

## <li>Instrukcja Obsługi Aplikacji</li>
## <li>Podsumowanie</li>

</ol>
