# Set 1
from collections import deque

# Problem 1:
# At a cultural festival, multiple performances are scheduled on a single stage. 
# However, due to last-minute changes, some performances need to be rescheduled or canceled. 
# The festival organizers use a stack to manage these changes efficiently.
# You are given a list changes of strings where each string represents a change action. 
# The actions can be:
#   "Schedule X": Schedule a performance with ID X on the stage.
#   "Cancel": Cancel the most recently scheduled performance that hasn't been canceled yet.
#   "Reschedule": Reschedule the most recently canceled performance to be the next on stage.
# Return a list of performance IDs that remain scheduled on the stage after all changes have been applied.

def manage_stage_changes(changes):
    # iterate through each change in changes
    # maintain a stack with each scheduled performance
    # modify the stack when canceled is called (remove the performancce and use a variable to hold it)
    # add the canceled performance back into the stack when reschedule is called
    # if there is no previously canceled performance, then do nothing ?

    stack = []
    canceled = ""
    for change in changes:
        if "Schedule" in change:
            id = change[len(change) - 1] # performance id
            stack.append(id)
        elif "Cancel" in change:
            canceled = stack.pop()
        elif "Reschedule" in change:
            if canceled != "":
                stack.append(canceled)
    
    return stack

# Tests
print(manage_stage_changes(["Schedule A", "Schedule B", "Cancel", "Schedule C", "Reschedule", "Schedule D"]))  
print(manage_stage_changes(["Schedule A", "Cancel", "Schedule B", "Cancel", "Reschedule", "Cancel"])) 
print(manage_stage_changes(["Schedule X", "Schedule Y", "Cancel", "Cancel", "Schedule Z"]))

# Problem 2
# You are organizing a festival and want to manage the queue of requests to perform. 
# Each request has a priority. Use a queue to process the performance requests in the order they 
# arrive but ensure that requests with higher priorities are processed before those with lower 
# priorities. Return the order in which performances are processed.
def process_performance_requests(requests):
    # iterate through each request and add to queue
    # if priority is higher than previously added, then add it before and queue can't be empty
    # if priority is lower than previously added, then add it after
    # return the just performances of queue

    queue = deque(sorted(requests, reverse = True))
    print(queue)
    result = []

    while queue: # still has items
        priority, performance = queue.popleft()
        result.append(performance)
    
    return result

# Tests
print(process_performance_requests([(3, 'Dance'), (5, 'Music'), (1, 'Drama')]))
print(process_performance_requests([(2, 'Poetry'), (1, 'Magic Show'), (4, 'Concert'), (3, 'Stand-up Comedy')]))
print(process_performance_requests([(1, 'Art Exhibition'), (3, 'Film Screening'), (2, 'Workshop'), (5, 'Keynote Speech'), (4, 'Panel Discussion')]))

