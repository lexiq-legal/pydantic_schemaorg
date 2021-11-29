from pydantic import Field
from pydantic_schemaorg.ReturnMethodEnumeration import ReturnMethodEnumeration


class ReturnByMail(ReturnMethodEnumeration):
    """Specifies that product returns must to be done by mail.

    See https://schema.org/ReturnByMail.

    """

    locals().update({"@type": Field("ReturnByMail", const=True)})


ReturnByMail.update_forward_refs()
