from pydantic import Field
from pydantic_schemaorg.HowToItem import HowToItem


class HowToTool(HowToItem):
    """A tool used (but not consumed) when performing instructions for how to achieve a result.

    See https://schema.org/HowToTool.

    """

    locals().update({"@type": Field("HowToTool", const=True)})


HowToTool.update_forward_refs()
