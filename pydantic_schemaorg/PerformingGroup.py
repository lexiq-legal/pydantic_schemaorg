from pydantic import Field
from pydantic_schemaorg.Organization import Organization


class PerformingGroup(Organization):
    """A performance group, such as a band, an orchestra, or a circus.

    See https://schema.org/PerformingGroup.

    """
    type_: str = Field("PerformingGroup", const=True, alias='@type')
    

PerformingGroup.update_forward_refs()
