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

import time
frame_time = 0.0

def run(state_current):
    global running, stack
    global frame_time
    current_time = time.time()
    running = True
    stack = [state_current]
    state_current.enter()
    while(running):
        stack[-1].handle_events()
        stack[-1].update()
        stack[-1].draw()
        #frame time 계산
        frame_time = time.time() - current_time
        frame_rate = 1.0/frame_time
        current_time += frame_time


    # stack의 위부터 반복적으로 지운다.
    while(len(stack)>0):
        stack[-1].exit()
        stack.pop()



def change_state(state):
    global stack
    if (len(stack) > 0):
        # execute the current state's exit function
        stack[-1].exit()
        # remove the current state
        stack.pop()
    stack.append(state)
    state.enter()
    pass


def pop_state():
    global stack
    if (len(stack) > 0):
        # execute the current state's exit function
        stack[-1].exit()
        # remove the current state
        stack.pop()

    # execute resume function of the previous state
    if (len(stack) > 0):
        stack[-1].resume()
    pass


def push_state(state):
    global stack
    if (len(stack) > 0):
        stack[-1].pause()
    stack.append(state)
    state.enter()


def quit():
    global running
    running = False

