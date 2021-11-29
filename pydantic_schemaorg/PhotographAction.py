from pydantic import Field
from pydantic_schemaorg.CreateAction import CreateAction


class PhotographAction(CreateAction):
    """The act of capturing still images of objects using a camera.

    See https://schema.org/PhotographAction.

    """

    locals().update({"@type": Field("PhotographAction", const=True)})


PhotographAction.update_forward_refs()
