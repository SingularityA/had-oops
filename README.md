## had-oops

#### Hadoop Tasks (Big Data Course)

##### Task 1

Для полного файла выполнение [job](https://github.com/SingularityA/had-oops/blob/master/job.py) заняло приблизительно 94 с.
```bash
python3 job.py input/wiki.txt -o output/results
```
Здесь тоже 94 с.
```bash
python3 job.py -r hadoop hdfs:///user/kiiru/wiki.txt -o hdfs:///user/kiiru/results
```
Для урезанного файла здесь  ~4 с.
```bash
python3 job.py input/wiki_trunc.txt -o output/results_trunc
```
А здесь - 37 с.
```bash
python3 job.py -r hadoop hdfs:///user/kiiru/wiki_trunc.txt -o hdfs:///user/kiiru/results_trunc
```

Откуда можно сделать вывод, что разворачивать hadoop стоит только для действительно больших данных.

##### Task 2

1.1 Самое длинное слово.
```
63	"codice_16codice_17codice_18codice_19codice_20codice_21codice_22"
```

1.2 Средняя длина слов.
```
Avg	6.056905087028759
```

1.3 Самое частоупотребляемое слово, состоящее из латинских букв.
```
13024	"ru"
```

1.4 Все слова, которые более чем в половине случаев начинаются с большой буквы и встречаются больше 10 раз.
```
...
13	борисоглебский
48	борисом
24	борису
16	борн
11	борна
11	борнео
...
```
