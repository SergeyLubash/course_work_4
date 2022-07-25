from typing import Optional, List

from project.dao import MovieDAO
from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.models import Movie


class MoviesService:
    def __init__(self, dao: MovieDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Movie:
        movie = self.dao.get_by_id(pk)
        if movie:
            return movie
        raise ItemNotFound(f'Movie with pk={pk} not exists.')

    def get_all(self, filter = None, page: Optional[int] = None) -> List[Movie]:
        return self.dao.get_all_order_by(page=page, filter=filter)

