from pydantic import Field
from pydantic_schemaorg.FindAction import FindAction


class DiscoverAction(FindAction):
    """The act of discovering/finding an object.

    See https://schema.org/DiscoverAction.

    """

    locals().update({"@type": Field("DiscoverAction", const=True)})


DiscoverAction.update_forward_refs()
