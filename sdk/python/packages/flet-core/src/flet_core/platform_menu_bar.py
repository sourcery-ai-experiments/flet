from typing import Any, List, Optional, Union

from flet_core.control import Control, OptionalNumber
from flet_core.ref import Ref
from flet_core.types import (
    ResponsiveNumber,
)


class PlatformMenuItem(Control):
    """
    TBA

    -----

    Online docs: https://flet.dev/docs/controls/platformmenuitem
    """

    def __init__(
        self,
        label: str,
        on_select=None,
        #
        # Control
        #
        ref: Optional[Ref] = None,
        visible: Optional[bool] = None,
        disabled: Optional[bool] = None,
        data: Any = None,
    ):
        Control.__init__(
            self,
            ref=ref,
            visible=visible,
            disabled=disabled,
            data=data,
        )

        self.label = label
        self.on_select = on_select

    def _get_control_name(self):
        return "platformmenuitem"

    # label
    @property
    def label(self) -> str:
        return self._get_attr("label")

    @label.setter
    def label(self, value: str):
        self._set_attr("label", value)

    # on_select
    @property
    def on_select(self):
        return self._get_event_handler("select")

    @on_select.setter
    def on_select(self, handler):
        self._add_event_handler("select", handler)


class PlatformMenu(Control):
    """
    TBA

    -----

    Online docs: https://flet.dev/docs/controls/platformmenu
    """

    def __init__(
        self,
        label: str,
        menus: List[PlatformMenuItem],
        #
        # Control
        #
        ref: Optional[Ref] = None,
        visible: Optional[bool] = None,
        disabled: Optional[bool] = None,
        data: Any = None,
    ):
        Control.__init__(
            self,
            ref=ref,
            visible=visible,
            disabled=disabled,
            data=data,
        )

        self.label = label
        self.menus = menus

    def _get_control_name(self):
        return "platformmenu"

    def _get_children(self):
        children = list(filter(lambda x: isinstance(x, PlatformMenuItem), self.__menus))
        return children

    # label
    @property
    def label(self) -> str:
        return self._get_attr("label")

    @label.setter
    def label(self, value: str):
        self._set_attr("label", value)

    # menus
    @property
    def menus(self) -> List[PlatformMenuItem]:
        return self.__menus

    @menus.setter
    def menus(self, value: List[PlatformMenuItem]):
        self.__menus = value or []


class PlatformMenuBar(Control):
    """
    TBA

    -----

    Online docs: https://flet.dev/docs/controls/platformmenubar
    """

    def __init__(
        self,
        controls: List[PlatformMenu] = None,
        #
        # Control
        #
        ref: Optional[Ref] = None,
        expand: Union[None, bool, int] = None,
        expand_loose: Optional[bool] = None,
        col: Optional[ResponsiveNumber] = None,
        opacity: OptionalNumber = None,
        visible: Optional[bool] = None,
        disabled: Optional[bool] = None,
        data: Any = None,
    ):
        Control.__init__(
            self,
            ref=ref,
            expand=expand,
            expand_loose=expand_loose,
            col=col,
            opacity=opacity,
            visible=visible,
            disabled=disabled,
            data=data,
        )

        self.__controls: List[PlatformMenu] = []
        self.controls = controls

    def _get_control_name(self):
        return "platformmenubar"

    def before_update(self):
        super().before_update()

    def _get_children(self):
        children = list(filter(lambda x: isinstance(x, PlatformMenu), self.__controls))
        return children

    # controls
    @property
    def controls(self) -> List[PlatformMenu]:
        return self.__controls

    @controls.setter
    def controls(self, value: List[PlatformMenu]):
        self.__controls = value or []
