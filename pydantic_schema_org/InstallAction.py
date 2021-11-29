from pydantic import Field
from pydantic_schema_org.ConsumeAction import ConsumeAction


class InstallAction(ConsumeAction):
    """The act of installing an application.

    See https://schema.org/InstallAction.

    """

    locals().update({"@type": Field("InstallAction", const=True)})


InstallAction.update_forward_refs()
