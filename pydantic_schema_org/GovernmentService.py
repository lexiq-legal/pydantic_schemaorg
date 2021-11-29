from pydantic import Field
from pydantic_schema_org.AdministrativeArea import AdministrativeArea
from typing import Any, Optional, Union, List
from pydantic_schema_org.Organization import Organization
from pydantic_schema_org.Service import Service


class GovernmentService(Service):
    """A service provided by a government organization, e.g. food stamps, veterans benefits,"
     "etc.

    See https://schema.org/GovernmentService.

    """

    jurisdiction: Optional[Union[List[Union[str, AdministrativeArea]], Union[str, AdministrativeArea]]] = Field(
        None,
        description="Indicates a legal jurisdiction, e.g. of some legislation, or where some government"
     "service is based.",
    )
    serviceOperator: Optional[Union[List[Organization], Organization]] = Field(
        None,
        description="The operating organization, if different from the provider. This enables the representation"
     "of services that are provided by an organization, but operated by another organization"
     "like a subcontractor.",
    )
    locals().update({"@type": Field("GovernmentService", const=True)})


GovernmentService.update_forward_refs()
