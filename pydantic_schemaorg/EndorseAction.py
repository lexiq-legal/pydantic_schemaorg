from pydantic import Field
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Person import Person
from typing import Any, Optional, Union, List
from pydantic_schemaorg.ReactAction import ReactAction


class EndorseAction(ReactAction):
    """An agent approves/certifies/likes/supports/sanction an object.

    See https://schema.org/EndorseAction.

    """
    type_: str = Field("EndorseAction", const=True, alias='@type')
    endorsee: Optional[Union[List[Union[Organization, Person]], Union[Organization, Person]]] = Field(
        None,
        description="A sub property of participant. The person/organization being supported.",
    )
    

EndorseAction.update_forward_refs()
