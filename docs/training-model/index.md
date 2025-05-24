---
title: Wybór i implementacja modelu AI
---

## Opis:

Do zadania klasyfikacji tekstu wybrano model BERT (Bidirectional Encoder Representations from Transformers) z biblioteki `transformers`. Jest to model językowy bazujący na architekturze transformera, który umożliwia rozumienie kontekstu słów w sposób dwukierunkowy.

W projekcie wykorzystano wersję modelu z repozytorium `distilbert-base-uncased`, który został załadowany z wykorzystaniem `AutoModelForSequenceClassification`. Liczba klas została automatycznie dostosowana na podstawie unikalnych etykiet w danych.

Implementacja obejmowała:

1. Wczytanie i wstępne przetworzenie danych (czyszczenie, kodowanie etykiet),

2. Inicjalizację modelu z odpowiednią liczbą klas wyjściowych,

3. Konfigurację parametrów treningowych, takich jak liczba epok, batch size, czy strategia logowania i zapisywania modelu,

4. Przeprowadzenie treningu z użyciem `Trainer`, który automatycznie obsługuje ewaluację, zapis modelu i tokenizatora.

## Oczekiwany wynik:

Zbudowany i przetestowany model klasyfikujący dane tekstowe, gotowy do oceny na zbiorze testowym. Model oraz tokenizer są zapisane na dysku w formacie kompatybilnym z Hugging Face Transformers i gotowe do użycia w środowisku produkcyjnym.
