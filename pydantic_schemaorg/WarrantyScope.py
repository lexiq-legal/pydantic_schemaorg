from pydantic import Field
from pydantic_schemaorg.Enumeration import Enumeration


class WarrantyScope(Enumeration):
    """A range of of services that will be provided to a customer free of charge in case of a defect"
     "or malfunction of a product. Commonly used values: * http://purl.org/goodrelations/v1#Labor-BringIn"
     "* http://purl.org/goodrelations/v1#PartsAndLabor-BringIn * http://purl.org/goodrelations/v1#PartsAndLabor-PickUp

    See https://schema.org/WarrantyScope.

    """

    locals().update({"@type": Field("WarrantyScope", const=True)})


WarrantyScope.update_forward_refs()
