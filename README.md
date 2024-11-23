# Проект BankOperationsProject


## Описание:

Проект BankOperationsProject - это веб-приложение на Python для фильтрации и сортировки списков транзакций с идентификационными данными.
Модуль GENERATORS позволяет фильтровать данные по операциям в зависимости от валюты, выводить описание операций. 
Генератор в модуле GENERATORS генерирует номера банковских карт.
Декоратор log в модуле DECORATORS автоматически регистрирует детали выполнения функций.
В модуле external_api происходит конвертирование данных по валютам с использованием API.
В модуле utils подсчитывается сумма транзакций, находящихся в фале operations.json
Модуль csv_pandas реализовывает чтение табличных данных из файлов csv и excel.
Модуль with_re выполнчет поиск транзакций по определённому слову и подсчёт транзакций по категориям.




## Установка:

1. Клонируйте репозиторий:

```
git@github.com:Daria149/BankOperationsProject.git
```

2. Установите зависимости:

```
pip install -r requirements.txt
```

## Использование:
1. Откройте приложение в вашем веб-браузере.
2. В модуле GENERATORS находятся первоначальные данные по банковским операциям.
2. При необходимости введите новую информацию с идентификационными данными, включающими id, state(статус идентификации), date(дату и время идентификации).
3. Запустите проект.


## Тестирование:
Проект содержит блок с тестами для проверки кода из главных модулей. 
При необходимости можно запустить выполнение тестов.


## Документация:
Для получения дополнительной информации обратитесь к файлу README.md.