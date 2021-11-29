from pydantic import Field
from pydantic_schemaorg.ReturnLabelSourceEnumeration import ReturnLabelSourceEnumeration


class ReturnLabelDownloadAndPrint(ReturnLabelSourceEnumeration):
    """Indicated that a return label must be downloaded and printed by the customer.

    See https://schema.org/ReturnLabelDownloadAndPrint.

    """

    locals().update({"@type": Field("ReturnLabelDownloadAndPrint", const=True)})


ReturnLabelDownloadAndPrint.update_forward_refs()
