# shared/mock

Contract sample responses. One JSON file per endpoint, named after it (e.g. `get_risk.json` for `GET /risk`).

- Built in mimari mode from a real data sample, so shapes match reality.
- The backend skeleton serves these until real data is wired in; the response shape must not change after that without both people agreeing.
- The frontend can run from these files alone (static fallback for the demo).
