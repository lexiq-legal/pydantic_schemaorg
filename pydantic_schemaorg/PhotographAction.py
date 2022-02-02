from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.CreateAction import CreateAction


class PhotographAction(CreateAction):
    """The act of capturing still images of objects using a camera.

    See: https://schema.org/PhotographAction
    Model depth: 4
    """
    type_: str = Field("PhotographAction", alias='@type')
    

