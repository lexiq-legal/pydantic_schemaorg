from pydantic import Field
from pydantic_schemaorg.TransferAction import TransferAction


class DownloadAction(TransferAction):
    """The act of downloading an object.

    See https://schema.org/DownloadAction.

    """
    type_: str = Field("DownloadAction", const=True, alias='@type')
    

DownloadAction.update_forward_refs()
