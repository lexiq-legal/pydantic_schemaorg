from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.ReturnLabelSourceEnumeration import ReturnLabelSourceEnumeration


class ReturnLabelCustomerResponsibility(ReturnLabelSourceEnumeration):
    """Indicated that creating a return label is the responsibility of the customer.

    See: https://schema.org/ReturnLabelCustomerResponsibility
    Model depth: 5
    """
    type_: str = Field("ReturnLabelCustomerResponsibility", alias='@type')
    

