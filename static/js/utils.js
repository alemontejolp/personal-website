function getDistanceFromTop(elementId) {
  let dist = 0
  let element = document.getElementById(elementId)
  // console.log('offsetTop:', element.offsetTop)
  // console.log('offsetHeight:', element.offsetHeight)
  while(element) {
    // console.log(element)
    // console.log('offsetTop:', element.offsetTop)
    // console.log('offsetHeight:', element.offsetHeight)
    dist += element.offsetTop + element.offsetHeight
    element = element.offsetParent
    // console.log('offsetTop:', element.offsetTop)
    // console.log('offsetHeight:', element.offsetHeight)
  }
  return dist
}

function getDistanceFromParent(elementId) {
  let dist = 0
  let element = document.getElementById(elementId)
  // console.log('offsetTop:', element.offsetTop)
  // console.log('offsetHeight:', element.offsetHeight)
  if(element) {
    dist += element.offsetTop + element.offsetHeight
  } else {
    console.log(`Element "${elementId}" not found.`)
  }
  return dist
}

function setVerticalPosition(elementId, yPosition) {
  let element = document.getElementById(elementId)
  element.style.top = yPosition
}

function placeElementAfterReferenceElement(elementId, referenceElementId, distGetter = getDistanceFromTop) {
  let dist = distGetter(referenceElementId)
  console.log(`elementId: ${elementId}; referenceElementId: ${referenceElementId}; dist: ${dist}`)
  setVerticalPosition(elementId, `${dist}px`)
}

function adjustVerticalPositionAfertWindowsResize(elementId, referenceElementId, distGetter = getDistanceFromTop) {
  placeElementAfterReferenceElement(elementId, referenceElementId, distGetter = distGetter)
  window.addEventListener('resize', () => {
    placeElementAfterReferenceElement(elementId, referenceElementId, distGetter = distGetter)
  })
}
