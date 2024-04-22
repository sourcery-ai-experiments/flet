import 'package:flutter/material.dart';

import '../flet_control_backend.dart';
import '../models/control.dart';
import 'error.dart';
import 'flet_store_mixin.dart';

class PlatformMenuBarControl extends StatefulWidget {
  final Control? parent;
  final Control control;
  final List<Control> children;
  final bool parentDisabled;
  final FletControlBackend backend;

  const PlatformMenuBarControl(
      {super.key,
      this.parent,
      required this.control,
      required this.children,
      required this.parentDisabled,
      required this.backend});

  @override
  State<PlatformMenuBarControl> createState() => _PlatformMenuBarControlState();
}

class _PlatformMenuBarControlState extends State<PlatformMenuBarControl>
    with FletStoreMixin {
  @override
  Widget build(BuildContext context) {
    debugPrint("PlatformMenuBar build: ${widget.control.id}");
    bool disabled = widget.control.isDisabled || widget.parentDisabled;

    return withControls(widget.control.childIds, (context, menusView) {
      debugPrint(
          "PlatformMenuBarControlState menusView build: ${widget.control.id}");

      var menus = menusView.controlViews
          .map((v) => v.control)
          .where((c) => c.isVisible)
          .map<PlatformMenuItem>((Control menuCtrl) {
        return PlatformMenu(
          label: menuCtrl.attrs["label"] ?? "Placeholder Label",
          menus: [],
        );
      }).toList();

      if (menus.isEmpty) {
        return const ErrorControl(
          "PlatformMenuBar must have at least one child control of type PlatformMenu.",
        );
      }

      PlatformMenuBar menuBar = PlatformMenuBar(
        menus: menus,
      );

      return menuBar;
    });
  }
}
