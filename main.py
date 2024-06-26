import requests
import time
import random

def get_solved_problem(users):
    touched_problem =set()
    for handle in users:
        url = f"https://codeforces.com/api/user.status?handle={handle}"
        response = requests.get(url)
        if response.status_code == 200:
            data = response.json()['result']
            for problemset in data:
                if 'contestId' in problemset['problem']:
                    contestId = problemset['problem']['contestId']
                    index = problemset['problem']['index']
                    touched_problem.add((contestId,index))
            print(f"fetched Data {handle} : {len(touched_problem)}")
        else:
            print(f"Not Fetched for {handle} ")
        time.sleep(10)
    return touched_problem

def get_unique_problem(ratings,user_solved_problem):
    url = "https://codeforces.com/api/problemset.problems"
    response = requests.get(url)
    dict={}
    if response.status_code == 200 :
        data = response.json()['result']['problems']
        for problemset in data:
            if "rating" in problemset:
                if problemset['rating'] in ratings:
                    problem = (problemset['contestId'],problemset['index'])
                    if problem not in user_solved_problem:
                        if problemset['rating'] not in dict:
                            dict[problemset['rating']]=[]        
                        dict[problemset['rating']].append(problem)
    time.sleep(10)
    return dict

def get_users():
    users=[]
    with open('users.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            users.append(line.strip())
    return users

def get_problem_criteria():
    list=[]
    with open('ratings.txt', 'r') as file:
        lines = file.readlines()
        for line in lines:
            list.append(tuple(line.strip().split()))
    return list

def get_problem_set(problemset,problem_criteria):
    problems=[]
    for rating,number in problem_criteria:
        for i in range(0,int(number)):
            prob = random.choice(problemset[int(rating)])
            problems.append(prob)
            problemset[int(rating)].remove(prob)
    # Open the file in write mode
    with open('contest_problemset.txt', 'w') as file:
        for contestId,index in problems:
            file.write(f"https://codeforces.com/contest/{contestId}/problem/{index}\n")
    print("Problemset Generated")

def get_ratings_list(problem_criteria):
    rating_list = []
    for rating,number in problem_criteria:
        rating_list.append(int(rating))
    return rating_list

# user_solved_problem = get_touched_problem(["ShazidMashrafi"])
# ratings_800 = get_rated_problem([800,900,1000,1100,1200],user_solved_problem)
users = get_users()
problem_criteria = get_problem_criteria() 
user_solved_problem = get_solved_problem(users)
ratings = get_ratings_list(problem_criteria)
unique_problem = get_unique_problem(ratings,user_solved_problem)
get_problem_set(unique_problem,problem_criteria)

    

