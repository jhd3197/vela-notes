# Changelog

## Unreleased

### Changed

- Notes fits a phone properly. It fills the space the server gives it instead of
  measuring a viewport unit of its own, so the editor no longer runs under the
  browser's toolbar or an open keyboard, and the server's safe areas and
  keyboard are subtracted once rather than twice. Search and the note title
  render at 16 pixels or more on touch, so tapping them no longer zooms the page
  and leaves it zoomed, while larger text you have chosen is kept. Reaching the
  end of the note list no longer starts moving the page behind it, the delete
  dialog scrolls inside itself on a short screen, and pinch zoom, panning and
  text selection are untouched.
- Notes now opens inside the Vela server's own workspace. The server draws the
  rail and the app's name, and Notes keeps its list, editor and search in the
  same surfaces, spacing and typography as the rest of Vela, following your
  light or dark preference. On a phone the list is the first screen and an
  opened note slides over it with a Back control. Saving, unsaved-work
  protection, conflict recovery and the create-note action are unchanged.

## 1.1.0 - 2026-09-14

### Added

- Private notes with persistent storage and reviewed app actions.
- Independent GitHub downloads, artifact checks and automatic releases after main updates.
- Contributor, security and funding information with shared changelog instructions.
