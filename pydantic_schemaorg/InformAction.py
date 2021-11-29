from pydantic import Field
from typing import List, Optional, Union, Any
from pydantic_schemaorg.CommunicateAction import CommunicateAction


class InformAction(CommunicateAction):
    """The act of notifying someone of information pertinent to them, with no expectation of"
     "a response.

    See https://schema.org/InformAction.

    """

    event: Any = Field(
        None,
        description="Upcoming or past event associated with this place, organization, or action.",
    )
    locals().update({"@type": Field("InformAction", const=True)})


InformAction.update_forward_refs()