---
title: Wdrożenie modelu i monitorowanie
---

## Opis:

Model AI został przeniesiony do środowiska produkcyjnego w sposób umożliwiający jego łatwe użycie i skalowalność. Wdrożenie objęło kilka kluczowych kroków:

1. Publikacja modelu na Hugging Face Hub – umożliwia zdalny dostęp do wersji modelu poprzez interfejs API oraz łatwe pobieranie przy użyciu transformers.

2. Stworzenie i opublikowanie paczki Python (pypi) – paczka zawiera niezbędny kod do ładowania modelu, preprocessingu i generowania predykcji. Dzięki temu możliwa jest łatwa integracja modelu z różnymi komponentami systemu.

3. Backend (REST API) został zaimplementowany z wykorzystaniem tej paczki, co pozwala na udostępnienie funkcji predykcyjnych w formie usług sieciowych.

4. Frontend umożliwia użytkownikowi końcowemu interakcję z modelem — przesyłanie CV i otrzymywanie wyniku klasyfikacji.

W ramach wdrożenia przewidziano również podstawowe mechanizmy monitorowania, takie jak:

* logowanie zapytań i odpowiedzi po stronie backendu,
* wersjonowanie modelu,
* możliwość przełączania się na inne wersje,
* zbieranie statystyk użycia (np. liczba zapytań, czas odpowiedzi).

## Oczekiwany wynik:

Zintegrowany system AI uruchomiony w środowisku produkcyjnym, dostępny dla użytkowników przez interfejs frontendowy. Model działa jako część większego ekosystemu (frontend + backend + biblioteka + Hugging Face), a jego wydajność i poprawność mogą być monitorowane oraz rozwijane w kolejnych iteracjach.
