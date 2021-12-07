from pydantic import Field
from pydantic_schemaorg.SizeSystemEnumeration import SizeSystemEnumeration


class SizeSystemImperial(SizeSystemEnumeration):
    """Imperial size system.

    See https://schema.org/SizeSystemImperial.

    """
    type_: str = Field("SizeSystemImperial", const=True, alias='@type')
    

SizeSystemImperial.update_forward_refs()
