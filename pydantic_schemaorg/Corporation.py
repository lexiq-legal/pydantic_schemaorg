from pydantic import Field
from typing import Any, Optional, Union, List
from pydantic_schemaorg.Organization import Organization


class Corporation(Organization):
    """Organization: A business corporation.

    See https://schema.org/Corporation.

    """
    type_: str = Field("Corporation", const=True, alias='@type')
    tickerSymbol: Optional[Union[List[str], str]] = Field(
        None,
        description="The exchange traded instrument associated with a Corporation object. The tickerSymbol"
     "is expressed as an exchange and an instrument name separated by a space character. For"
     "the exchange component of the tickerSymbol attribute, we recommend using the controlled"
     "vocabulary of Market Identifier Codes (MIC) specified in ISO15022.",
    )
    

Corporation.update_forward_refs()
