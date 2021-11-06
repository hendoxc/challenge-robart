from pydantic import BaseModel
import datetime as dt
from typing import Optional


class RepoOwner(BaseModel):

    login: str
    html_url: str


class Repo(BaseModel):

    owner: RepoOwner
    name: str
    html_url: str
    watchers: int
    language: Optional[str] = None
    forks: int
    size: int
    pushed_at: dt.datetime
    created_at: dt.datetime
    updated_at: dt.datetime
