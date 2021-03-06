# -*- coding: utf-8 -*-

from github import Github
from datetime import datetime

import json, sys

def json_serial(obj):
  """JSON Serializer for objects not serializable by default json code"""
  if isinstance(obj, datetime):
    return obj.isoformat()
  # raise return obj
  """TypeError("Type not serializable")"""

AUTH_TOKEN = 'PLEASE TYPE YOUR GITHUB API TOKEN'

if len(sys.argv) > 1:
    if sys.argv[1] is not None or sys.argv[1] != '':
        AUTH_TOKEN = sys.argv[1]
else:
    raise SyntaxError('please type your github api token')

user = Github(login_or_token=AUTH_TOKEN)

omg_data = dict()
omg_data['user'] = dict()

github_user = user.get_user()
omg_data['user']['login'] = github_user.login
omg_data['user']['type'] = github_user.type
omg_data['user']['name'] = github_user.name
omg_data['user']['avatar_url'] = github_user.avatar_url
omg_data['user']['company'] = github_user.company
omg_data['user']['blog'] = github_user.blog
omg_data['user']['location'] = github_user.location
omg_data['user']['email'] = github_user.email
omg_data['user']['hireable'] = github_user.hireable is None if False else True
omg_data['user']['following'] = github_user.following
omg_data['user']['followers'] = github_user.followers
omg_data['user']['public_repos'] = github_user.public_repos
omg_data['user']['public_gists'] = github_user.public_gists
omg_data['user']['created_at'] = github_user.created_at
omg_data['user']['updated_at'] = github_user.updated_at
omg_data['user']['url'] = github_user.url


omg_data['repositories'] = []
omg_data['languages'] = []
repos = github_user.get_repos()

for repo in repos:
    repo_data = dict()
    repo_data['name'] = repo.name
    repo_data['full_name'] = repo.full_name
    repo_data['forks_count'] = repo.forks_count
    repo_data['stargazers_count'] = repo.forks_count
    repo_data['watchers_count' ] = repo.watchers_count
    repo_data['language'] = repo.language
    repo_data['fork'] = repo.fork is None if False else True
    repo_data['open_issues_count'] = repo.open_issues_count
    repo_data['url'] = repo.html_url
    omg_data['repositories'].append(repo_data)

    lang_data = dict()
    lang_data['owner'] = repo.owner.login
    lang_data['repo_name'] = repo.name
    lang_data['url'] = repo.html_url
    lang_data['languages'] = []
    for language, line in repo.get_languages().items():
        lang = dict()
        if language is not None and language != '':
            lang['name'] = language
            lang['line'] = line
            lang_data['languages'].append(lang)
    omg_data['languages'].append(lang_data)

print(json.dumps(omg_data, indent=4, default=json_serial))
