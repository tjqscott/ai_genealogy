# README layout study

[Open the live mock page](https://tjqscott.github.io/ai_genealogy/) or open `index.html` locally in a browser. All four banners, including the headline, have been recomposed and exported at 5:1. The page shows the complete images without CSS crops or a ratio selector.

The text is sample copy to judge the spacing and sequence. This page is not an installable release of the genealogy skill bundle.

## Edit and rebuild

Edit `index.template.html`, then run from the repository root:

```sh
python3 scripts/build_preview.py
python3 scripts/build_preview.py --check
```

The builder uses the Python standard library. A portable version with the four images embedded can be made with:

```sh
python3 scripts/build_preview.py --embed --output preview.html
```

The final PNGs are in `assets/`. The image-generation tool returns a 3:1 canvas, so these new compositions were drawn inside its central 5:1 band. Source canvases and prompts are kept in `artwork/`. To reproduce the exports on macOS, run `bash scripts/export_banners.sh`, then rebuild the page. The exporter uses the system `sips` command to remove the blank margins without stretching the artwork. The builder rejects images whose pixel dimensions are not exactly 5:1.

See [artwork credits](ARTWORK.md) for portrait references and the distinction between archive photographs and generated illustrations.

GitHub Pages currently publishes the `/docs` directory from `docs/readme-layout`, so the draft can be reviewed before merging. After the PR is merged, switch the Pages source to `main` before deleting the branch.
