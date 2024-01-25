### THIS FILE IS AUTO-GENERATED. DO NOT EDIT. ###

from openbb_core.app.static.container import Container


class Extensions(Container):
    # fmt: off
    """
Routers:
    /openbb_eia

Extensions:
    - openbb_eia@1.0.0

    - openbb_eia@1.0.0    """
    # fmt: on

    def __repr__(self) -> str:
        return self.__doc__ or ""

    @property
    def openbb_eia(self):
        # pylint: disable=import-outside-toplevel
        from . import openbb_eia

        return openbb_eia.ROUTER_openbb_eia(command_runner=self._command_runner)
