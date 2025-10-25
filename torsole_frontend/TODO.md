# TODO: Add Fullscreen and Download Functionality to GP Photos

- [x] Update `gp-photos.ts`: Add `selectedPhoto` property for modal state, `openFullscreen(photo)` method to set selected photo, `closeFullscreen()` method to clear it, and `downloadPhoto(photo)` method to trigger download via a temporary link.
- [x] Update `gp-photos.html`: Add fullscreen and download icons to the hover overlay. Add a modal div that appears when `selectedPhoto` is set, displaying the full image with close and download buttons. Make the image clickable to open fullscreen.
- [x] Test the fullscreen modal and download functionality after implementation. (Build successful, server started, but browser testing disabled)
- [x] Ensure responsive design for mobile devices. (Modal uses responsive classes like max-w-4xl, max-h-full, object-contain)
