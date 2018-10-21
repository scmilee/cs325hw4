
#standard file reader from all of my previous assignments
unsortedMatrix = [];
with open('./act.txt') as f:
    for line in f:
        numbers_float = map(int, line.split());
        unsortedMatrix.append(numbers_float);
index = 0
activityCounts = []
#this little bit of code just gets the amount of sessions to run the main program and the length of each session
while index <= len(unsortedMatrix) -1:
    tempList = unsortedMatrix[index]
    activityCounts.append(tempList)
    tempVal = unsortedMatrix[index][0]  
    index +=1
    index += tempVal

def greed(sortedArray):
    #initialize the current start time and the choice list
    currentStartTime = 0
    chosenActivities = []
    for activity in sortedArray:
        #set default first choice
        if currentStartTime == 0:
            currentStartTime = activity[1]
            chosenActivities.append(activity[0])
        #compare if the end time of the current activity conflicts with the current starting time
        #if theres no conflict add it to the choices
        elif currentStartTime >= activity[2]:
            currentStartTime = activity[1]
            chosenActivities.append(activity[0])
    #return the choices
    return chosenActivities

for actIndex in range(0, len(activityCounts)):
    #delete the first index as thats just an indicator of how many there are.
    #get the activities from the unsorted matrix indicated by the activity counts
    del unsortedMatrix[0]
    activities = unsortedMatrix[:activityCounts[actIndex][0]]
    #sort them by the 2nd column and then reverse it in order to get a array of activities sorted by 
    #lastest start time first
    sortedActivities = sorted(activities,key=lambda x: x[1])
    sortedActivities.reverse()
    
    output = greed(sortedActivities)
    #standard printing output
    print "Set " + str(actIndex + 1)
    print "Number of activities selected = " + str(len(output))
    string = ''
    for activity in output:
        string += str(activity) + ' '
    print string +"\n"

    #it then removes the existing array from the unsortedMatrix
    del unsortedMatrix[:activityCounts[actIndex][0]]
