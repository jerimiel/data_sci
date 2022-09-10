#!/usr/bin/env python
# coding: utf-8

# In[68]:


import numpy as np
import random


# In[ ]:





# In[69]:


P2=random.choice(['R','P','S'])


# In[74]:


def score(P1,P2):
    if P1==P2:
        reward = -1
        done=False
        print('draw')
    if P1=='R' and P2=='S':
        reward = 1
        done=True
        print('won')
    if P1=='R' and P2=='P':
        reward = -2
        done=False
        print('lost')
    if P1=='P' and P2=='S':
        reward = -2
        done=False
        print('lost')
    if P1=='P' and P2=='R':
        reward = 1
        done=True
        print('won')
    if P1=='S' and P2=='R':
        reward = -2
        done=False
        print('lost')
    if P1=='S' and P2=='P':
        reward = 1
        done=True
        print('won')
    return reward,done


# In[77]:


q_table=np.zeros((3,3))
learning_rate = 0.1
discount_factor = 0.6
exploration = 0.1
epochs = 20
game={'R':['R','P','S'],'P':['R','P','S'],'S':['R','P','S']}
for play in range(epochs):
    state=random.choice(['R','P','S'])
    play=random.choice(['R','P','S'])
    pos_state=['R','P','S'].index(state)
    done = False
    
    while not done:
        random_value = random.uniform(0, 1)
        if (random_value < exploration):
            action=['R','P','S'].index(play)
        else:
            action = np.argmax(q_table[pos_state]) # Use the action with the highest q-value
        next_state=game[state][action]
        reward,done= score(next_state,state)
        pos_next_state=['R','P','S'].index(next_state)
        prev_q = q_table[pos_state, action]
        next_max_q = np.max(q_table[pos_next_state])
        
        new_q = (1 - learning_rate) * prev_q + learning_rate * (reward + discount_factor * next_max_q)
        q_table[pos_state, action] = new_q
        
        state = next_state
        


# In[ ]:





# In[ ]:




