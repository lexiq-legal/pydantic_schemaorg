from pydantic import Field, AnyUrl
from pydantic_schemaorg.DataCatalog import DataCatalog
from typing import Any, Union, List, Optional
from datetime import datetime
from pydantic_schemaorg.DataDownload import DataDownload
from pydantic_schemaorg.PropertyValue import PropertyValue
from pydantic_schemaorg.CreativeWork import CreativeWork


class Dataset(CreativeWork):
    """A body of structured information describing some topic(s) of interest.

    See https://schema.org/Dataset.

    """

    includedDataCatalog: Optional[Union[List[DataCatalog], DataCatalog]] = Field(
        None,
        description="A data catalog which contains this dataset (this property was previously 'catalog',"
     "preferred name is now 'includedInDataCatalog').",
    )
    datasetTimeInterval: Optional[Union[List[datetime], datetime]] = Field(
        None,
        description="The range of temporal applicability of a dataset, e.g. for a 2011 census dataset, the"
     "year 2011 (in ISO 8601 time interval format).",
    )
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
    catalog: Optional[Union[List[DataCatalog], DataCatalog]] = Field(
        None,
        description="A data catalog which contains this dataset.",
    )
    distribution: Optional[Union[List[DataDownload], DataDownload]] = Field(
        None,
        description="A downloadable form of this dataset, at a specific location, in a specific format.",
    )
    includedInDataCatalog: Optional[Union[List[DataCatalog], DataCatalog]] = Field(
        None,
        description="A data catalog which contains this dataset.",
    )
    issn: Optional[Union[List[str], str]] = Field(
        None,
        description="The International Standard Serial Number (ISSN) that identifies this serial publication."
     "You can repeat this property to identify different formats of, or the linking ISSN (ISSN-L)"
     "for, this serial publication.",
    )
    variableMeasured: Optional[Union[List[Union[str, PropertyValue]], Union[str, PropertyValue]]] = Field(
        None,
        description="The variableMeasured property can indicate (repeated as necessary) the variables"
     "that are measured in some dataset, either described as text or as pairs of identifier"
     "and description using PropertyValue.",
    )
    locals().update({"@type": Field("Dataset", const=True)})


Dataset.update_forward_refs()
