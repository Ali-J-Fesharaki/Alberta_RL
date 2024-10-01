import torch 
from torch.distributions import Normal, Uniform, Bernoulli
import pandas as pd 
from torch.utils.tensorboard import SummaryWriter
logger=SummaryWriter(log_dir='./runs')
class KArmBandit():
    def __init__(self,k,distributions) :
        """
        Initialize the K-Armed Bandit.

        Args:
        k (int): NUmber of arms (bandits).
        distribution (list):list of PyTorch distribution objects for each arm.

        """
        assert len(distributions)==k
        self.k=k
        self.distributions=distributions

    def sample(self,arm):
        """
        
        Sample from the specified arms's distribution.

        Args:
        arm (int): The index of the arm sample from (0 to k-1)

        Returns:
        float: A sample (reward) from the specified arms's distribution.

        """

        assert 0<=arm<self.k, "Invalid arm index!"
        return self.distributions[arm].sample().item()#Sample from the chosen arm's distribution 
    

if(__name__=='__main__'):
    k=10
    epsilon=0.3
    actions=range(k)
    avgs=range(k)
    scales=torch.rand(k)
    q_table=pd.DataFrame()
    distributions=[]
    for index,avg in enumerate(avgs):
        distributions.append(Normal(loc=avg,scale=scales[index]))
    k_handler=KArmBandit(len(distributions),distributions)
    for i in range(1000):
        #random action
        
        #Epsilon_greedy
        best_action=q_table.iloc[0,:].argmax()
        actions=actions[actions!=best_action]
        idx=torch.randint(0,len(actions)-1,(1,)).item()
        random_action=actions[idx]
        if(Bernoulli(probs=epilon))

        reward=k_handler.sample(idx)
        q_table[str(idx)]=+reward

        logger.add_scalar('Reward',,i+1)
    
logger.close() 

        
