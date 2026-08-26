# archive

Superseded documents. Nothing here is current — kept only so the older revision
is recoverable without digging through git history.

| File | Superseded by | Why |
|---|---|---|
| `marketing/Klyara_Day_By_Day_90_Day_Plan.md` | `marketing/Klyara_Day_By_Day_90_Days.md` | Same document, earlier revision. Identical headings; the newer file adds a section titled "Added since this plan was first written" and is 2,305 bytes longer. |
| `build/Klyara_Build_Manual_v3_2.md` | `build/Klyara_Build_Manual_v3_3.md` | Byte-identical (MD5 `E17B27EF…`). The same content was saved twice in the source project under two version names — "v3.3" is not a newer revision of "v3.2". |

## What was *not* archived, and why

**The markdown documents in `marketing/` do overlap with the PDFs and DOCX in
`assets/docs/`** — 23 of the 24 have a published counterpart, for example
`marketing/Klyara_Sales_Pack.md` and `assets/docs/08_Marketing_and_Ops/09_sales_pack.pdf`.
Neither is stale: they are the same documents in source and published form, both
generated on 26 August 2026. Archiving either side would throw away something
current, so both stay.

`assets/docs/` is also load-bearing — 226 paths under it are linked from
`admin.html` and the site's other pages. Moving any of those files breaks those
links, so nothing in `assets/docs/` was touched.

`assets/docs/09_Assets/` was removed: it was an empty folder.
