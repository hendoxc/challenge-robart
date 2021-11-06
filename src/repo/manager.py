import requests
from model.repo import Repo
from model.sortmethod import SortType
from typing import Callable, List, Optional


class RepoManager:

    def __init__(self) -> None:

        self.url = 'https://api.github.com'

    def get_repositories(
        self,
        user_name: str,
        watchers: int = 1,
        language: Optional[str] = None
    ) -> List[Repo]:

        response = requests.get(self.url + f'/users/{user_name}/repos').json()

        repo_list = filter(self._filter_by_watcher(watchers), [
                           Repo(**data) for data in response])

        if language:
            repo_list = filter(self._filter_by_language(language), repo_list)

        return list(repo_list)

    @staticmethod
    def sort_repos_by(
        repo_list: List[Repo],
        sort_types: List[SortType]
    ) -> List[Repo]:

        def sort_func(repo: Repo):

            rdict = repo.dict()
            valid_keys = set([s.value for s in sort_types])

            repo_attr = tuple([
                val for key, val in rdict.items()
                if key in valid_keys
            ])

            return repo_attr

        repo_sorted = sorted(repo_list, key=sort_func)

        return repo_sorted

    def _filter_by_watcher(self, min_watchers: int) -> Callable:

        def filter_repo(repo: Repo):

            if repo.watchers < min_watchers:
                return False

            return True

        return filter_repo

    def _filter_by_language(self, language: str) -> Callable:

        def filter_repo(repo: Repo):

            if repo.language != language:
                return False

            return True

        return filter_repo

    @ staticmethod
    def _sort_method(sort_type: SortType) -> Callable:

        mapping = {
            SortType.size: lambda r: r.size,
            SortType.created_at: lambda r: r.created_at,
            SortType.pushed_at: lambda r: r.pushed_at,
            SortType.updated_at: lambda r: r.updated_at
        }

        return mapping[sort_type]
