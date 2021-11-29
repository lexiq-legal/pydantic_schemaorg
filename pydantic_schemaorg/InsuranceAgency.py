from pydantic import Field
from pydantic_schemaorg.FinancialService import FinancialService


class InsuranceAgency(FinancialService):
    """An Insurance agency.

    See https://schema.org/InsuranceAgency.

    """

    locals().update({"@type": Field("InsuranceAgency", const=True)})


InsuranceAgency.update_forward_refs()
