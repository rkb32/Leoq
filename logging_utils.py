import matplotlib.pyplot as plt

def plot_rewards(rewards):
    plt.plot(rewards)
    plt.title("Training Rewards")
    plt.xlabel("Episode")
    plt.ylabel("Reward")
    plt.savefig("training_rewards.png")
    plt.close()
def plot_loss(losses):
    plt.plot(losses)
    plt.title("Training Loss")
    plt.xlabel("Step")
    plt.ylabel("Loss")
    plt.savefig("training_loss.png")
    plt.close()
