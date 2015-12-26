import state
import states

sm = state.StateManager()

sm.switchTo(states.CheckServerState())
sm.doModal()
