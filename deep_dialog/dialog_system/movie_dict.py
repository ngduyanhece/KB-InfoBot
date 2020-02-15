'''

'''

import pickle as pickle
import copy
import nltk
import string

from collections import defaultdict
from deep_dialog.tools import to_tokens
import json

class MovieDict:
    def __init__(self, path):
        self.load_dict(path)
        self.count_values()
        self._build_token_index()
    
    def load_dict(self, path):
        # with open(path, 'rb') as f:
        #     u = pickle._Unpickler(f)
        #     u.encoding = 'latin1'
        #     dict_data = u.load()
        with open(path, 'r') as f:
            dict_data = json.load(f)
        #dict_data = pickle.load(open(path, 'rb'))
        self.dict = copy.deepcopy(dict_data)

    def count_values(self):
        self.lengths = {}
        for k,v in self.dict.items():
            self.lengths[k] = len(v)

    def _build_token_index(self):
        self.tokens = {}
        for slot,vals in self.dict.items():
            self.tokens[slot] = defaultdict(list)
            for vi,vv in enumerate(vals):
                w_v = to_tokens(vv)
                for w in w_v: self.tokens[slot][w].append(vi)
