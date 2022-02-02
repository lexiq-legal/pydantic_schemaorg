from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ConsumeAction import ConsumeAction


class InstallAction(ConsumeAction):
    """The act of installing an application.

    See: https://schema.org/InstallAction
    Model depth: 4
    """
    type_: str = Field("InstallAction", alias='@type')
    

