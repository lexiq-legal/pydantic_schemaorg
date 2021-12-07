from pydantic import Field
from pydantic_schemaorg.ReturnMethodEnumeration import ReturnMethodEnumeration


class ReturnByMail(ReturnMethodEnumeration):
    """Specifies that product returns must to be done by mail.

    See https://schema.org/ReturnByMail.

    """
    type_: str = Field("ReturnByMail", const=True, alias='@type')
    

ReturnByMail.update_forward_refs()
