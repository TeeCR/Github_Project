import base64
import hashlib
from datetime import datetime
from hashlib import sha1, sha256
from pydoc_data.topics import topics
from github import Github, Repository
from prettytable import PrettyTable

from github.Commit import Commit
from github.Tag import Tag

# username = "TeeCR"
# g = Github("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")
# url = f"https://api.github.com/users/{username}"
# g=Github()
# user = g.get_user(username)

g = Github("TeeCR")
g = Github("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")

table = PrettyTable()
table.field_names = ["Number", "Repository Name", "Private", "Public","Created Date","Language","Stargazers","topics"]

#github generated access token
access_token = "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"

#login with access token
login = Github(access_token)

#get the user
user = login.get_user()

#get all repositories
my_repos = user.get_repos()

current_date_time = datetime.now()

number = 0

for repository in my_repos:
    number = number + 1
    name = repository.name
    private,public = repository.private, not(repository.private)
    created_date = repository.created_at
    language = repository.language
    stargazers = repository.stargazers_count
    get_topics = repository.get_topics()

#     i = 5
# for commit in commitresponse:
# 	commit.update()
# 	print(commit.last_modified)
# 	i -= 1
# 	if i < 0:
# 		break


    table.add_row([number, name, private, public, created_date, language, stargazers, get_topics])

print(table)


with open("/Users/tahsin.hussain/downloads/output.csv", "w", newline='') as f_output: 
        f_output.write(table.get_csv_string())


# def AllCommits(commits):
#         for repository in my_repos:
#                 master = repository.get_branch("master")
#                 sha_com = master.commit
#                 commits = repository.get_commit(sha=sha_com.sha)
#         return commits