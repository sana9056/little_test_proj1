Задача№1
Выполнение реализовано в файле Apple_list.py
Для наглядности решил добавить несколько лишних printов.


Задача№2
Выполнение реализовано в файле Animals.py
Немного не понял зачем было отдельно делать функцию для издаваемых звуков.
Если потом надо вызывать полную информацию. Вызов которой так же можно реализовать через функцию.
В целом получилось так.


Задача№3
Для задачи №3 я по случайности начал писать код под unittest.
По этому есть файл orig_unit.py (Где тест заточен под unittest и запускался из под IDE PYCHARM)
Когда закончил работу с ним, то понял что накосячил, и начал проработку дальше.
Тут уже второй файл orig_pytest.py Скрипт теста был поправлен к стандарту pytest через unittest2pytest.
А после доработан до рабочего варианта. Запускать orig_pytest.py необходимо через "pytest -s main.py" Чтобы выводилось 
нужное в задании сообщение. 
