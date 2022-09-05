Код репозитория основан на [ironpython-stubs](https://github.com/gtalarico/ironpython-stubs).
Выражаю [gtalarico](https://github.com/gtalarico) бесконечную благодарность за вклад в развитие сообщества разработчиков, скриптов и плагинов для инженерных программ.
Я не стал делать форк его репозитория, потому что хочу внести координальные изменения,
к тому же, автор уже давно им не занимается, а преемник так и не был найден.

Так же как и в базовом репозитории, "заглушки" могут быть использованы в различных текстовых редакторах, но все примеры будут рассматриваться в [visual studio code](https://code.visualstudio.com/).

На самом деле сгенерированный код нельзя называть "заглушками", но данное название уже прижилось в сообществе. Если хотите узнать про настоящие заглушки для python кода, то почитайте [тут](https://mypy.readthedocs.io/en/stable/stubs.html).

## Для пользователей
Сгенерированные заглушки ищите в [релизах](https://github.com/BIMOpenGroup/revitapistubs/releases).
Как вы можете заметить, они разделены на `common` и `revit`.  
В `common` хранятся заглушки системных библиотек Windows, пакеты IronPython, [Dynamo](https://github.com/DynamoDS) и [RPS](https://github.com/architecture-building-systems/revitpythonshell).  
В `revit` хранятся заглушки для нескольких версий библиотек `Revit API`.  
Чтобы не было конфликтов у анализатора кода, подключать заглушки надо с помощью двух путей.
```json
// %APPDATA%\Code\User\settings.json
"python.analysis.extraPaths": [
    "ВАШ_ПУТЬ\\stubs\\common",
    "ВАШ_ПУТЬ\\stubs\\revit\\2019"
],
```

При изменении версии Revit для конкретного проекта, придётся повторить оба пути.
```json
// .vscode/settings.json
"python.analysis.extraPaths": [
    "ВАШ_ПУТЬ\\stubs\\common",
    "ВАШ_ПУТЬ\\stubs\\revit\\2021"
],
```

Подробнее о подключении доп модулей читайте [тут](https://code.visualstudio.com/docs/python/editing).  
Примеры использования заглушек смотрите [тут](https://github.com/BIMOpenGroup/RevitAPIStubs/tree/master/examples).  

Чтобы заглушки были максимально эффективными, их надо допиливать руками, но об этом подробнее в примерах.  
Надеюсь, в будущем это будет исправлено.
Если выйдет новая версия Revit API, но при этом код генерации не изменится, то будет обновлён архив последнего релиза.  

## Для котрибьюторов
Любая помощь приветствуется!  
Пишите вопросы, предложения, замечания. Даже если я не смогу что-то поправить вовремя, то возможно кто-то из сообщества поможет.

### Общая информация
Генерация заглушек возможна через консоль, и это выглядит предпочтительным и гибким вариантом, но для простоты я выбрал [RevitPythonShell](https://github.com/architecture-building-systems/revitpythonshell).
Например, не надо заботиться о дополнительных зависимостях для `RevitAPIUI` или требовать пути для генерации,
просто открываем нужный нам Revit и запускаем скрипт.
К тому же, данный репозиторий создан для генерации заглушек только для Revit.

Из-за того что `Pylance` достаточно производительный в отличие от `Jedi` заглушки больше не нужно "минимизировать".
Поэтому раньше требовалось запускать скрипт для обработки сгенерированных заглушек и формирования `stubs.min`.

Решил разместить заглушки в релизах, потому что нет смысла хранить их в репозитории.
Единственная причина хранения их в репозитории - если кто-то будет их обновлять/исправлять руками. Но это очень большой и ненужный труд. Лучше попробовать улучшить генератор.

### Как генерировать заглушки
В оболочке RPS запускаем `src/main.py`, изменив при этом путь к `src_dir`.   
Если запускать через кастомную кнопку на панели RPS, то в коде ничего менять не надо.  
Заглушки сгенерируются в корне репозитория.

### Правила
Как и практически в любом опенсорсе тут принята система [Forking Workflow](https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow).  
Тезисно:
- Делаем форк репозитория;
- Создаём ветку от `master`;
- Делаем `pull request` в `upstream/master`.

Правила именования веток:
- Стиль kebab-case;
- Первым словом идёт задача fix/feature/refactor и т.д. Последующими - краткое описание, либо номер issue.  
    fix-iss57 / feature-iss14 / refactor-generator.

Просьба добавить папки различных IDE в свой глобальный gitignore.

### Текущие задачи
На данный момент приоритетной задачей является улучшение кода генератора.

---

The repository code is based on [ironpython-stubs](https://github.com/gtalarico/ironpython-stubs).
I express my infinite gratitude to [gtalarico](https://github.com/gtalarico) for contributing to the development of the community of developers, scripts and plug-ins for engineering programs.
I did not fork his repository, because I want to make cardinal changes,
besides, the author has not been engaged in it for a long time, and a successor has not been found.

Just like in the base repository, "stubs" can be used in various text editors, but all examples will be covered in [visual studio code](https://code.visualstudio.com/).

In fact, the generated code cannot be called "stubs", but this name has already taken root in the community. If you want to learn about real stubs for python code, then read [here](https://mypy.readthedocs.io/en/stable/stubs.html).

## For users
Look for generated stubs in [releases](https://github.com/BIMOpenGroup/revitapistubs/releases).
As you can see, they are divided into `common` and `revit`.
`common` stores Windows system library stubs, IronPython packages, [Dynamo](https://github.com/DynamoDS) and [RPS](https://github.com/architecture-building-systems/revitpythonshell).
`revit` stores stubs for several versions of the `Revit API` libraries.
To avoid conflicts with the code analyzer, you need to connect stubs using two ways.
```json
// %APPDATA%\Code\User\settings.json
"python.analysis.extraPaths": [
    "YOUR_PATH\\stubs\\common",
    "YOUR_WAY\\stubs\\revit\\2019"
],
```

If you change the version of Revit for a particular project, you will have to repeat both paths.
```json
// .vscode/settings.json
"python.analysis.extraPaths": [
    "YOUR_PATH\\stubs\\common",
    "YOUR_WAY\\stubs\\revit\\2021"
],
```

Read more about connecting additional modules [here](https://code.visualstudio.com/docs/python/editing).
See examples of using stubs [here](https://github.com/BIMOpenGroup/RevitAPIStubs/tree/master/examples).

In order for the stubs to be as effective as possible, they must be finished by hand, but more on this in the examples.
Hopefully this will be fixed in the future.
If a new version of the Revit API is released, but the generation code does not change, then the archive of the latest release will be updated.

## For contributors
Any help is welcome!
Write questions, suggestions, comments. Even if I can't fix something in time, maybe someone from the community can help.

### General information
Stubs generation is possible via the console and this seems to be the preferred and flexible option, but for simplicity I chose [RevitPythonShell](https://github.com/architecture-building-systems/revitpythonshell).
For example, no need to take care of additional dependencies for `RevitAPIUI` or require a path to generate,
just open the Revit we need and run the script.
In addition, this repository is designed to generate stubs for Revit only.

Because `Pylance` is quite performant, unlike `Jedi`, stubs no longer need to be "minimized".
Therefore, it used to be necessary to run a script to process the generated stubs and form `stubs.min`.

I decided to place stubs in releases, because it makes no sense to store them in a repository.
The only reason to keep them in the repository is if someone will update/fix them by hand. But this is a very big and unnecessary work. It is better to try to improve the generator.

### How to generate stubs
In the RPS shell, run `src/main.py`, changing the path to `src_dir`.
If you run through a custom button on the RPS panel, then you don’t need to change anything in the code.
The stubs will be generated at the root of the repository.

### Rules
As in almost any open source, the [Forking Workflow] system is adopted here (https://www.atlassian.com/git/tutorials/comparing-workflows/forking-workflow).
Abstract:
- Making a fork of the repository;
- Create a branch from `master`;
- Make a `pull request` in `upstream/master`.

Branch naming rules:
- Kebab-case style;
- The first word is the fix/feature/refactor task, etc. Subsequent - a brief description, or issue number.
    fix-iss57 / feature-iss14 / refactor-generator.

Please add folders of various IDEs to your global gitignore.

### Current tasks
At the moment, the priority task is to improve the generator code.
