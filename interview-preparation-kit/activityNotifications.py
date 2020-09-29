def activityNotifications(expenditure, d):
    n = len(expenditure)    #size of expenditure array
    median = 0
    notif = 0   #notifications

    for i in range(d,n):
        days = expenditure[i-d:i]
        days.sort()
        const = int(d/2)
        if d % 2 == 0:
            median = (days[const-1] + days[const])/2
        else:
            median = days[const]
        if expenditure[i] >= 2 * median:
            notif += 1
    return notif

d = 5
expenditure = [2,3,4,2,3,6,8,4,5]

print(activityNotifications(expenditure,d))

#This code did not execute within the time limits for larger arrays as input
#Optimize it
        