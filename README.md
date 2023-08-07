# wine-reviews
Code Louisville Data Analysis Exercise


## Overivew

In this exercise we will create a summary of wine reviews by country and write
the data to a CSV file. This exercise is based on the Kaggle Learn Pandas 
exercise 3.

Create a Python program that reads in the `data/winemag-data-130k-v2.csv.zip` 
file. Create a summary of the data that contains the name, number of reviews, 
and the average points for each unique country in the dataset. Write the summary
data to a new file in the `data` folder named `reviews-per-country.csv`.

### Example Output Data

| country | count | points |
| ------- | ----- | ------ |
| US | 54504 | 88.6 |
| France | 22093 | 88.8 |
| Italy | 19540 | 88.6 |
| Spain | 6645 | 87.3 |
| Portugal | 5691 | 88.3 |
| ... | ... | ... |
| Bosnia and Herzegovina | 2 | 86.5 |
| Armenia | 2 | 87.5 |
| Slovakia | 1 | 87.0 |
| China | 1 | 89.0 |
| Egypt | 1 | 84.0 |

### Notes
- The csv file created by your program should be saved in the `data` folder.
- The csv file created by your program should be added, committed and pushed 
to GitHub.
- The column names should match the example above.
- The values in the points column should be rounded to 1 decimal point.


## Instructions
1. Click on the link in the assignment in Google Classroom.
1. Accept the exercise from GitHub. GitHub will automatically create a new repo 
for you with an open Pull Request for your changes.
1. Clone the new repo to your machine.
1. Create a virtual environment, activate it, and install the required packages. 
(see instructions below)
1. Add your code to the specified file.
1. Add/Commit/Push your code back to GitHub.GitHub will run the automated tests 
when you push.
1. Review the Pull Request on your repo to see the status of the tests.
1. “Turn in” the assignment in Google Classroom.

### Virutal Environment Instructions

1. After you have cloned the repo to your machine, navigate to the project 
folder in GitBash/Terminal.
1. Create a virtual environment in the project folder. `python3 -m venv venv` [^1]
1. Activate the virtual environment. `source venv/bin/activate`
1. Install the required packages. `pip install -r requirements.txt`
1. When you are done working on your repo, deactivate the virtual environment. 
`deactivate`

[^1]: GitBash on Windows uses “python” instead of “python3”

### Automated Testing

This repo contains a small testing program that is automatically run by GitHub 
to validate your code. This testing program is contained in the tests.py file. 
You don't have to do anything with this file to complete the exercise, but 
you can follow these steps if you would like to run the tests on your machine.

1. Open GitBash in Windows or the Terminal in Mac and navigate to the project 
folder.
1. Run the tests. We won't be covering testing with python in this course. Use 
the following command to run the tests: `pytest tests.py`. You can read more 
about it [here](https://realpython.com/python-testing/).
1. Review the output from running the test. This will let you know whether your 
code produces the expected results.