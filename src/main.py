from repo.manager import RepoManager
from model.sortmethod import SortType
import sys


def main(user_name: str):

    manager = RepoManager()

    user_repos = manager.get_repositories(user_name=user_name)

    user_repos = RepoManager.sort_repos_by(
        repo_list=user_repos,
        sort_types=[SortType.created_at, SortType.size]
    )

    for r in user_repos:
        print(
            f'{r.html_url}\n\t-> Watchers: {r.watchers}\n'
            f'\t-> Langauge: {r.language}\n\t-> Size: {r.size}\n'
            f'\t-> Created at: {r.created_at}\n'
            f'\t-> Pushed at: {r.pushed_at}\n'
            f'\t-> Updated at: {r.updated_at}\n'
        )

    pass


if __name__ == '__main__':
    main(sys.argv[1])
