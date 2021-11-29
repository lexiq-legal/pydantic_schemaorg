from pydantic import Field
from pydantic_schemaorg.Project import Project


class FundingAgency(Project):
    """A FundingAgency is an organization that implements one or more [[FundingScheme]]s"
     "and manages the granting process (via [[Grant]]s, typically [[MonetaryGrant]]s)."
     "A funding agency is not always required for grant funding, e.g. philanthropic giving,"
     "corporate sponsorship etc. Examples of funding agencies include ERC, REA, NIH, Bill"
     "and Melinda Gates Foundation...

    See https://schema.org/FundingAgency.

    """

    locals().update({"@type": Field("FundingAgency", const=True)})


FundingAgency.update_forward_refs()
