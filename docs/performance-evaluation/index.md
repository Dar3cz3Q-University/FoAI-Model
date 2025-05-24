---
title: Ocena wyników modelu i optymalizacja
---

## Opis:

Model został oceniony na podstawie zestawu danych testowych przygotowanego w fazie wstępnego przetwarzania. Ewaluacja odbywa się automatycznie po każdej epoce treningu (eval_strategy="epoch"), co umożliwia monitorowanie jakości modelu w czasie.

Do oceny modelu można wykorzystać metryki takie jak:

* accuracy (dokładność) – podstawowa metryka klasyfikacyjna,
* F1-score – w przypadku niezbalansowanych klas,

oraz analiza błędów (np. poprzez macierz pomyłek).

W kodzie przewidziano również możliwość logowania wyników co logging_steps=10 oraz zapis modelu z każdej epoki, co umożliwia łatwe cofnięcie się do najlepszego checkpointa.

Optymalizacja może być prowadzona przez:

* zmianę liczby epok (np. 2–5),
* dostosowanie learning rate,
* zmianę rozmiaru batcha,
* wzbogacenie preprocessing'u (np. zaawansowane czyszczenie, balansowanie klas).

## Oczekiwany wynik:

Model osiągający zadowalające wyniki na zbiorze testowym, zoptymalizowany pod kątem wybranych metryk. Gotowy do integracji z systemem produkcyjnym.
