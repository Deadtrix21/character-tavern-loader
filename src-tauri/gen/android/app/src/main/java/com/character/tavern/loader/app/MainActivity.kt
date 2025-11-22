package com.character.tavern.loader.app
import android.os.Bundle
import androidx.activity.enableEdgeToEdge
import android.os.Build
import android.view.View
import android.view.WindowInsets

class MainActivity : TauriActivity() {
  override fun onCreate(savedInstanceState: Bundle?) {
    enableEdgeToEdge()
    super.onCreate(savedInstanceState)
    if (Build.VERSION.SDK_INT >= Build.VERSION_CODES.KITKAT_WATCH) {
      window.decorView.setOnApplyWindowInsetsListener { v, insets ->
        v.setPadding(
          insets.systemWindowInsetLeft,
          insets.systemWindowInsetTop,
          insets.systemWindowInsetRight,
          insets.systemWindowInsetBottom
        )
        insets.consumeSystemWindowInsets()
      }
    }
  }
}