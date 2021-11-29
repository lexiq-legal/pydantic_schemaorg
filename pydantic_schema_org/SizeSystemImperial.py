from pydantic import Field
from pydantic_schema_org.SizeSystemEnumeration import SizeSystemEnumeration


class SizeSystemImperial(SizeSystemEnumeration):
    """Imperial size system.

    See https://schema.org/SizeSystemImperial.

    """

    locals().update({"@type": Field("SizeSystemImperial", const=True)})


SizeSystemImperial.update_forward_refs()
