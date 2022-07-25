from typing import Optional, List

from project.dao.base import BaseDAO
from project.exceptions import ItemNotFound
from project.models import Genre


class GenresService:
    def __init__(self, dao: BaseDAO) -> None:
        self.dao = dao

    def get_item(self, pk: int) -> Genre:
        genre = self.dao.get_by_id(pk)
        if genre:
            return genre
        raise ItemNotFound(f'Genre with pk={pk} not exists.')

    def get_all(self, page: Optional[int] = None) -> List[Genre]:
        return self.dao.get_all(page=page)
