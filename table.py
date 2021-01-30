# coding=utf-8
from typing import Literal, List
from dataclasses import dataclass


JustifyMethod = Literal['right', 'left', 'center', 'full']


@dataclass()
class Header:
    """定义表格的Header属性"""

    content: str = None
    """表格首行的内容"""

    justify: JustifyMethod = 'full'
    """内容的间距"""

    width: int = None


class Table:
    """用于在控制台显示表格的类"""
    table_header: List[Header]

    def __init__(self,
                 title: str = None
                 ):
        self.title = title

    def add_header(
            self,
            content: str,
            justify: JustifyMethod = "full",
            width: int = None
    ) -> None:
        """将用户提供的每一个表格的首行定义为对象添加到table_header

        :param content: 保存用户提供的表格首行的内容
        :param justify: 定义显示时，内容是居中还是向右（左）对齐，或者是填充
        :param width: 定义其行的宽度，但提供的的参数小于的content时，将重新计算宽度
        """
        header = Header(
            content=content,
            justify=justify,
            width=width,
        )
        self.table_header.append(header)
