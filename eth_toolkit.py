from abc import ABC
from superagi.tools.base_tool import BaseToolkit, BaseTool
from typing import Type, List
from superagi.tools.external_tools.ethToolkit.test_eth import TestEthTool



class EthereumToolkit(BaseToolkit, ABC):
    name: str = "Ethereum Toolkit"
    description: str = "Ethereum Tool kit contains all tools related to interacting with Ethereum"

    def get_tools(self) -> List[BaseTool]:
        return [TestEthTool()]

    def get_env_keys(self) -> List[str]:
        return ["ETH_PRIVATE_KEY"]
