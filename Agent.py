from util import manhattanDistance
from game import Directions
import random, util

from game import Agent

## Example Agent
class ReflexAgent(Agent):

  def Action(self, gameState):

    move_candidate = gameState.getLegalActions()

    scores = [self.reflex_agent_evaluationFunc(gameState, action) for action in move_candidate]
    bestScore = max(scores)
    Index = [index for index in range(len(scores)) if scores[index] == bestScore]
    get_index = random.choice(Index)

    return move_candidate[get_index]

  def reflex_agent_evaluationFunc(self, currentGameState, action):

    successorGameState = currentGameState.generatePacmanSuccessor(action)
    newPos = successorGameState.getPacmanPosition()
    oldFood = currentGameState.getFood()
    newGhostStates = successorGameState.getGhostStates()
    newScaredTimes = [ghostState.scaredTimer for ghostState in newGhostStates]
    return successorGameState.getScore()



def scoreEvalFunc(currentGameState):

  return currentGameState.getScore()

class AdversialSearchAgent(Agent):

  def __init__(self, getFunc ='scoreEvalFunc', depth ='2'):
    self.index = 0
    self.evaluationFunction = util.lookup(getFunc, globals())

    self.depth = int(depth)

######################################################################################

class MinimaxAgent(AdversialSearchAgent):

  def Action(self, gameState):
    ####################### Write Your Code Here ################################
    def MaxAction(self, currentGameState, turn, depth):
      if depth == self.depth or currentGameState.isWin() or currentGameState.isLose():
        return self.evaluationFunction(currentGameState)
      move_candidate = currentGameState.getLegalActions(turn)
      best_score = float('-inf')
      best_action = Directions.STOP
      for action in move_candidate:
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        next_score = MinAction(self, successorGameState, turn+1, depth)
        if best_score < next_score:
          best_score = next_score
          best_action = action
      if depth == 0:
        return best_action
      return best_score

    def MinAction(self, currentGameState, turn, depth):
      if currentGameState.isWin() or currentGameState.isLose():
        return self.evaluationFunction(currentGameState)
      move_candidate = currentGameState.getLegalActions(turn)
      best_score = float('inf')
      for action in move_candidate:
        successorGameState = currentGameState.generateSuccessor(turn, action)
        if turn == currentGameState.getNumAgents() - 1:
          next_score = MaxAction(self, successorGameState, 0, depth+1)
        else:
          next_score = MinAction(self, successorGameState, turn+1, depth)
        best_score = min(best_score, next_score)
      return best_score
    #####
    return MaxAction(self, gameState, 0, 0)
    #raise Exception("Not implemented yet")

    ############################################################################




class AlphaBetaAgent(AdversialSearchAgent):

  def Action(self, gameState):
    ####################### Write Your Code Here ################################
    def Alpha(self, currentGameState, turn, depth, alpha, beta):
      if depth == self.depth or currentGameState.isWin() or currentGameState.isLose():
        return self.evaluationFunction(currentGameState)
      move_candidate = currentGameState.getLegalActions(turn)
      best_score = float('-inf')
      best_action = Directions.STOP
      for action in move_candidate:
        successorGameState = currentGameState.generateSuccessor(turn, action)
        next_score = Beta(self, successorGameState, turn+1, depth, alpha, beta)
        if beta < next_score:
          return next_score
        alpha = max(alpha, best_score)
        if best_score < next_score:
          best_score = next_score
          best_action = action
      if depth == 0:
        return best_action
      return best_score

    def Beta(self, currentGameState, turn, depth, alpha, beta):
      if currentGameState.isWin() or currentGameState.isLose():
        return self.evaluationFunction(currentGameState)
      move_candidate = currentGameState.getLegalActions(turn)
      best_score = float('inf')
      for action in move_candidate:
        successorGameState = currentGameState.generateSuccessor(turn, action)
        if turn == currentGameState.getNumAgents() - 1:
          next_score = Alpha(self, successorGameState, 0, depth+1, alpha, beta)
        else:
          next_score = Beta(self, successorGameState, turn+1, depth, alpha, beta)
        if alpha > next_score:
          return next_score
        beta = min(beta, next_score)
        best_score = min(best_score, next_score)
      return best_score
    #####
    return Alpha(self, gameState, 0, 0, float('-inf'), float('inf'))
    #raise Exception("Not implemented yet")

    ############################################################################



class ExpectimaxAgent(AdversialSearchAgent):

  def Action(self, gameState):
    ####################### Write Your Code Here ################################
    def ExpectiMaxAction(self, currentGameState, turn, depth):
      if depth == self.depth or currentGameState.isWin() or currentGameState.isLose():
        return self.evaluationFunction(currentGameState)
      move_candidate = currentGameState.getLegalActions(turn)
      best_score = float('-inf')
      best_action = Directions.STOP
      prob = 1.0/float(len(move_candidate))
      for action in move_candidate:
        successorGameState = currentGameState.generatePacmanSuccessor(action)
        next_score = prob * ExpectiMinAction(self, successorGameState, turn+1, depth)
        if best_score < next_score:
          best_score = next_score
          best_action = action
      if depth == 0:
        return best_action
      return best_score

    def ExpectiMinAction(self, currentGameState, turn, depth):
      if currentGameState.isWin() or currentGameState.isLose():
        return self.evaluationFunction(currentGameState)
      move_candidate = currentGameState.getLegalActions(turn)
      best_score = float('inf')
      prob = 1.0/float(len(move_candidate))
      for action in move_candidate:
        successorGameState = currentGameState.generateSuccessor(turn, action)
        if turn == currentGameState.getNumAgents() - 1:
          next_score = prob * ExpectiMaxAction(self, successorGameState, 0, depth+1)
        else:
          next_score = prob * ExpectiMinAction(self, successorGameState, turn+1, depth)
        best_score = min(best_score, next_score)
      return best_score
    #####
    return ExpectiMaxAction(self, gameState, 0, 0)
    #raise Exception("Not implemented yet")

    ############################################################################
