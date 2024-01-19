from github import Github
import csv
# 创建 Github 对象，需要提供个人访问令牌
g = Github("填写token")

# 获取当前用户
user = g.get_user('mtdykly')
repos=[]
data=[]
for following in user.get_following():
    # print(following)
    print(f"Follower: {following.login}")
    username=following
# 列出当前用户的所有仓库
    for repo in following.get_repos():
        print(repo.name)
        repos.append(repo)
    data.append([username,repos])

with open('following_repos.csv','w',newline='',encoding='utf-8')as csv_file:
    csv_writer=csv.writer(csv_file)
    csv_writer.writerow(['关注者','仓库'])
    csv_writer.writerows(data)

print("成功")

