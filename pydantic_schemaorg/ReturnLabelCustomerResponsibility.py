from pydantic import Field
from pydantic_schemaorg.ReturnLabelSourceEnumeration import ReturnLabelSourceEnumeration


class ReturnLabelCustomerResponsibility(ReturnLabelSourceEnumeration):
    """Indicated that creating a return label is the responsibility of the customer.

    See https://schema.org/ReturnLabelCustomerResponsibility.

    """

    locals().update({"@type": Field("ReturnLabelCustomerResponsibility", const=True)})


ReturnLabelCustomerResponsibility.update_forward_refs()
