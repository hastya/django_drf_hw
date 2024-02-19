<h1> HW1 </h1> 
Новый Django-проект с DRF в настройках проекта.

Созданы следующие модели:

<ins>Пользователь: </ins>
- все поля от обычного пользователя, но авторизацию заменить на email;
- телефон;
- город;
- аватарка.

Модель пользователя разместите в приложении users

<ins>Курс:</ins>
- название,
- превью (картинка),
- описание.

<ins>Урок:</ins>
- название,
- описание,
- превью (картинка),
- ссылка на видео.

Урок и курс - это связанные между собой сущности. Уроки складываются в курс, в одном курсе может быть много уроков. Реализована связь между ними.
Модель курса и урока в отдельном приложении materilas

CRUD для моделей курса и урока. Для реализации CRUD для курса используется Viewsets, а для урока - Generic-классы.

Для работы контроллеров описаны простейшие сериализаторы.
При реализации CRUD для уроков реализованы все необходимые операции (получение списка, получение одной сущности, создание, изменение и удаление).

Реализован эндпоинт для редактирования профиля любого пользователя на основе Generic.

<h1> HW2 </h1> 
Для модели курса добавлено в сериализатор поле вывода количества уроков. Поле реализовано с помощью SerializerMethodField()

Добавлена новая модель в приложение users:
<ins>Платежи:</ins>
- пользователь,
- дата оплаты,
- оплаченный курс или урок,
- сумма оплаты,
- способ оплаты: наличные или перевод на счет.

Поля "пользователь", "оплаченный курс" и "отдельно оплаченный урок" - ссылки на соответствующие модели.

Для сериализатора для модели курса реализовано поле вывода уроков с помощью сериализатора для связанной модели.
Один сериализатор выдает и количество уроков курса и информацию по всем урокам курса одновременно.

Настроена фильтрация для эндпоинта вывода списка платежей с возможностями:
- менять порядок сортировки по дате оплаты,
- фильтровать по курсу или уроку,
- фильтровать по способу оплаты.

Для профиля пользователя сделан вывод истории платежей, через расширение сериализатора для вывода списка платежей.