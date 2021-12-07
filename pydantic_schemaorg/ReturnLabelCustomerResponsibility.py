from pydantic import Field
from pydantic_schemaorg.ReturnLabelSourceEnumeration import ReturnLabelSourceEnumeration


class ReturnLabelCustomerResponsibility(ReturnLabelSourceEnumeration):
    """Indicated that creating a return label is the responsibility of the customer.

    See https://schema.org/ReturnLabelCustomerResponsibility.

    """
    type_: str = Field("ReturnLabelCustomerResponsibility", const=True, alias='@type')
    

ReturnLabelCustomerResponsibility.update_forward_refs()
