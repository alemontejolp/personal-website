window.addEventListener('load', () => {
  // When the window got resized, replace the main containser
  // with respect to the global nav.
  adjustVerticalPositionAfertWindowsResize('navbar-example2', 'global-nav')
  adjustVerticalPositionAfertWindowsResize('aboutme-content', 'navbar-example2')
})
