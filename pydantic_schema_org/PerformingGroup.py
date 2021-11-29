from pydantic import Field
from pydantic_schema_org.Organization import Organization


class PerformingGroup(Organization):
    """A performance group, such as a band, an orchestra, or a circus.

    See https://schema.org/PerformingGroup.

    """

    locals().update({"@type": Field("PerformingGroup", const=True)})


PerformingGroup.update_forward_refs()
