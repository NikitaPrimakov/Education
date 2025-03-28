# Глава 1. Страницы руководств man


## Команда man $команда

Вы можете ввести команду man с последующим именем интересующей команды (для которой вам хотелось бы получить справочную информацию) и начать чтение страницы руководства. Нажмите q для выхода из режима чтения страницы руководства. Некоторые страницы руководств содержат примеры (расположенные ближе к концу страницы).

```
paul@laika:~$ man whois
Форматирование страницы whois(1), подождите...
```

## Команда man $имя_файла_конфигурации

Для большинства файлов конфигурации имеются отдельные страницы руководств.

```
paul@laika:~$ man syslog.conf
Форматирование страницы syslog.conf(5), подождите...
```

## Команда man $демон

Также данное утверждение справедливо для большинства демонов (программ, работающих в фоновом режиме) из вашей системы.

```
paul@laika:~$ man syslogd
Форматирование страницы syslogd(8), подождите...
```

## Команда man -k (apropos)

Команда man -k (или apropos) позволяет вывести список страниц руководств, содержащих заданную строку.

```
paul@laika:~$ man -k syslog
lm-syslog-setup (8)  - configure laptop mode to switch syslog.conf ...
logger (1)           - a shell command interface to the syslog(3) ...
syslog-facility (8)  - Setup and remove LOCALx facility for sysklogd
syslog.conf (5)      - syslogd(8) configuration file
syslogd (8)          - Linux system logging utilities.
syslogd-listfiles (8) - list system logfiles
```

## Команда whatis

Для ознакомления с описанием страницы руководства следует использовать команду whatis с именем интересующей страницы руководства.

```
paul@u810:~$ whatis route
route (8)            - show / manipulate the IP routing table
```

## Команда whereis

Расположение файла страницы руководства в рамках файловой системы может быть определено с помощью команды whereis.

```
paul@laika:~$ whereis -m whois
whois: /usr/share/man/man1/whois.1.gz
```

Этот файл может быть непосредственно прочитан с помощью команды man.

```
paul@laika:~$ man /usr/share/man/man1/whois.1.gz
```

## Номера справочных разделов

Вы, скорее всего, обратили внимание на числа в круглых скобках. Выполнив команду man man, вы можете узнать о том, что эти числа являются номерами справочных разделов. Исполняемые файлы и команды оболочки отнесены к первому справочному разделу.

1 Исполняемые программы или команды оболочки (shell)
2 Системные вызовы (функции, предоставляемые ядром)
3 Библиотечные вызовы (функции, предоставляемые программными библиотеками)
4 Специальные файлы (обычно находящиеся в каталоге /dev)
5 Форматы файлов и соглашения, например о /etc/passwd
6 Игры
7 Разное (включает пакеты макросов и соглашения), например man(7), groff(7)
8 Команды администрирования системы (обычно, запускаемые только суперпользователем)
9 Процедуры ядра [нестандартный раздел]

## Команда man разделфайл

Таким образом, при обращении к странице руководства для команды passwd, вы можете обнаружить, что эта страница обозначается как passwd(1); при обращении к странице руководства для файла passwd используется обозначение passwd(5). Приведенные ниже примеры команд иллюстрируют методику открытия страниц руководств из корректных разделов.

```
[paul@RHEL52 ~]$ man passwd      # открывает первую найденную страницу руководства
[paul@RHEL52 ~]$ man 5 passwd    # открывает страницу руководства из раздела 5
```

## Команда man man

Если вы желаете узнать больше о команде man, прочитайте это замечательное руководство (Read The Fantastic Manual - RTFM).

К сожалению, на страницах руководств невозможно найти ответы на все вопросы...

```
paul@laika:~$ man woman
Нет справочной страницы для woman
```

## Утилита mandb

Если вы убеждены в том, что страница руководства существует, но при этом вы не можете получить доступ к ней, попробуйте выполнить команду mandb в дистрибутиве Debian/Mint.

```
root@laika:~# mandb
В 0 man-подкаталогах содержатся более новые справочные страницы. 
Добавлено 0 справочных страниц. 
Добавлено 0 побочных cat-страниц. 
Вычищено 0 старых записей базы данных.
```

Или команду makewhatis в дистрибутиве CentOS/Redhat.

```
[root@centos65 ~]# apropos scsi
scsi: ничего подходящего не найдено.
[root@centos65 ~]# makewhatis 
[root@centos65 ~]# apropos scsi
hpsa       (4)  - HP Smart Array SCSI driver
lsscsi     (8)  - list SCSI devices (or hosts) and their attributes
sd         (4)  - Driver for SCSI Disk Drives
st         (4)  - SCSI tape device
```

# Глава 2. Работа с директориями

## Команда pwd

С помощью команды pwd (расшифровывается как Print Working Directory - вывести информацию о рабочей директории) может быть получена информация о вашем текущем местонахождении в рамках файловой системы. Попробуйте выполнить эту команду: получите доступ к интерфейсу командной строки системы (воспользовавшись одним из приложений со следующими названиями: terminal, console или xterm) и введите команду pwd. Командная оболочка выведет путь к вашей текущей директории.

```
paul@debian8:~$ pwd
/home/paul
```

## Команда cd

Вы можете изменить вашу текущую директорию с помощью команды cd (расшифровывается как Change Directory - изменить директорию).

```
paul@debian8$ cd /etc
paul@debian8$ pwd
/etc
paul@debian8$ cd /bin
paul@debian8$ pwd
/bin
paul@debian8$ cd /home/paul/
paul@debian8$ pwd
/home/paul
```

Команда ```cd ~```

Команда ```cd``` также может использоваться для быстрого перехода назад в вашу домашнюю директорию. Простое исполнение команды cd без задания пути к целевой директории приведет к перемещению в домашнюю директорию. Исполнение команды ```cd ~``` приведет к аналогичному эффекту.

```
paul@debian8$ cd /etc
paul@debian8$ pwd
/etc
paul@debian8$ cd
paul@debian8$ pwd
/home/paul
paul@debian8$ cd ~
paul@debian8$ pwd
/home/paul
```

Команда ```cd ..```

Для перехода в родительскую директорию (ту директорию, которая находится над вашей текущей директорией в дереве директорий) следует использовать команду ```cd ..``` .

```
paul@debian8$ pwd
/usr/share/games
paul@debian8$ cd ..
paul@debian8$ pwd
/usr/share
```

Для того, чтобы остаться в текущей директории, просто введите команду ```cd .```. Позднее мы все же познакомимся с практическим примером использования символа ., представляющего текущую директорию.

Команда ```cd -```

Другой полезный вариант использования команды cd заключается в выполнении простой команды ```cd -``` для перехода в предыдущую директорию.

```
paul@debian8$ pwd
/home/paul
paul@debian8$ cd /etc
paul@debian8$ pwd
/etc
paul@debian8$ cd -
/home/paul
paul@debian8$ cd -
/etc
```

## Абсолютные и относительные пути

Вы должны иметь представление об абсолютных и относительных путях в рамках дерева директорий файловой системы. Если вы вводите путь, начинающийся с символа слэша (/), подразумевается, что путь будет указан относительно корневой директории файловой системы. Если же вы не начинаете ввод пути с символа слэша, подразумевается, что точкой отсчета будет текущая директория.

В примере ниже показано, что текущей директорией является директория /home/paul. Для перехода из этой директории в директорию /home вам придется ввести команду cd /home вместо команды cd home.

```
paul@debian8$ pwd
/home/paul
paul@debian8$ cd home
bash: cd: home: Нет такого файла или каталога
paul@debian8$ cd /home
paul@debian8$ pwd
/home
```

При нахождении в директории /home вам придется ввести команду cd paul вместо команды cd /paul для перехода в поддиректорию paul текущей директории /home.

```
paul@debian8$ pwd
/home
paul@debian8$ cd /paul
bash: cd: /paul: Нет такого файла или каталога
paul@debian8$ cd paul
paul@debian8$ pwd
/home/paul
```

В том же случае, если вашей текущей директорией является корневая директория /, то и команда cd /home, и команда cd home позволят вам переместиться в директорию /home.

```
paul@debian8$ pwd
/
paul@debian8$ cd home
paul@debian8$ pwd
/home
paul@debian8$ cd /
paul@debian8$ cd /home
paul@debian8$ pwd
/home
```

## Утилита ls

Вы можете вывести список содержимого директории с помощью утилиты ls.

```
paul@debian8:~$ ls
allfiles.txt  dmesg.txt  services   stuff  summer.txt
paul@debian8:~$
```

Команда ```ls -a```

Часто используемым параметром утилиты ls является параметр ```-a```, который предназначен для вывода информации обо всех файлах. Под выводом информации обо всех файлах подразумевается вывод информации в том числе и о скрытых файлах. В том случае, если имя файла в рамках файловой системы Linux начинается с символа точки, он считается скрытым файлом и не включается в обычные списки содержимого директорий.

```
paul@debian8:~$ ls
allfiles.txt  dmesg.txt  services  stuff  summer.txt
paul@debian8:~$ ls -a
.   allfiles.txt   .bash_profile  dmesg.txt   .lesshst  stuff
..  .bash_history  .bashrc        services    .ssh      summer.txt 
paul@debian8:~$
```

Команда ```ls -l```

Вам придется многократно использовать параметры утилиты ls для вывода информации о содержимом директории в различных форматах или для вывода информации о различных файлах из директории. Команда ls без параметров позволяет получить список файлов, расположенных в директории. Команда ls -l (в качестве параметра использована строчная буква L, а не число 1) позволяет получить более подробный список файлов.

```
paul@debian8:~$ ls -l
итого 17296
-rw-r--r-- 1 paul paul 17584442 сен 17 00:03 allfiles.txt
-rw-r--r-- 1 paul paul    96650 сен 17 00:03 dmesg.txt
-rw-r--r-- 1 paul paul    19558 сен 17 00:04 services
drwxr-xr-x 2 paul paul     4096 сен 17 00:04 stuff
-rw-r--r-- 1 paul paul        0 сен 17 00:04 summer.txt
```

Команда ```ls -lh```

Другим периодически используемым параметром утилиты ls является параметр -h. Он позволяет выводить числовые значения (соответствующие размерам файлов) в формате, лучше читаемом человеком. Также в примере ниже показаны варианты передачи параметров утилите ls. Позднее в данной книге будут даны подробные пояснения относительно выводимых данных.

Обратите внимание на то, что мы используем строчную букву L, а не число 1 в качестве параметра утилиты в данном примере

```
paul@debian8:~$ ls -l -h
итого 17M
-rw-r--r-- 1 paul paul  17M сен 17 00:03 allfiles.txt
-rw-r--r-- 1 paul paul  95K сен 17 00:03 dmesg.txt
-rw-r--r-- 1 paul paul  20K сен 17 00:04 services
drwxr-xr-x 2 paul paul 4.0K сен 17 00:04 stuff
-rw-r--r-- 1 paul paul    0 сен 17 00:04 summer.txt
paul@debian8:~$ ls -lh
итого 17M
-rw-r--r-- 1 paul paul  17M сен 17 00:03 allfiles.txt
-rw-r--r-- 1 paul paul  95K сен 17 00:03 dmesg.txt
-rw-r--r-- 1 paul paul  20K сен 17 00:04 services
drwxr-xr-x 2 paul paul 4.0K сен 17 00:04 stuff
-rw-r--r-- 1 paul paul    0 сен 17 00:04 summer.txt
paul@debian8:~$ ls -hl
итого 17M
-rw-r--r-- 1 paul paul  17M сен 17 00:03 allfiles.txt
-rw-r--r-- 1 paul paul  95K сен 17 00:03 dmesg.txt
-rw-r--r-- 1 paul paul  20K сен 17 00:04 services
drwxr-xr-x 2 paul paul 4.0K сен 17 00:04 stuff
-rw-r--r-- 1 paul paul    0 сен 17 00:04 summer.txt
paul@debian8:~$ ls -h -l
итого 17M
-rw-r--r-- 1 paul paul  17M сен 17 00:03 allfiles.txt
-rw-r--r-- 1 paul paul  95K сен 17 00:03 dmesg.txt
-rw-r--r-- 1 paul paul  20K сен 17 00:04 services
drwxr-xr-x 2 paul paul 4.0K сен 17 00:04 stuff
-rw-r--r-- 1 paul paul    0 Sep 17 00:04 summer.txt
paul@debian8:~$
```

## Утилита mkdir

Обход дерева директорий файловой системы Unix является интересным занятием, но еще больший интерес представляет создание ваших собственных директорий с помощью утилиты mkdir. Вам придется передавать как минимум один параметр утилите mkdir, а именно, имя новой директории, которая должна быть создана. При этом следует серьезно задумываться перед использованием начального символа / в именах директорий.

```
paul@debian8:~$ mkdir mydir
paul@debian8:~$ cd mydir
paul@debian8:~/mydir$ ls -al
итого 8
drwxr-xr-x  2 paul paul 4096 сен 17 00:07 .
drwxr-xr-x 48 paul paul 4096 сен 17 00:07 ..
paul@debian8:~/mydir$ mkdir stuff
paul@debian8:~/mydir$ mkdir otherstuff
paul@debian8:~/mydir$ ls -l
итого 8
drwxr-xr-x 2 paul paul 4096 сен 17 00:08 otherstuff
drwxr-xr-x 2 paul paul 4096 сен 17 00:08 stuff
paul@debian8:~/mydir$
```

Команда ```mkdir -p```

Исполнение следующей команды закончится неудачей, так как родительской директории для директории threedirsdeep не существует.

```
paul@debian8:~$ mkdir mydir2/mysubdir2/threedirsdeep
mkdir: невозможно создать каталог "mydir2/mysubdir2/threedirsdeep": Нет такого файла или каталога
```

В случае использования параметра -p утилиты mkdir при необходимости будут создаваться родительские директории.

```
paul@debian8:~$ mkdir -p mydir2/mysubdir2/threedirsdeep
paul@debian8:~$ cd mydir2

paul@debian8:~/mydir2$ ls -l
итого 4
drwxr-xr-x 3 paul paul 4096 сен 17 00:11 mysubdir2
paul@debian8:~/mydir2$ cd mysubdir2
paul@debian8:~/mydir2/mysubdir2$ ls -l
итого 4
drwxr-xr-x 2 paul paul 4096 сен 17 00:11 threedirsdeep

paul@debian8:~/mydir2/mysubdir2$ cd threedirsdeep/
paul@debian8:~/mydir2/mysubdir2/threedirsdeep$ pwd
/home/paul/mydir2/mysubdir2/threedirsdeep
```

## Утилита rmdir

В том случае, если директория пуста, вы можете использовать утилиту rmdir для удаления этой директории.


```
paul@debian8:~/mydir$ ls -l
итого 8
drwxr-xr-x 2 paul paul 4096 сен 17 00:08 otherstuff
drwxr-xr-x 2 paul paul 4096 сен 17 00:08 stuff

paul@debian8:~/mydir$ rmdir otherstuff
paul@debian8:~/mydir$ cd ..
paul@debian8:~$ rmdir mydir
rmdir: не удалось удалить "mydir": Каталог не пуст
paul@debian8:~$ rmdir mydir/stuff
paul@debian8:~$ rmdir mydir
paul@debian8:~$
```

Команда ```rmdir -p```

И по аналогии с параметром mkdir -p, вы также можете использовать утилиту rmdir для рекурсивного удаления директорий.

```
paul@debian8:~$ mkdir -p test42/subdir
paul@debian8:~$ rmdir -p test42/subdir
paul@debian8:~$
```

