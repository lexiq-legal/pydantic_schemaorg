from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class BoardingPolicyType(Enumeration):
    """A type of boarding policy used by an airline.

    See https://schema.org/BoardingPolicyType.

    """
    type_: str = Field("BoardingPolicyType", const=True, alias='@type')
    

BoardingPolicyType.update_forward_refs()
