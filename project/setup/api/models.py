from flask_restx import fields, Model

from project.setup.api import api

genre: Model = api.model('Жанр', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

director: Model = api.model('Режисер', {
    'id': fields.Integer(required=True, example=1),
    'name': fields.String(required=True, max_length=100, example='Комедия'),
})

movie: Model = api.model('Фильм', {
    'id': fields.Integer(required=True, example=1),
    'title': fields.String(required=True, max_length=100, example='Омерзительная восьмерка'),
    'description': fields.String(required=True, max_length=100, example='США после Гражданской войны. Легендарный охотник за головами Джон Рут по кличке Вешатель конвоирует заключенную. По пути к ним прибиваются еще несколько путешественников. Снежная буря вынуждает компанию искать укрытие в лавке на отшибе, где уже расположилось весьма пестрое общество: генерал конфедератов, мексиканец, ковбой… И один из них - не тот, за кого себя выдает. '),
    'trailer': fields.String(required=True, max_length=100, example='https://www.youtube.com/watch?v=lmB9VWm0okU'),
    'year': fields.Integer(required=True, example=2015),
    'rating': fields.Float(required=True, example=7.8),
    'genre': fields.Nested(genre),
    'director': fields.Nested(director),
})

user: Model = api.model('Пользователь', {
    'id': fields.Integer(required=True, example=1),
    'email': fields.String(required=True, max_length=100, example='serg_l@mail.ru'),
    'password': fields.String(required=True, max_length=100, example='190234'),
    'name': fields.String(required=True, max_length=100, example='Serg'),
    'surname': fields.String(required=True, max_length=100, example='Lubash'),
    'genre': fields.Nested(genre),
})
