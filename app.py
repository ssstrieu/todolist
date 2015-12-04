from datetime import date


#list columns: id,task,duedate,isCompleted, isAlertOn
dummyList=[
[1,'eat food','2015-12-05',True,False]
,[2,'study c#','2015-12-08',False, False]
,[3,'pet cats','2015-12-05',True, True]
,[4,'send emails','2015-12-05',False, True]
]

# dummyList[3][3]=True
# print dummyList[3]

today =date.today()
quitFlag=False



def showMenuOptions():
	print '''
	Type "A" to ADD a new To Do Item.
	Type "C" to CHANGE an existing item.
	Type "L" to show the LIST. 
	'''
	#Type "Q to QUIT the program"
	
def chooseMenuOptions():
	addResponses=['add', 'a', 'new']
	changeResponses=['change','c']
	listResponses=['list','l']
	quitResponses=['q', 'quit', 'exit']
	menuChoice= raw_input('> ')
	if menuChoice.lower() in addResponses:
		print 'Add an item'
		addItemToList()
	elif menuChoice.lower() in changeResponses:
		print 'Change an item'
		changeItem()
	elif menuChoice.lower() in listResponses:
		print 'print a list'
		displayAllListItems(dummyList)
	elif menuChoice.lower() in quitResponses:
		print 'Bye.'
		quitFlag=True
	else:
		print 'Not a menu option.'
		showMenuOptions()


def changeItem():
	displayAllListItems(dummyList)
	itemNumber=int(raw_input("Number of Item you want to change \n >" ))-1
	print '''
	Type "R" to REMOVE the item.
	Type "D" to change the DUE DATE.
	Type "C" to make item as COMPLETE
	Type "A" to toggle ALERTS

	'''
	changeAction=raw_input("> ")
	if changeAction.lower()=="r":
		print 'REMOVED'
		dummyList[itemNumber][3]='Removed'
		print dummyList[itemNumber]
	elif changeAction.lower()=="d":
		newDueDate=raw_input('Enter new due date. (YYYY-MM-DD)')
		dummyList[itemNumber][2]=newDueDate
		print dummyList[itemNumber]
	elif changeAction.lower()=="c":
		dummyList[itemNumber][3]=True
		print dummyList[itemNumber]
	elif changeAction.lower()=="a":
		if dummyList[itemNumber][4]==True:
			dummyList[itemNumber][4]=False
			print dummyList[itemNumber]
		else:
			dummyList[itemNumber][4]=True
			print dummyList[itemNumber]
	else:
		print 'invalid command'	

def addItemToList():
	taskName=raw_input('Enter Task Description: ')
	dueDate=raw_input('Enter Due Date: (YYYY-MM-DD) ')
	dummyList.append([len(dummyList)+1,taskName,dueDate, False, False])
	displayAllListItems(dummyList)


def getCompletionStatus(row):
	#returns completion status of row and formats for display
	if row[3]==True:
		return "Completed"
	else: 
		return "Incomplete"

def getAlertStatus(row):
	#returns completion status of row and formats for display
	if row[3]==True:
		return "Alert On"
	else: 
		return "Alert Off"

def displayAllListItems(list):
	#eventually need to filter current items only
	print "====== To Do List ======" 
	for i in list:
		if i[3]!='Removed':
			print "  Item {0} - {1} - Due: {2} - {3} - {4}". format(i[0],i[1],i[2],getCompletionStatus(i),getAlertStatus(i))
			print '-------------------------------------------------------------------'

def displayIncompleteItems(list):
	print "====== Unfinished Items List ======" 
	for i in list:
		if i[3]!=True:
			print "  Item {0} - {1} - Due: {2} - {3} - {4}". format(i[0],i[1],i[2],getCompletionStatus(i),getAlertStatus(i))
			print '-------------------------------------------------------------------'

def displayCompletedItems(list):
	print "====== Completed Items List ======" 
	for i in list:
		if i[3]==True:
			print "  Item {0} - {1} - Due: {2} - {3} - {4}". format(i[0],i[1],i[2],getCompletionStatus(i),getAlertStatus(i))
			print '-------------------------------------------------------------------'

def startUp():
	print "Today is ", today
	displayAllListItems(dummyList)
	while quitFlag==False:
		showMenuOptions()
		chooseMenuOptions()

startUp()

# displayIncompleteItems(dummyList)
#displayCompletedItems(dummyList)