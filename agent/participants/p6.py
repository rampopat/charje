import pandas as pd
import sys

from agents.rf_agent import RfAgent
from agents.random_agent_controller import RandomController

if __name__ == "__main__":
    controller = RandomAgentController(RfAgent(
            '0x3FFA1EA78d44488c43DE84B6D03C3b6C0DC7248E'))
    if len(sys.argv) == 3:
        controller.run(start_time=pd.to_datetime(sys.argv[1]),
                       end_time=pd.to_datetime(sys.argv[2]))
    elif len(sys.argv) == 4:
        controller.run(start_time=pd.to_datetime(sys.argv[1]),
                       end_time=pd.to_datetime(sys.argv[2]),
                       time_delta=pd.Timedelta(sys.argv[3]))
