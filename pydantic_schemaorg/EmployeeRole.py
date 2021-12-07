from pydantic import Field
from typing import Any, Optional, Union, List
from pydantic_schemaorg.PriceSpecification import PriceSpecification
from decimal import Decimal
from pydantic_schemaorg.OrganizationRole import OrganizationRole


class EmployeeRole(OrganizationRole):
    """A subclass of OrganizationRole used to describe employee relationships.

    See https://schema.org/EmployeeRole.

    """
    type_: str = Field("EmployeeRole", const=True, alias='@type')
    salaryCurrency: Optional[Union[List[str], str]] = Field(
        None,
        description="The currency (coded using [ISO 4217](http://en.wikipedia.org/wiki/ISO_4217) )"
     "used for the main salary information in this job posting or for this employee.",
    )
    baseSalary: Union[List[Union[Decimal, PriceSpecification, Any]], Union[Decimal, PriceSpecification, Any]] = Field(
        None,
        description="The base salary of the job or of an employee in an EmployeeRole.",
    )
    

EmployeeRole.update_forward_refs()
