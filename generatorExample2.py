import random

def get_data():
    """Return 3 random integers between 0 and 9"""
    return random.sample(range(10), 3)

def averageOp():
    """Displays a running average across lists of integers sent to it"""
    running_sum = 0
    data_items_seen = 0

    while True:
        data = yield
        data_items_seen += len(data)
        running_sum += sum(data)
		#g = (x for x in data)
		#print(list(g))		
        print('The running average is {}'.format(running_sum / float(data_items_seen)))

def generatefunc(averageOpr):
    """Produces a set of values and forwards them to the pre-defined averageOpr
    function"""
    while True:
        data = get_data()
        print('Produced {}'.format(data))
        averageOpr.send(data)
        yield

if __name__ == '__main__':
    averageOpr = averageOp()
    averageOpr.send(None)
	#	print("Start")
	
    generator = generatefunc(averageOpr)

    for i in range(10):
        print('Generating...')
        next(generator)	