from pydantic import Field
from pydantic_schemaorg.ConsumeAction import ConsumeAction


class InstallAction(ConsumeAction):
    """The act of installing an application.

    See https://schema.org/InstallAction.

    """
    type_: str = Field("InstallAction", const=True, alias='@type')
    

InstallAction.update_forward_refs()
