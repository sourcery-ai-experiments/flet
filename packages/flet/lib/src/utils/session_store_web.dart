import 'package:flutter/foundation.dart';
// ignore: avoid_web_libraries_in_flutter
import 'package:web' as html;

const String _sessionIdKey = "_flet_session_id";

class SessionStore {
  static String? get sessionId {
    return get(_sessionIdKey);
  }

  static set sessionId(String? value) {
    set(_sessionIdKey, value ?? "");
  }

  static String? get(String name) {
    debugPrint("Get session storage $name");
    return html.window.sessionStorage[name];
  }

  static void set(String name, String value) {
    debugPrint("Set session storage $name");
    html.window.sessionStorage[name] = value;
  }
}
