# HLS Playlist Sequence Checker

This script helps diagnose **broadcast streaming issues** by checking the **media sequence numbers** of variant playlists in an HLS (HTTP Live Streaming) master playlist.  

In broadcast/VNOC operations, out-of-sync or mismatched sequence numbers can cause playback issues such as black frames, stutters, or missing segments. This tool quickly extracts each sub-playlist (variant) from a master URL and reports its `#EXT-X-MEDIA-SEQUENCE` value.

---

## Features
- Fetches an **HLS master playlist**.
- Extracts **variant playlist URLs**.
- Retrieves the **`#EXT-X-MEDIA-SEQUENCE`** tag from each variant.
- Prints results for quick comparison across variants.

---

## Example Output
Master playlist: https://example.com/stream/master.m3u8

Checking variants...
- https://example.com/stream/480p.m3u8  ->  MEDIA-SEQUENCE: 10423
- https://example.com/stream/720p.m3u8  ->  MEDIA-SEQUENCE: 10423
- https://example.com/stream/1080p.m3u8 ->  MEDIA-SEQUENCE: 10423


## If a mismatch is found:

- https://example.com/stream/480p.m3u8  ->  MEDIA-SEQUENCE: 10423
- https://example.com/stream/720p.m3u8  ->  MEDIA-SEQUENCE: 10425   **mismatch**

---

## 1 Dependency needed
- pip install requests
