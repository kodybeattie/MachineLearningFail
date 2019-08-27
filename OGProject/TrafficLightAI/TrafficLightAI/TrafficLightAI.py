import gym
import gym_sim
env = gym.make('sim-v0')

env.render()
#observation, reward, done, info = env.step(action)
#print("reseting")
env.close()
#for t in range(5000):
    #   print("T = " + str(t) + " EP = " + str(i_episode))
    #  
    # if done:
    #    print("Episode finished after {} timesteps".format(t+1))
        #   break
