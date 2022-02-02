from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.HowToItem import HowToItem


class HowToTool(HowToItem):
    """A tool used (but not consumed) when performing instructions for how to achieve a result.

    See: https://schema.org/HowToTool
    Model depth: 5
    """
    type_: str = Field("HowToTool", alias='@type')
    

