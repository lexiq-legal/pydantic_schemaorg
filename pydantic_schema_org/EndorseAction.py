from pydantic import Field
from pydantic_schema_org.Person import Person
from pydantic_schema_org.Organization import Organization
from typing import Any, Optional, Union, List
from pydantic_schema_org.ReactAction import ReactAction


class EndorseAction(ReactAction):
    """An agent approves/certifies/likes/supports/sanction an object.

    See https://schema.org/EndorseAction.

    """

    endorsee: Optional[Union[List[Union[Person, Organization]], Union[Person, Organization]]] = Field(
        None,
        description="A sub property of participant. The person/organization being supported.",
    )
    locals().update({"@type": Field("EndorseAction", const=True)})


EndorseAction.update_forward_refs()
