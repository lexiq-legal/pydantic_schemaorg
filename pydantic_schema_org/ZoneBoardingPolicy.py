from pydantic import Field
from pydantic_schema_org.BoardingPolicyType import BoardingPolicyType


class ZoneBoardingPolicy(BoardingPolicyType):
    """The airline boards by zones of the plane.

    See https://schema.org/ZoneBoardingPolicy.

    """

    locals().update({"@type": Field("ZoneBoardingPolicy", const=True)})


ZoneBoardingPolicy.update_forward_refs()
