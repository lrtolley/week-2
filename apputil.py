import numpy as np


# update/add code below ...

def ways(n):
    ''' 
    tells how many ways to make change 
    using only nickles and pennies
    '''
    ans = (n//5)+1 #the number of ways to make change for n cents using only nickles 
                  # and pennies is the number of times a nickle can fit into n cents + 1 (the all pennies way)
    return ans

def ways2(coins):
    ''' tells how many ways there are to make change using pennies and nickles'''
    dp = [0] * (coins + 1) # Create a list to store the number of ways to make change for each amount
    dp[0] = 1 # There is one way to make change for 0 cents
    for coin in [1, 5]: # Iterate over each coin denomination
        for x in range(coin, coins + 1): # Iterate over each amount from the coin value to the target amount
            dp[x] += dp[x - coin] # Update the number of ways to make change for the current amount
    return dp[coins] # Return the number of ways to make change for the target amount


def lowest_score(names, scores):
    '''
    Returns the name of the person with the lowest score.
    names: np.array of names
    scores: np.array of scores
    '''
    minscore = np.argmin(scores) # find the index of the minimum score

    return names[minscore] # return the name corresponding to the minimum score

def sort_names(names, scores):
    '''
    Returns a list of names sorted by their scores in descending order.
    names: array of names
    scores: array of scores'''
    zipped_scores = dict(zip(names, scores))
    sorted_score = sorted(zipped_scores.items(), key=lambda item: item[1], reverse=True)
    #cleaned_score = [item[0] for item in sorted_score]
    
    return sorted_score
