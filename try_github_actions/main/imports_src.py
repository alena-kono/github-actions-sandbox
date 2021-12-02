"""Here are some sample types that are supposed to be imported."""


from typing import Dict, List, Union

Url = str
Urls = List[str]

ResponseStatus = int
UrlStatus = Dict[Url, ResponseStatus]
TimeoutSec = Union[int, float]
