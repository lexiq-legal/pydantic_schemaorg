from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class BoardingPolicyType(Enumeration):
    """A type of boarding policy used by an airline.

    See https://schema.org/BoardingPolicyType.

    """

    locals().update({"@type": Field("BoardingPolicyType", const=True)})


BoardingPolicyType.update_forward_refs()
