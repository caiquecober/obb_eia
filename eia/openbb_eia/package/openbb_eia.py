### THIS FILE IS AUTO-GENERATED. DO NOT EDIT. ###

from openbb_core.app.static.container import Container
from openbb_core.app.model.obbject import OBBject
from typing import List, Union, Optional, Literal
from openbb_core.app.static.utils.decorators import validate

from openbb_core.app.static.utils.filters import filter_inputs


class ROUTER_openbb_eia(Container):
    """/openbb_eia
    eia_historical
    get_test
    """

    def __repr__(self) -> str:
        return self.__doc__ or ""

    @validate
    def eia_historical(
        self, provider: Optional[Literal["openbb_eia"]] = None, **kwargs
    ) -> OBBject:
        """Example Data.

        Parameters
        ----------
        provider : Optional[Literal['openbb_eia']]
            The provider to use for the query, by default None.
            If None, the provider specified in defaults is selected or 'openbb_eia' if there is
            no default.
        series : str
            EIA series identifier. (provider: openbb_eia)

        Returns
        -------
        OBBject
            results : List[EIAHistorical]
                Serializable results.
            provider : Optional[Literal['openbb_eia']]
                Provider name.
            warnings : Optional[List[Warning_]]
                List of warnings.
            chart : Optional[Chart]
                Chart object.
            extra: Dict[str, Any]
                Extra info.

        EIAHistorical
        -------------
        date : Optional[str]
            Date of the data point. (provider: openbb_eia)
        value : Optional[float]
            Value of the data point. (provider: openbb_eia)

        Example
        -------
        >>> from openbb import obb
        >>> obb.openbb_eia.eia_historical()
        """  # noqa: E501

        return self._run(
            "/openbb_eia/eia_historical",
            **filter_inputs(
                provider_choices={
                    "provider": provider,
                },
                standard_params={},
                extra_params=kwargs,
            )
        )

    @validate
    def get_test(self, symbol: Union[str, List[str]] = "AAPL") -> OBBject:
        """Get options data."""  # noqa: E501

        return self._run(
            "/openbb_eia/get_test",
            **filter_inputs(
                symbol=symbol,
            )
        )
