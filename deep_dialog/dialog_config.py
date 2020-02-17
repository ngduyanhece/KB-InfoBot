'''
'''

all_acts = ['request', 'inform']
inform_slots = ['brand','color','material']

sys_request_slots = ['brand','color','material']

start_dia_acts = {
    #'greeting':[],
    'request':['brand', 'color']
}   

#reward information
FAILED_DIALOG_REWARD = -1
SUCCESS_DIALOG_REWARD = 2
PER_TURN_REWARD = -0.1
SUCCESS_MAX_RANK = 5
MAX_TURN = 10

MODEL_PATH = './data/pretrained/'