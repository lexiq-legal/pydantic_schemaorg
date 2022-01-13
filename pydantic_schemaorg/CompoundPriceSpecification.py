from __future__ import annotations
from typing import TYPE_CHECKING


from pydantic import Field

from typing import Union, List, Optional

from pydantic_schemaorg.PriceSpecification import PriceSpecification


class CompoundPriceSpecification(PriceSpecification):
    """A compound price specification is one that bundles multiple prices that all apply in"
     "combination for different dimensions of consumption. Use the name property of the attached"
     "unit price specification for indicating the dimension of a price component (e.g. \"electricity\""
     "or \"final cleaning\").

    See: https://schema.org/CompoundPriceSpecification
    Model depth: 5
    """

    type_: str = Field("CompoundPriceSpecification", const=True, alias="@type")
    priceType: "Optional[Union[List[Union[str, PriceTypeEnumeration]], Union[str, PriceTypeEnumeration]]]" = Field(
        None,
        description="Defines the type of a price specified for an offered product, for example a list price,"
        "a (temporary) sale price or a manufacturer suggested retail price. If multiple prices"
        "are specified for an offer the [[priceType]] property can be used to identify the type"
        "of each such specified price. The value of priceType can be specified as a value from enumeration"
        "PriceTypeEnumeration or as a free form text string for price types that are not already"
        "predefined in PriceTypeEnumeration.",
    )
    priceComponent: "Optional[Union[List[Union[UnitPriceSpecification, str]], Union[UnitPriceSpecification, str]]]" = Field(
        None,
        description="This property links to all [[UnitPriceSpecification]] nodes that apply in parallel"
        "for the [[CompoundPriceSpecification]] node.",
    )


if TYPE_CHECKING:

    from pydantic_schemaorg.PriceTypeEnumeration import PriceTypeEnumeration

    from pydantic_schemaorg.UnitPriceSpecification import UnitPriceSpecification

    CompoundPriceSpecification.update_forward_refs()
