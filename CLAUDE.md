# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Personal portfolio/link-in-bio site for samuelsan.es built with **Reflex** (Python full-stack framework). Bilingual (Spanish/English), statically exported to React for Vercel hosting. No backend server — `enable_state=False`.

## Commands

```bash
# Development
reflex run                          # Start dev server at localhost:3000

# Production build
reflex export --frontend-only       # Export static frontend to frontend.zip
unzip frontend.zip -d public        # Extract for Vercel deployment

# Dependencies
pip install -r requirements.txt     # Python deps (reflex, deep-translator)
```

## Architecture

**Entry point:** `link_bio/link_bio.py` — defines two routes (`/` Spanish, `/en` English) using the same `_page(lang)` composition function.

**Component hierarchy:**
```
_page(lang) → rx.fragment
  ├── rx.script (manifest.json)
  └── rx.box
      ├── navbar(lang)          # Logo + language selector
      ├── rx.center
      │   └── header(lang)      # Avatar, name, stats, bio
      │       links(lang)       # Social links + Medium publications
      └── footer(lang)
```

**Key directories:**
- `link_bio/components/` — Reusable UI components (navbar, footer, card, link_button, etc.)
- `link_bio/views/` — Page sections (header, links)
- `link_bio/services/` — Language service (JSON i18n + Google Translate), publication service (Medium RSS via rss2json API)
- `link_bio/styles/` — Centralized styling: `styles.py` (sizes, responsive breakpoints), `colors.py` (dark theme palette), `fonts.py`
- `assets/language/` — Translation files (`es.json`, `en.json`)

**Styling system:** Uses `Enum` classes for `Size`/`SizeReflex`, preset style dicts, and `rx.breakpoints()` for responsive design. Tailwind is disabled. Max-width container: 650px.

## Key Patterns

- All components accept `lang: str` parameter for i18n
- Translations: `language_service.t(key, lang)` reads from JSON files, falls back to Google Translate
- Publications fetched at build time from Medium RSS feed (`publication_service.py`)
- Conditional rendering with `rx.cond()` (e.g., show publications only if available)
- SEO metadata defined in `@rx.page()` decorators (meta, Open Graph, Twitter Cards)

## Configuration

- `rxconfig.py` — Reflex config with `SitemapPlugin`, no Tailwind, no state
- `vercel.json` — Security headers + aggressive static asset caching (1 year)
- `.github/workflows/deploy.yml` — CI/CD: export → disable WebSocket in JS → deploy to Vercel

## Reflex 0.8.26 Compatibility Notes

- `rx.head()` and `rx.html()` no longer exist — use `rx.script()` directly in components
- `script_tags` parameter removed from `@rx.page()` — place scripts inside component tree
- `bun_path` in config must be a `Path` object, not a string with `$HOME`
- `SitemapPlugin` must be explicitly added to `plugins` list (no longer auto-enabled silently)
