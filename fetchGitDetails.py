import pygithub3
import operator
from pygithub3.services.repos.commits import Commits

gh = pygithub3.Github()

class my_dictionary(dict):

    # __init__ function
    def __init__(self):
        self = dict()

        # Function to add key:value

    def add(self, key, value):
        self[key] = value


def fetch_committees(list_of_repos, org_name, n, m):
    commits_instance = Commits()
    final_ans = my_dictionary()
    for repo in list_of_repos.keys():
        print 'the repo is: ' + repo
        commits = commits_instance.list(user=str(org_name), repo=str(repo), sha='master')
        user_commit_count_map = my_dictionary()
        for page in commits.iterator():
            print 'user is: ' + page.author
            if str(page.author.login) in user_commit_count_map.keys():
                user_commit_count_map[str(page.author.login)] += 1
            else:
                user_commit_count_map.add(str(page.author.login), 1)
        print 'list of commits per repo: ' + user_commit_count_map
        sorted_commits = sorted(user_commit_count_map.items(), key=operator.itemgetter(1), reverse=True)
        top_sorted_commits = dict(sorted_commits[0:m])
        print 'top sorted users: ' + top_sorted_commits
        final_ans.add(repo, top_sorted_commits)
        print 'adding to the final : ' + final_ans

    print final_ans
    return final_ans


def fetch_top_n_repos(organization, n, m):
    all_repos = gh.repos.list(user=organization).all()
    list_of_repo = my_dictionary()
    for repo in all_repos:
        list_of_repo.add(str(repo.name), repo.forks)

    sorted_list_of_repo = sorted(list_of_repo.items(), key=operator.itemgetter(1), reverse=True)
    print sorted_list_of_repo
    return dict(sorted_list_of_repo[0:n])

def main():

    org_name = raw_input("Enter the organization name: ")
    num_of_repos = int(raw_input("ENter the no of repos"))
    num_of_committees = int(raw_input("Enter the no of committees"))

    # To get n most popular repos of an Org based on the forks
    list_of_repos = fetch_top_n_repos(org_name, num_of_repos, num_of_committees)

    # To get top m committees and their commit count
    fetch_results = fetch_committees(list_of_repos, org_name, num_of_repos, num_of_committees)

    print fetch_results

main()