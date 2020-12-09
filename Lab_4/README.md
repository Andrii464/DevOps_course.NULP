# Lab_4: Робота з Docker.

+ Інсталював Docker.
+ Ознайомився з офіційною документацією по Docker.
+ Перевірив чи докер встановлений і  чи працює правильно, запустив перевірку версії, вивів допомогу та тестовий імедж:
```
docker -v
docker -h
sudo docker run docker/whalesay cowsay Docker is fun

```
Результати виконання команд перенаправляю у файл my_work.log та роблю коміт його до репозиторію. Для цього використовую оператори перенаправлення потоку виводу> i >>.

+ Ознайомився з документацією `Dockerfile`, який описує контент імеджу.
+ Створюю імедж із Django сайтом зробленим у попередній роботі: 
  - Використoвую команди, щоб завантажити базовий імедж з репозиторію:
    ```
    sudo docker pull python:3.6-slim
    sudo docker images
    	REPOSITORY          TAG                 IMAGE ID            CREATED             SIZE
    	python              3.6-slim            29b8dbd5cf2f        5 days ago          111MB
    	docker/whalesay     latest              6b362a9f73eb        5 years ago         247MB
    sudo docker inspect python:3.6-slim
    ```

   - Створюю файл з іменем `Dockerfile` та копіюю туди вміст  файлу з репозиторію.
   - Ознайомлююся із коментарями, щоб зрозуміти структуру написання `Dockerfile`.
   - Замінюю посилання на власний Git репозиторій із моїм веб-сайтом та комічу даний `Dockerfile`.

