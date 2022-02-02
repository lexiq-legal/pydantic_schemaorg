from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ReturnLabelSourceEnumeration import ReturnLabelSourceEnumeration


class ReturnLabelDownloadAndPrint(ReturnLabelSourceEnumeration):
    """Indicated that a return label must be downloaded and printed by the customer.

    See: https://schema.org/ReturnLabelDownloadAndPrint
    Model depth: 5
    """
    type_: str = Field("ReturnLabelDownloadAndPrint", alias='@type')
    

