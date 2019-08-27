import gym
import gym_sim
env = gym.make('sim-v0')

#observation, reward, done, info = env.step(action)
env.render()
env.close()
