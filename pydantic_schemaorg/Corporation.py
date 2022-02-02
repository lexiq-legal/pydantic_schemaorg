from __future__ import annotations
from typing import TYPE_CHECKING

from typing import Union, List, Optional


from pydantic import Field
from pydantic_schemaorg.Organization import Organization


class Corporation(Organization):
    """Organization: A business corporation.

    See: https://schema.org/Corporation
    Model depth: 3
    """
    type_: str = Field("Corporation", alias='@type')
    tickerSymbol: Optional[Union[List[Union[str, 'Text']], str, 'Text']] = Field(
        None,
        description="The exchange traded instrument associated with a Corporation object. The tickerSymbol"
     "is expressed as an exchange and an instrument name separated by a space character. For"
     "the exchange component of the tickerSymbol attribute, we recommend using the controlled"
     "vocabulary of Market Identifier Codes (MIC) specified in ISO15022.",
    )
    


if TYPE_CHECKING:
    from pydantic_schemaorg.Text import Text
