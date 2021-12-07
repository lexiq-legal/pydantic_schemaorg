from pydantic import Field
from pydantic_schemaorg.HowToItem import HowToItem


class HowToTool(HowToItem):
    """A tool used (but not consumed) when performing instructions for how to achieve a result.

    See https://schema.org/HowToTool.

    """
    type_: str = Field("HowToTool", const=True, alias='@type')
    

HowToTool.update_forward_refs()
