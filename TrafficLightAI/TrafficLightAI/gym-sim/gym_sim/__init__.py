from gym.envs.registration import register

register(
    id='sim-v0',
    entry_point='gym_sim.envs.sim_env:SimEnv',
)
