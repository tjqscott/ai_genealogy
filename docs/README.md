# README layout study

Open `index.html` in a browser. It compares the original 3:1 section banners with shorter 5:1 and 6:1 crops. The approved headline stays at 3:1 throughout.

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

The original images are kept intact in `assets/`. Shorter versions are browser layout crops, not separate image exports. After choosing a ratio, the artwork can be recomposed for the final README.

See [artwork credits](ARTWORK.md) for portrait references and the distinction between archive photographs and generated illustrations.
