from pydantic import Field
from pydantic_schemaorg.Landform import Landform


class Mountain(Landform):
    """A mountain, like Mount Whitney or Mount Everest.

    See https://schema.org/Mountain.

    """
    type_: str = Field("Mountain", const=True, alias='@type')
    

Mountain.update_forward_refs()
