from pydantic import Field
from pydantic_schemaorg.EntertainmentBusiness import EntertainmentBusiness
from typing import Any, Union, List, Optional
from pydantic_schemaorg.PlayAction import PlayAction


class PerformAction(PlayAction):
    """The act of participating in performance arts.

    See https://schema.org/PerformAction.

    """

    entertainmentBusiness: Optional[Union[List[EntertainmentBusiness], EntertainmentBusiness]] = Field(
        None,
        description="A sub property of location. The entertainment business where the action occurred.",
    )
    locals().update({"@type": Field("PerformAction", const=True)})


PerformAction.update_forward_refs()
