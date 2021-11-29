from pydantic import Field
from pydantic_schemaorg.ImageObject import ImageObject


class Barcode(ImageObject):
    """An image of a visual machine-readable code such as a barcode or QR code.

    See https://schema.org/Barcode.

    """

    locals().update({"@type": Field("Barcode", const=True)})


Barcode.update_forward_refs()
