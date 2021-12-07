from pydantic import Field
from pydantic_schemaorg.CreateAction import CreateAction


class PhotographAction(CreateAction):
    """The act of capturing still images of objects using a camera.

    See https://schema.org/PhotographAction.

    """
    type_: str = Field("PhotographAction", const=True, alias='@type')
    

PhotographAction.update_forward_refs()
