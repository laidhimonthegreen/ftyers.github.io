

ПРИЛОЖЕНИЯ:
- алгоритм maxmatch -- файл maxmatch.py (включает в себя комментарии)
- сравниваемые последовательности из ста предложений -- ideal100 (эталон) и maxmatch100 (предложения, токенизированные с помощью алгоритма)
- результаты сравнения -- wer.txt (список значений WER для каждой пары предложений и среднее арифметическое данных значений)

Среднее арифметическое значений WER для 100 предложений составило приблизительно 0.12. Таким образом, несмотря на то, что алгоритм иногда допускает ошибки (как правило, дробит слова на слова единичной длины), он работает достаточно эффективно.

Пример:
Эталон: 『 三十五 人 の 小学生 』 など の 作品 を 収録 し て いる 。
Работа алгоритма: 『 三十五 人 の 小学生 』 な ど の 作品 を 収録 し て い る 。
Можно заметить, что слова など и いる были разбиты алгоритмом. 