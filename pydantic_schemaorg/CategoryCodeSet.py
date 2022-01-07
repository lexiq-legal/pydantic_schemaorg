from pydantic import Field
from pydantic_schemaorg.CategoryCode import CategoryCode
from typing import List, Optional, Union
from pydantic_schemaorg.DefinedTermSet import DefinedTermSet


class CategoryCodeSet(DefinedTermSet):
    """A set of Category Code values.

    See https://schema.org/CategoryCodeSet.

    """
    type_: str = Field("CategoryCodeSet", const=True, alias='@type')
    hasCategoryCode: Optional[Union[List[Union[CategoryCode, str]], Union[CategoryCode, str]]] = Field(
        None,
        description="A Category code contained in this code set.",
    )
    

CategoryCodeSet.update_forward_refs()
