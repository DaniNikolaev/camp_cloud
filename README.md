# Проект: Тестовое задание Сloud.ru Camp

## Описание

Простая программа на Python и Автоматизация тестирования с использованием Playwright. Включает тесты, написанные на Python, а также линтеры для проверки качества кода.

## Установка

Для запуска скриптов и тестов вам необходимо установить следующие инструменты и библиотеки:

### Необходимые инструменты

- [Python](https://www.python.org/downloads/) (версия 3.7 или выше)
- [Git](https://git-scm.com/downloads) (для управления версиями)
- [GitHub CLI](https://cli.github.com/) (для создания репозиториев на GitHub)

### Установка зависимостей

1. Клонируйте репозиторий на ваш локальный компьютер:
   ```bash
   git clone https://github.com/DaniNikolaev/camp_cloud.git
   cd camp_cloud

2. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv venv
   source venv/bin/activate  # Для Linux/Mac
   venv\Scripts\activate  # Для Windows

3. Установите необходимые библиотеки:
   ```bash
   pip install -r requirements.txt

Содержимое requirements.txt:
astroid==3.3.10  
colorama==0.4.6  
dill==0.4.0  
exceptiongroup==1.3.0  
flake8==7.2.0  
greenlet==3.2.2  
iniconfig==2.1.0  
isort==6.0.1  
mccabe==0.7.0  
packaging==25.0  
platformdirs==4.3.8  
playwright==1.52.0  
pluggy==1.6.0  
pycodestyle==2.13.0  
pyee==13.0.0  
pyflakes==3.3.2  
pylint==3.3.7  
pytest==8.3.5  
tomli==2.2.1  
tomlkit==0.13.2  
typing_extensions==4.13.2  

### Запуск тестов
Для запуска тестов выполните следующую команду в терминале:
```bash
pytest
```
### Линтинг кода
Для проверки качества кода с помощью линтеров выполните следующие команды:
#### Flake8
```bash
flake8 .
```
#### Pylint
```bash
pylint .
```
