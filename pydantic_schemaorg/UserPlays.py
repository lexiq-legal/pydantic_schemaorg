from pydantic import Field
from pydantic_schemaorg.UserInteraction import UserInteraction


class UserPlays(UserInteraction):
    """UserInteraction and its subtypes is an old way of talking about users interacting with"
     "pages. It is generally better to use [[Action]]-based vocabulary, alongside types"
     "such as [[Comment]].

    See https://schema.org/UserPlays.

    """

    locals().update({"@type": Field("UserPlays", const=True)})


UserPlays.update_forward_refs()
