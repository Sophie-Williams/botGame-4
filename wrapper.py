import numpy as np
from core import base_environment
from gym import spaces
from output import output

class GymWrapper(object):
  def __init__(self, env):
    self._env = env

  @property
  def env(self):
    return self._env

  @property
  def _n_actions(self):
    return self.env.action_dim()

  def _observation(self): #this function should return an image, that's it, we can define null action here to do this.
    """
    Gym environment only supports one kind of observation
    """
    return output() #return the output when action is null or 0
	#return self.env.observation()[self._obsKey]


  def _reset(self): #this guy can be empty
    self.env.reset()
    return self._observation()


  def reset(self):
    return self._reset()


  def _step(self, action): #this function should take in the action, perform that action and then return the resultant image
    assert type(action) == np.ndarray, 'action must be a nd-array'
    self.env.step(action)
    obs    = output(action)  #just directly call the output function here, instead of self._observation(action) 
    reward = self.env.reward()
    done   = False
    return obs, reward, done, dict(reward=reward)


  def step(self, action):
    return self._step(action)
