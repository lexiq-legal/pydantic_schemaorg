from pydantic import Field
from pydantic_schemaorg.CategoryCode import CategoryCode
from typing import Any, Union, List, Optional
from pydantic_schemaorg.DefinedTermSet import DefinedTermSet


class CategoryCodeSet(DefinedTermSet):
    """A set of Category Code values.

    See https://schema.org/CategoryCodeSet.

    """

    hasCategoryCode: Optional[Union[List[CategoryCode], CategoryCode]] = Field(
        None,
        description="A Category code contained in this code set.",
    )
    locals().update({"@type": Field("CategoryCodeSet", const=True)})


CategoryCodeSet.update_forward_refs()
