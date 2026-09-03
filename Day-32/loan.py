#1.Design a Loan Approval System Using Credit Score, Income, and Existing Liabilities 
'''
credit_score=int(input())
monthly_income=int(input())
existing_liabilities =int(input())
if credit_score>=750 and monthly_income>=50000 and existing_liabilities<=20000:
    print("Approved")
elif 650<=credit_score <=749 and monthly_income>=50000 and existing_liabilities<=20000:
    print("Approved with Conditions ")
else:
    print("Rejected")
    '''
#2. Build an Employee Bonus Calculator Based on Performance Rating, Experience, and Attendance 
salary =int(input())
performance_rating = int(input())
experience = int(input())
attendance=int(input())

if performance_rating == 5:
    perf = salary * 0.25
elif performance_rating == 4:
    perf = salary * 0.15
elif performance_rating == 3:
    perf = salary * 0.10
else:
    perf = 0

if experience > 10:
    exp = salary * 0.10
elif experience >= 5:
    exp = salary * 0.05
else:
    exp = 0


if attendance >= 95:
    att = 5000
elif attendance >= 85:
    att = 2000
else:
    att = 0

total_bonus = perf + exp + att

print(float(total_bonus))