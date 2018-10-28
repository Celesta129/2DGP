class MainFrameWork:
    def __init__(self,state):
        self.enter = state.enter
        self.exit = state.exit
        self.pause = state.pause
        self.resume = state.resume
        self.handle_events = state.handle_events
        self.update = state.update
        self.draw = state.draw


running = False
stack = None


def run(state_current):
    global running, stack
    running = True
    stack = [state_current]
    state_current.enter()
    while(running):
        stack[-1].handle_events()
        stack[-1].update()
        stack[-1].draw()

    # stack의 위부터 반복적으로 지운다.
    while(len(stack)>0):
        stack[-1].exit()
        stack.pop()



def change_state(state):
    pass


def pop_state(state):
    pass


def push_state(state):
    pass


def quit():
    global running
    running = False

