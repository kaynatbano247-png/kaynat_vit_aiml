#exam study planner
print("WELCOME TO EXAM STUDY PLANNER, A SMART PLANNER THAT WILL HELP YOU TO PREPARE FOR YOUR EXAMS ")
n=int(input("Enter the number of subjects you have "))
sub=[]
deadl=[]
difflev=[]
for i in range(1,n+1):
    subject=input("Enter the subject name ")
    sub.append(subject)
    deadline=int(input("Enter the number of days left for this subject "))
    deadl.append(deadline)
    difficulty_level=int(input("rate the subject under 1 to 5 based on its difficulty "))
    difflev.append(difficulty_level)
priority_score=[]
for i in range(n):
    if deadl[i]==0:
        prior_score = (difflev[i] * 2) + (1)
    else:
        prior_score=(difflev[i]*2)+(1/deadl[i])
    priority_score.append(prior_score)
dictionary=dict(zip(sub,priority_score))
dictionary=dict(sorted(dictionary.items(), key=lambda item: item[1], reverse=True))
print("your priority subjects are as follow from higher to lower:")
print(dictionary)
a=int(input("click 1 if you want a daily planner else click 2"))
if a==1:
  study_hours=int(input("Enter the available study hours in a day"))
  total_priority = sum(priority_score)
  study_plan={}

  for i in range(n):
    hours = (priority_score[i] / total_priority) * study_hours
    study_plan[sub[i]] = hours
    study_plan = dict(sorted(study_plan.items(), key=lambda x: x[1], reverse=True))

    print("\nSuggested Study Hours per Subject:")
    for subject, hours in study_plan.items():
             print(f"{subject} → {hours:.2f} hours/day")
else:
  rate=int(input(print(" Please rate your experience with this planner from 1 to 5 ")))
  if(1<=rate<=5):
     print("Thank you")
  else:
      print("wrong input")






