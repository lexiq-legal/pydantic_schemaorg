from __future__ import annotations


from pydantic import Field
from pydantic_schemaorg.Project import Project


class FundingAgency(Project):
    """A FundingAgency is an organization that implements one or more [[FundingScheme]]s"
     "and manages the granting process (via [[Grant]]s, typically [[MonetaryGrant]]s)."
     "A funding agency is not always required for grant funding, e.g. philanthropic giving,"
     "corporate sponsorship etc. Examples of funding agencies include ERC, REA, NIH, Bill"
     "and Melinda Gates Foundation...

    See: https://schema.org/FundingAgency
    Model depth: 4
    """
    type_: str = Field("FundingAgency", alias='@type')
    

