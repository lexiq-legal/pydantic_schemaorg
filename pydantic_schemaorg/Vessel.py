from pydantic import Field
from pydantic_schemaorg.AnatomicalStructure import AnatomicalStructure


class Vessel(AnatomicalStructure):
    """A component of the human body circulatory system comprised of an intricate network of"
     "hollow tubes that transport blood throughout the entire body.

    See https://schema.org/Vessel.

    """
    type_: str = Field("Vessel", const=True, alias='@type')
    

Vessel.update_forward_refs()
