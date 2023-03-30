# MiddleDiplomPyton

Приложение хранит заметки в списке словарей notes, каждый из которых представляет одну заметку с идентификатором, заголовком, текстом и датой/временем создания или последнего изменения.
При запуске приложения происходит загрузка заметок из файла notes.json, если таковой существует. Далее приложение ждет ввода команд от пользователя. Доступны следующие команды:

•	list - выводит список всех заметок в консоль.

•	add - добавляет новую заметку с заголовком и текстом, введенными пользователем.

•	edit ID - редактирует заметку с указанным идентификатором, заменяя заголовок и/или текст на новые значения, введенные пользователем.

•	delete ID - удаляет заметку с указанным идентификатором.

•	exit - завершает работу приложения.

После выполнения всех команд список заметок сохраняется в файл notes.json.
Основная логика приложения реализована в функциях load_notes(), save_notes(), list_notes(), add_note(), edit_note_command(), delete_note_command() и find_note_by_id(). При чтении и записи заметок в файл приложение использует модуль json.
