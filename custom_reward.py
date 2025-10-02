def smooth_navigation_reward(state, action, done):
    """Custom reward: penalizes collisions, rewards smoother actions.""" 
    reward = 0 
    # Example: negative reward if collision 
    if state.get("collision", False): 
        reward -= 10 
 
    # Positive reward for smooth small actions 
        reward += 2 
 
    # Bonus for episode completion without collision 
    if done and not state.get("collision", False): 
        reward += 20 
 
    return reward 
