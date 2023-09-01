import json
from typing import Type

from pydantic import BaseModel, Field

from superagi.tools.base_tool import BaseTool


class TestEthInput(BaseModel):
    print_line: str = Field(..., description="The string to print. default value is \"Hello from Ethereum\"")
 


class TestEthTool(BaseTool):
    """
    Runs Ethereum scripts

    Attributes:
        name : The name of the tool.
        description : The description of the tool.
        args_schema : The args schema.
    """
    name: str = "Test Ethereum"
    args_schema: Type[BaseModel] = TestEthInput
    description: str = "Runs Ethereum scripts"

    def _execute(self, print_line: str = "Hello from Ethereum") -> str:
        """
        Execute the test ethereum tool.

        Args:
            print_line : The string to print. Defaults to "Hello from Ethereum".
           

        Returns:
            print the line from input
        """
        return print_line

