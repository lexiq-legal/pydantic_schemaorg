from pydantic import Field
from pydantic_schemaorg.ReturnMethodEnumeration import ReturnMethodEnumeration


class ReturnAtKiosk(ReturnMethodEnumeration):
    """Specifies that product returns must be made at a kiosk.

    See https://schema.org/ReturnAtKiosk.

    """
    type_: str = Field("ReturnAtKiosk", const=True, alias='@type')
    

ReturnAtKiosk.update_forward_refs()
