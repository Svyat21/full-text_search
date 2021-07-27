### Полнотекстовый поиск с индексацией в Elasticsearch 
#### Проект написан на фреймворке Flask
# 
#### Развертывание приложения
- [скачайте и установите Elasticsearch](https://www.elastic.co/guide/en/elasticsearch/reference/current/install-elasticsearch.html)


- создайте виртуальное окружение и установите необходимые библиотеки из файла requirements.txt

```pip install -r requirements.txt```

- откройте python console в директории ```full-text_search``` и проиндексируйте базу

```
>>> from app.models import Document
>>> Document.reindex()
```

#### Запуск приложения

```flask run```