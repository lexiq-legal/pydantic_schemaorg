from pydantic import Field
from pydantic_schemaorg.ReturnMethodEnumeration import ReturnMethodEnumeration


class ReturnAtKiosk(ReturnMethodEnumeration):
    """Specifies that product returns must be made at a kiosk.

    See https://schema.org/ReturnAtKiosk.

    """

    locals().update({"@type": Field("ReturnAtKiosk", const=True)})


ReturnAtKiosk.update_forward_refs()
