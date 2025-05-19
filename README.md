<h1 align="center">Padzanij Web</h1>


---


Padzanij Web is the frontend used for most of the clients available for end users, such as desktop browsers, Android, and iOS.

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

