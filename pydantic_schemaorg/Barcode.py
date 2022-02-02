from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ImageObject import ImageObject


class Barcode(ImageObject):
    """An image of a visual machine-readable code such as a barcode or QR code.

    See: https://schema.org/Barcode
    Model depth: 5
    """
    type_: str = Field("Barcode", alias='@type')
    

