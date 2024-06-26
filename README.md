# Problem-Set-Generator-For-Codforces-Gym

This repository contains a problem set generator for Codeforces Gym. It reads user information, desired ratings, and problem counts from specified files, uses the Codeforces API to fetch problems, and generates a problem set for a contest.

## Files

- `users.txt`: Contains the usernames of Codeforces users who will attend the gym contest.
- `ratings.txt`: Contains the desired rating and the desired problem count.
- `main.py`: The main script to generate the problem set.
- `contest_problemset.txt`: The output file where the generated problem set links are stored.

## File Formats

### `users.txt`

Each line should contain a single Codeforces username. Example:

tourist
jiangly
Benq
orzdevinwang


### `ratings.txt`

The file should contain two lines:
1. Desired rating of the problems.
2. Desired number of problems.
(800 rating problems 2, 900 ratings problem 3, 1000 rating problem 2)
Example:

800 2
900 1
1000 2


## How to Use

1. Clone the repository:

## How to Use

1. Clone the repository:

```bash
git clone https://github.com/DividedByyZero/Problem-Set-Generator-For-Codeforces-Gym
cd Problem-Set-Generator-For-Codeforces-Gym
2. Install 
pip install requests
3. Run Main Scripts
python main.py
