from pydantic import Field
from pydantic_schemaorg.Organization import Organization
from pydantic_schemaorg.Person import Person
from typing import Any, Union, List, Optional
from pydantic_schemaorg.ReactAction import ReactAction


class EndorseAction(ReactAction):
    """An agent approves/certifies/likes/supports/sanction an object.

    See https://schema.org/EndorseAction.

    """

    endorsee: Optional[Union[List[Union[Organization, Person]], Union[Organization, Person]]] = Field(
        None,
        description="A sub property of participant. The person/organization being supported.",
    )
    locals().update({"@type": Field("EndorseAction", const=True)})


EndorseAction.update_forward_refs()
