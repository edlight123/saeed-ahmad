# Saeed Ahmad – Modern Portfolio (Static)

This repo contains a modern, fast, and accessible static website template tailored for a personal portfolio (inspired by saeed-ahmad.com) without copying any copyrighted content.

## What's inside

- No build tools required — just open `site/index.html`.
- Responsive layout, dark mode, and subtle animations.
- Sections: Hero, About, Experience, Projects, Publications, Contact.
- Accessible navigation with skip link and scroll spy.
- SEO basics + Person schema.

## Customize content

You can edit `site/index.html` directly, or use `site/content.json` to keep content separate and easily reusable. If `content.json` exists, the page loads it and renders sections dynamically.

- Replace text placeholders (bio, roles, projects, publications, links) in `index.html` or fill them in `content.json`.
- Update social/profile links in the Contact section and in JSON-LD.
- Replace `assets/avatar.svg` with your own avatar/photo if desired.

### Using content.json

Edit `site/content.json` fields:
- hero: name, tagline, location, currently
- about: bio, expertise[], highlights[]
- experience: [{ role, org, start, end, summary, bullets[] }]
- projects: [{ name, tags[], desc, demo, code }]
- publications: [{ title, venue, year, pdf }]
- contact: { email, links: [{ label, url }], cv }

## Run locally

You can open the file directly in a browser, or serve it with a tiny web server for best results.

```bash
# Serve the site at http://localhost:8000
python3 -m http.server -d site 8000
```

## Deploy

- GitHub Pages: push this repo, then enable Pages from the `site/` folder in repository settings.
- Any static host (Netlify, Vercel, Cloudflare Pages) can deploy `site/` as-is.

## Content rights note

If you own the rights to the content at https://saeed-ahmad.com/, you can paste it into the placeholders here. Otherwise, please provide your own text and images.