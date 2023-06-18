window.addEventListener('load', () => {
  // When the window got resized, replace the main containser
  // with respect to the global nav.
  adjustVerticalPositionAfertWindowsResize('main-content', 'global-nav')
})
