from typing import Literal

class Table:
    """用于在控制台显示表格的类"""
    JustifyMethod = Literal['right', 'left', 'center']

    def __init__(self):


    def add_header(
            self,
            content: str,
            justify: JustifyMethod="right",
            width: int=None
    ):

