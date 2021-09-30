#!/usr/bin/env python
# encoding: utf-8

"""
Testing iter_block_items()
"""

from __future__ import (
    absolute_import, division, print_function, unicode_literals
)

from docx import Document
from docx.document import Document as _Document
from docx.oxml.text.paragraph import CT_P
from docx.oxml.table import CT_Tbl
from docx.table import _Cell, Table
from docx.text.paragraph import Paragraph


def iter_block_items(parent):
    """
    Generate a reference to each paragraph and table child within *parent*,
    in document order. Each returned value is an instance of either Table or
    Paragraph. *parent* would most commonly be a reference to a main
    Document object, but also works for a _Cell object, which itself can
    contain paragraphs and tables.
    """
    if isinstance(parent, _Document):
        parent_elm = parent.element.body
        # print(parent_elm.xml)
    elif isinstance(parent, _Cell):
        parent_elm = parent._tc
    else:
        raise ValueError("something's not right")

    for child in parent_elm.iterchildren():
        if isinstance(child, CT_P):
            yield Paragraph(child, parent)
        elif isinstance(child, CT_Tbl):
            yield Table(child, parent)


document = Document('【有研硅】财务部分.docx')
list = []
tableIndex = 0
for idx, block in enumerate(iter_block_items(document)):
    target = block.text if isinstance(block, Paragraph) else '<table>'
    list.append(target)
    if target == "<table>":
        list.pop(-1)
        list.append(f"Sheet{tableIndex}")
        tableIndex += 1

tableInput = input("请输入工作表名称：")
index = list.index(tableInput)
print(list[index-2])
print(list[index-1])
print(list[index+1])
print(list[index+2])
