<h1 align="center">Padzanij Web</h1>
<h3 align="center">Part of the <a href="https://padzanij.org">Padzanij Project</a></h3>

---

<p align="center">
<img alt="Logo Banner" src="https://raw.githubusercontent.com/padzanij/padzanij-ux/master/branding/SVG/banner-logo-solid.svg?sanitize=true"/>
<br/>
<br/>
<a href="https://github.com/padzanij/padzanij-web">
<img alt="GPL 2.0 License" src="https://img.shields.io/github/license/padzanij/padzanij-web.svg"/>
</a>
<a href="https://github.com/padzanij/padzanij-web/releases">
<img alt="Current Release" src="https://img.shields.io/github/release/padzanij/padzanij-web.svg"/>
</a>
<a href="https://translate.padzanij.org/projects/padzanij/padzanij-web/?utm_source=widget">
<img src="https://translate.padzanij.org/widgets/padzanij/-/padzanij-web/svg-badge.svg" alt="Translation Status"/>
</a>
<br/>
<a href="https://opencollective.com/padzanij">
<img alt="Donate" src="https://img.shields.io/opencollective/all/padzanij.svg?label=backers"/>
</a>
<a href="https://features.padzanij.org">
<img alt="Feature Requests" src="https://img.shields.io/badge/fider-vote%20on%20features-success.svg"/>
</a>
<a href="https://matrix.to/#/+padzanij:matrix.org">
<img alt="Chat on Matrix" src="https://img.shields.io/matrix/padzanij:matrix.org.svg?logo=matrix"/>
</a>
<a href="https://www.reddit.com/r/padzanij">
<img alt="Join our Subreddit" src="https://img.shields.io/badge/reddit-r%2Fpadzanij-%23FF5700.svg"/>
</a>
</p>

Padzanij Web is the frontend used for most of the clients available for end users, such as desktop browsers, Android, and iOS. We welcome all contributions and pull requests! If you have a larger feature in mind please open an issue so we can discuss the implementation before you start. Translations can be improved very easily from our <a href="https://translate.padzanij.org/projects/padzanij/padzanij-web">Weblate</a> instance. Look through the following graphic to see if your native language could use some work!

<a href="https://translate.padzanij.org/engage/padzanij/?utm_source=widget">
<img src="https://translate.padzanij.org/widgets/padzanij/-/padzanij-web/multi-auto.svg" alt="Detailed Translation Status"/>
</a>

## Build Process

### Dependencies

- [Node.js](https://nodejs.org/en/download)
- npm (included in Node.js)

### Getting Started

1. Clone or download this repository.

   ```sh
   git clone https://github.com/padzanij/padzanij-web.git
   cd padzanij-web
   ```

2. Install build dependencies in the project directory.

   ```sh
   npm install
   ```

3. Run the web client with webpack for local development.

   ```sh
   npm start
   ```

4. Build the client with sourcemaps available.

   ```sh
   npm run build:development
   ```

## Directory Structure

> [!NOTE]
> We are in the process of refactoring to a [new structure](https://forum.padzanij.org/t-proposed-update-to-the-structure-of-padzanij-web) based on [Bulletproof React](https://github.com/alan2207/bulletproof-react/blob/master/docs/project-structure.md) architecture guidelines.
> Most new code should be organized under the appropriate app directory unless it is common/shared.

```
.
└── src
    ├── apps
    │   ├── dashboard           # Admin dashboard app
    │   ├── experimental        # New experimental app
    │   ├── stable              # Classic (stable) app
    │   └── wizard              # Startup wizard app
    ├── assets                  # Static assets
    ├── components              # Higher order visual components and React components
    ├── constants               # Common constant values
    ├── controllers             # Legacy page views and controllers 🧹 ❌
    ├── elements                # Basic webcomponents and React equivalents 🧹
    ├── hooks                   # Custom React hooks
    ├── lib                     # Reusable libraries
    │   ├── globalize           # Custom localization library
    │   ├── padzanij-apiclient  # Supporting code for the deprecated apiclient package
    │   ├── legacy              # Polyfills for legacy browsers
    │   ├── navdrawer           # Navigation drawer library for classic layout
    │   └── scroller            # Content scrolling library
    ├── plugins                 # Client plugins (features dynamically loaded at runtime)
    ├── scripts                 # Random assortment of visual components and utilities 🐉 ❌
    ├── strings                 # Translation files (only commit changes to en-us.json)
    ├── styles                  # Common app Sass stylesheets
    ├── themes                  # Sass and MUI themes
    ├── types                   # Common TypeScript interfaces/types
    └── utils                   # Utility functions
```

- ❌ &mdash; Deprecated, do **not** create new files here
- 🧹 &mdash; Needs cleanup
- 🐉 &mdash; Serious mess (Here be dragons)
