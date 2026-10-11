[![Build Status](https://app.travis-ci.com/kpdvstu/PTLab2.svg?branch=master)](https://app.travis-ci.com/kpdvstu/PTLab2)
# Лабораторная 2 по дисциплине "Технологии программирования"

Магазин мягкой мебели (диваны, кресла, пуфы и банкетки, кушетки) на Django + PostgreSQL.

## Функциональность

* каталог товаров с фильтром по категории (`/`, `/?category=<id>`);
* **корзина**: покупатель кладёт товары в корзину (`/cart/`), общая стоимость показывается
  на странице корзины и в шапке каждой страницы;
* в корзине **может быть только один экземпляр одного товара** — это проверяется в коде
  (`Cart.add`) и гарантируется ограничением уникальности `(cart, product)` в БД;
* корзина привязана к сессии, поэтому авторизация покупателю не нужна;
* покупка отдельного товара «сразу» (`/buy/<id>/`) — как в исходной лабораторной;
* модели доступны в админке (`/admin/`).

## Запуск

```
pip install -r requirements.txt
# БД: PostgreSQL, база django_db, пользователь postgres (см. tplab2/settings.py);
# пароль берётся из переменной окружения DATABASE_PASSWORD
python manage.py migrate
python manage.py loaddata products.yaml   # категории и товары
python manage.py runserver
```

## Тесты

```
python manage.py test shop/tests/
```

Для тестов Django сам создаёт и удаляет отдельную базу `test_django_db`, поэтому
у пользователя PostgreSQL должно быть право `CREATEDB`.

Покрытие кода:

```
pip install coverage
coverage run manage.py test shop/tests/
coverage report
```
