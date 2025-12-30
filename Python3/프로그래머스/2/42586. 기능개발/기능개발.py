import math
def solution(progresses, speeds):
    days = []
    for progress, speed in zip(progresses, speeds):
        day = math.ceil((100-progress) / speed)
        days.append(day)
    
    max_day = days[0]
    count = 0
    answers = []
    
    for day in days:
        if day <= max_day:
            count += 1
        else: 
            answers.append(count)
            max_day = day
            count = 1
        
    answers.append(count)
    return answers

                
                
        