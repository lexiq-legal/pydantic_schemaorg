from pydantic import Field
from typing import Any, Union, List, Optional
from pydantic_schemaorg.PriceSpecification import PriceSpecification
from decimal import Decimal
from pydantic_schemaorg.OrganizationRole import OrganizationRole


class EmployeeRole(OrganizationRole):
    """A subclass of OrganizationRole used to describe employee relationships.

    See https://schema.org/EmployeeRole.

    """

    salaryCurrency: Optional[Union[List[str], str]] = Field(
        None,
        description="The currency (coded using [ISO 4217](http://en.wikipedia.org/wiki/ISO_4217) )"
     "used for the main salary information in this job posting or for this employee.",
    )
    baseSalary: Union[List[Union[Decimal, PriceSpecification, Any]], Union[Decimal, PriceSpecification, Any]] = Field(
        None,
        description="The base salary of the job or of an employee in an EmployeeRole.",
    )
    locals().update({"@type": Field("EmployeeRole", const=True)})


EmployeeRole.update_forward_refs()
