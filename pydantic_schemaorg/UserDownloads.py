from pydantic import Field
from pydantic_schemaorg.UserInteraction import UserInteraction


class UserDownloads(UserInteraction):
    """UserInteraction and its subtypes is an old way of talking about users interacting with"
     "pages. It is generally better to use [[Action]]-based vocabulary, alongside types"
     "such as [[Comment]].

    See https://schema.org/UserDownloads.

    """

    locals().update({"@type": Field("UserDownloads", const=True)})


UserDownloads.update_forward_refs()
