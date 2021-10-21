# Тестовые сценарии на странице Yandex

Cкрипт выполняет два тестовых сценария:
#### Поиск в Яндексе
1. Зайти на [yandex.ru](http://yandex.ru)
2. Проверить наличие поля поиска
3. Ввести в поиск Тензор
4. Проверить, что пояилась таблица с подсказками
5. При нажатии Enter появляется таблица результатов поиска
6. В первых 5 результатах есть ссылка на [tensor.ru](https://tensor.ru)

#### Картинки в Яндексе
1. Зайти на [yandex.ru](http://yandex.ru)
2. Ссылка "Картинки" присутствует на странице
3. Кликаем на ссылку
4. Проверить, что перешли на url https://yandex.ru/images/
5. Открыть первую категорию, проверить что открылась, в поиске верный текст
6. Открыть первую картинку, проверить что открылась
7. При нажатии кнопки "вперед" картинка изменяется
8. При нажатии кнопки "назад" картинка изменяется на изображение из шага 6. Необходимо проверить, что это то же изображение.

### Как установить

Python3 должен быть уже установлен. 
Затем используйте `pip` для установки зависимостей:
```
pip install -r requirements.txt
```
Для работы скрипта требуется установить браузер Google Chrome и webdriver Chrome.

[Инструкция для установки webdriver'а](https://selenium-python.com/install-chromedriver-chrome)

Скрипт запускается командой 
```
pytest test_yandex_page.py
``` 
Существует возможность запуска сценариев по отдельности с использованием маркировки.

Для первого сценария:
```
pytest search test_yandex_page.py
```
Для второго сценария:
```
pytest image test_yandex_page.py
```

### Цель проекта

Код написан в качестве выполнения тестового задания.
