from pydantic import Field
from pydantic_schemaorg.TransferAction import TransferAction


class DownloadAction(TransferAction):
    """The act of downloading an object.

    See https://schema.org/DownloadAction.

    """

    locals().update({"@type": Field("DownloadAction", const=True)})


DownloadAction.update_forward_refs()
