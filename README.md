# challenge-robart

## How to Run
```
python src/main.py <user_name>
```

## How to use class
```python
# initalize
manager = RepoManager()

# specify user name, and filter options like min watcher language
# default min watchers is 1 and if no language is specified all repos are returned
user_repos = manager.get_repositories(
    user_name=user_name,
    watchers=2,
    language='Python'
)

# pass in list of Repo Objects and specify how to sort
# using 1 or more SortType Enums
user_repos = RepoManager.sort_repos_by(
    repo_list=user_repos,
    sort_types=[SortType.created_at, SortType.size]
)
```
