# Artwork and portrait sources

All four 5:1 banners are new compositions made with OpenAI's built-in image-generation tool. They use the approved G2 headline and its companion banners as references for the green-and-ivory identity.

The headline in `assets/01-headline-5x1.png` retains the AI-to-family-tree direction and the six historical portrait references. Its portraits are generated treatments of those references, not unaltered archival scans.

The family connections are illustrative. These six sitters are not presented as a documented family. Catalogue titles may identify the person who ordered the photograph rather than the sitter.

Photographs are from the C. M. Bell Studio Collection, Library of Congress, and appear in the Library's [Free to Use and Reuse portrait set](https://www.loc.gov/free-to-use/portrait-photos-19th-century/). The Library describes the set as having no known copyright restrictions. The [collection article](https://blogs.loc.gov/picturethis/2017/04/c-m-bell-studio-collection-newly-digitized-portraits/) and [reuse statement](https://blogs.loc.gov/loc/2017/06/free-to-use-and-reuse-19th-century-portrait-photos/) are the supplied sources for that description.

| Portrait reference in the original design | Catalogue title | Record |
| --- | --- | --- |
| Large, top | Heffner, Mrs. T.M. | [07065](https://www.loc.gov/resource/bellcm.07065/) |
| Large, bottom | Lewis, Mrs. E.B. | [13407](https://www.loc.gov/resource/bellcm.13407/) |
| Final column, first | C.M. Bell | [23682](https://www.loc.gov/resource/bellcm.23682/) |
| Final column, second | Flagg, Mrs. C.A. | [11893](https://www.loc.gov/resource/bellcm.11893/) |
| Final column, third | Herbert, B.F. | [18374](https://www.loc.gov/resource/bellcm.18374/) |
| Final column, fourth | Holly, Rev. J.S. | [11660](https://www.loc.gov/resource/bellcm.11660/) |

Suggested credit: “Portrait references: C. M. Bell Studio Collection, Library of Congress. Artwork and portrait treatments generated with AI. Connections are illustrative.”

## Companion banners

The three companion banners were made with OpenAI's image-generation tool, using the approved headline as a style reference. The documents and newspaper pages are illustrations, not records offered as evidence. Their printed and handwritten text is decorative.

`assets/03-newspapers-5x1.png` uses generated treatments of two archival portrait references: [07065](https://www.loc.gov/resource/bellcm.07065/) and [18374](https://www.loc.gov/resource/bellcm.18374/). These are not unaltered photographs, authentic newspaper clippings or a claim that the sitters were related.

`assets/04-free-sources-5x1.png` depicts a folder of records and a trial-planning calendar. It makes no promise of unlimited free access or a particular trial duration. Provider terms and collection coverage should be checked before publication.

The original 3:1 artwork remains in Git history. For the 5:1 edition, new compositions were generated within a central band on a padded canvas, then exported by removing the blank space above and below. The source canvases and prompts are in `artwork/`; `scripts/export_banners.sh` reproduces the exports. The page displays each complete 5:1 PNG without clipping or distortion.
