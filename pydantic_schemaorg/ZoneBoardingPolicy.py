from pydantic import Field
from pydantic_schemaorg.BoardingPolicyType import BoardingPolicyType


class ZoneBoardingPolicy(BoardingPolicyType):
    """The airline boards by zones of the plane.

    See https://schema.org/ZoneBoardingPolicy.

    """
    type_: str = Field("ZoneBoardingPolicy", const=True, alias='@type')
    

ZoneBoardingPolicy.update_forward_refs()
