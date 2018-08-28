# Without directly modifying the data structures, create a script in either
# python or javascript that cycles through all the parents and prints to the
# terminal the proper activities for their child's age group. When there are no
# more activities for that parent, print “Curriculum complete!”..
#
# (Make sure your script accounts for any edge cases in the provided data!)

parents = {
    'Henry': {'childName': 'Calvin', 'age': 1},
    'Ada': {'childName': 'Lily', 'age': 4},
    'Emilia': {'childName': 'Petra', 'age': 2},
    'Biff': {'childName': 'Biff Jr', 'age': 3},
    'Milo': {}
}

activities = [
    {
        'age': 1,
        'activity': [
            'Go outside and feel surfaces.',
            'Try singing a song together.',
            'Point and name objects.'
            ]
    },
    {
        'age': 2,
        'activity': [
            'Draw with crayons.',
            'Play with soundmaking toys or instruments.',
            'Look at family pictures together.'
            ]
    },
    {
        'age': 3,
        'activity': [
            'Build with blocks.',
            'Try a simple puzzle.',
            'Read a story together.'
            ]
    }
]


# - Personalize the message output to make it more friendly.
# - Allow users to input new activities & parents before executing the script.

while input('Do you wanna enter a new parent? (y/n)') == 'y':
    newParent = input('Enter a new parent\'s name: ')
    newChild = input(newParent + '\'s child\'s name is: ')
    newAge = int(input(newChild + '\'s age is: '))
    parents[newParent] = {'childName': newChild, 'age': newAge}


while input('Do you wanna enter some more activities? (y/n)') == 'y':
    newActivity = input('Enter some new activity: ')
    actAge = int(input(newActivity + ' is proper for kids at what age? '))
    while not isinstance(actAge, int):
        print ('please enter a valid age!')
        actAge = input(newActivity + ' is proper for kids at what age? ')
    ages = []
    for act in activities:
        ages.append(act['age'])
    if actAge in ages:
        list(filter(lambda activity: activity['age'] == actAge, activities))[0]['activity'].append(newActivity)
    else:
        activities.append({'age': actAge, 'activity': [newActivity]})

for parent in parents.keys():
    print('++++++++++')
    try:
        print('Proper activities for ' + parent + '\'s kid: ')
        for act in list(filter(lambda activity: activity['age'] == parents[parent]['age'], activities))[0]['activity']:
            print(' - ' + act)
    except:
        if (parents[parent].keys()):
            print ('There\'s no proper activity for ' + parent + '\'s kid!')
        else:
            print (parent + ' has no kid!')
        continue
    print('Curriculum complete!')

#  Print one activity at a time per parent and continue cycling through until all parents have recieved all their activities.

print('=============ONE ACTIVITY PER PARENT================')
parentActivities = {}
for parent in parents.keys():
    try:
        actList = (list(filter(lambda activity: activity['age'] == parents[parent]['age'], activities))[0]['activity']).copy()
    except:
        actList = []
    parentActivities[parent] = actList

while len(list(parentActivities)) != 0:
    for parent in list(parentActivities):
        if(len(parentActivities[parent]) != 0):
            print(parent + ' \'s kid can: ' + parentActivities[parent].pop())
        else:
            parentActivities.pop(parent)
            print(parent + '\'s kid\'s curriculum complete!')
    print('++++++++++')

# Want to really shine and show us your chops?  Work in some of these stretch
# goals using any tools or libraries you see fit.
# - Document your creation process with proper git workflow.
