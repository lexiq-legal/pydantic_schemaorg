from pydantic import Field, AnyUrl
from typing import Any, Union, List, Optional
from pydantic_schemaorg.CreativeWork import CreativeWork


class DataCatalog(CreativeWork):
    """A collection of datasets.

    See https://schema.org/DataCatalog.

    """

    measurementTechnique: Optional[Union[List[Union[AnyUrl, str]], Union[AnyUrl, str]]] = Field(
        None,
        description="A technique or technology used in a [[Dataset]] (or [[DataDownload]], [[DataCatalog]]),"
     "corresponding to the method used for measuring the corresponding variable(s) (described"
     "using [[variableMeasured]]). This is oriented towards scientific and scholarly dataset"
     "publication but may have broader applicability; it is not intended as a full representation"
     "of measurement, but rather as a high level summary for dataset discovery. For example,"
     "if [[variableMeasured]] is: molecule concentration, [[measurementTechnique]]"
     "could be: \"mass spectrometry\" or \"nmr spectroscopy\" or \"colorimetry\" or \"immunofluorescence\"."
     "If the [[variableMeasured]] is \"depression rating\", the [[measurementTechnique]]"
     "could be \"Zung Scale\" or \"HAM-D\" or \"Beck Depression Inventory\". If there are"
     "several [[variableMeasured]] properties recorded for some given data object, use"
     "a [[PropertyValue]] for each [[variableMeasured]] and attach the corresponding [[measurementTechnique]].",
    )
    dataset: Any = Field(
        None,
        description="A dataset contained in this catalog.",
    )
    locals().update({"@type": Field("DataCatalog", const=True)})


DataCatalog.update_forward_refs()
