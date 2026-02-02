Current setup is functional but "homemade". Migrating to a standardized framework like Eleventy (11ty.dev) would make it much more maintainable, extensible, and professional. 11ty is excellent for static sites with Markdown, and it handles templating, layouts, and plugins out of the box.

## Option 1: Migrate to Eleventy (Recommended for Standardization)

Eleventy can process your Markdown files, apply consistent layouts/themes, and even handle data files. Can be set up like:

### Step-by-Step Migration:

1. **Install Node.js** (if not already installed):
   ```bash
   # On macOS
   brew install node
   ```

2. **Initialize 11ty**:
   ```bash
   npm init -y
   npm install @11ty/eleventy
   ```

3. **Create 11ty Config** (`.eleventy.js`):
   ```javascript
   module.exports = function(eleventyConfig) {
     // Copy static files
     eleventyConfig.addPassthroughCopy("*.html"); // For your existing HTML if needed
     
     // Watch for changes
     eleventyConfig.addWatchTarget("./src/");
     
     return {
       dir: {
         input: "src",
         output: "_site"
       }
     };
   };
   ```

4. **Restructure Files**:
   ```
   src/
   ├── _includes/
   │   ├── layouts/
   │   │   └── base.njk  # Your Harry Potter theme layout
   │   └── partials/
   ├── pages/
   │   ├── index.md
   │   ├── lodging.md
   │   └── south_first_itinerary.md
   └── _data/
       └── site.json  # Global config
   ```

5. **Create Base Layout** (`src/_includes/layouts/base.njk`):
   ```html
   <!DOCTYPE html>
   <html lang="en">
   <head>
     <meta charset="UTF-8">
     <title>{{ title }}</title>
     <style>
       /* Your Harry Potter CSS here */
       body { font-family: 'Cinzel', serif; background: #f5f5dc; }
       /* ... rest of your theme ... */
     </style>
   </head>
   <body>
     <nav>
       <a href="/">Home</a> | 
       <a href="/lodging/">Lodging</a> | 
       <a href="/itineraries/">Itineraries</a>
     </nav>
     <hr>
     {{ content | safe }}
   </body>
   </html>
   ```

6. **Update Markdown Files** (add frontmatter):
   ```markdown
   ---
   layout: layouts/base.njk
   title: Lodging Options
   ---
   
   # 🇬🇹 Guatemala Accommodation Comparison
   <!-- Your content -->
   ```

7. **Handle Excel Data**: Keep your Python script for Excel processing, or use 11ty's data files.

8. **Build & Serve**:
   ```bash
   npx @11ty/eleventy --serve  # Development server
   npx @11ty/eleventy  # Build for production
   ```

9. **Update GitHub Actions**: Change the build step to run 11ty instead of your Python script.

## HAS BEEN DONE FOR NOW - Option 2: Improve Current Python Script (Less Disruptive)

Make [`convert.py`](convert.py ) more general and modular:

- Use Jinja2 for templates instead of hardcoded HTML
- Separate layout, content, and data processing
- Add configuration files for themes/layouts

This keeps Python but makes it more maintainable.

## Benefits of 11ty:
- **Standardized**: Widely used, active community
- **Flexible**: Markdown, data files, custom plugins
- **Fast**: Incremental builds, great performance
- **Future-proof**: Easy to add features like RSS, sitemaps, etc.
