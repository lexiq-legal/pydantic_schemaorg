from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.TransferAction import TransferAction


class DownloadAction(TransferAction):
    """The act of downloading an object.

    See: https://schema.org/DownloadAction
    Model depth: 4
    """
    type_: str = Field("DownloadAction", alias='@type')
    

