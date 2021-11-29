from pydantic import Field
from pydantic_schemaorg.UserInteraction import UserInteraction


class UserBlocks(UserInteraction):
    """UserInteraction and its subtypes is an old way of talking about users interacting with"
     "pages. It is generally better to use [[Action]]-based vocabulary, alongside types"
     "such as [[Comment]].

    See https://schema.org/UserBlocks.

    """

    locals().update({"@type": Field("UserBlocks", const=True)})


UserBlocks.update_forward_refs()
