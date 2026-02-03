#!/usr/bin/env python3
import markdown
import os
import pandas as pd
import json
import argparse
from jinja2 import Environment, FileSystemLoader

# Load configuration
with open('config.json', 'r') as f:
    config = json.load(f)

# Setup Jinja2
env = Environment(loader=FileSystemLoader('src/templates'))
template = env.get_template('base.html')

def convert_md_to_html(md_file, html_file):
    with open(md_file, 'r') as f:
        md_content = f.read()
    html_content = markdown.markdown(md_content, extensions=['tables'])
    
    # Render template
    output = template.render(
        title=os.path.basename(md_file).replace('.md', '').replace('_', ' ').title(),
        content=html_content,
        config=config
    )
    
    with open(html_file, 'w') as f:
        f.write(output)

def create_itinerary_html(output_dir):
    xl = pd.ExcelFile('content/Guatemala.xlsx')
    sheets = xl.sheet_names  # ['South first', 'North first']
    
    def sheet_to_html(sheet_name):
        df = pd.read_excel(xl, sheet_name=sheet_name)
        df = df.dropna(subset=['Day'])
        return df.to_html(index=False, classes='table table-striped')
    
    south_html = sheet_to_html('South first')
    north_html = sheet_to_html('North first')
    
    content = f"""
    <h1>🇬🇹 Guatemala Itineraries</h1>
    <p>Detailed day-by-day itineraries with budget breakdowns. Choose your preferred route:</p>
    
    <div class="tab">
        <button class="tablinks active" onclick="openTab(event, 'South')">South First Itinerary</button>
        <button class="tablinks" onclick="openTab(event, 'North')">North First Itinerary</button>
    </div>

    <div id="South" class="tabcontent" style="display: block;">
        <h2>🧙‍♂️ South First Itinerary</h2>
        {south_html}
    </div>

    <div id="North" class="tabcontent">
        <h2>🧙‍♀️ North First Itinerary</h2>
        {north_html}
    </div>

    <p><a href="Guatemala.xlsx" download>Download the full Excel file</a></p>

    <p><a href="south_first_itinerary.html">📖 Read the South First Itinerary Narration</a></p>

    <script>
        function openTab(evt, tabName) {{
            var i, tabcontent, tablinks;
            tabcontent = document.getElementsByClassName("tabcontent");
            for (i = 0; i < tabcontent.length; i++) {{
                tabcontent[i].style.display = "none";
            }}
            tablinks = document.getElementsByClassName("tablinks");
            for (i = 0; i < tablinks.length; i++) {{
                tablinks[i].className = tablinks[i].className.replace(" active", "");
            }}
            document.getElementById(tabName).style.display = "block";
            evt.currentTarget.className += " active";
        }}
    </script>
    """
    
    output = template.render(
        title="Guatemala Itineraries",
        content=content,
        config=config
    )
    
    with open(os.path.join(output_dir, 'itinerary.html'), 'w') as f:
        f.write(output)

# Convert the files
def main(output_dir):
    os.makedirs(output_dir, exist_ok=True)
    convert_md_to_html('content/lodging.md', os.path.join(output_dir, 'lodging.html'))
    convert_md_to_html('content/south_first_itinerary.md', os.path.join(output_dir, 'south_first_itinerary.html'))  # Rename to avoid conflict
    create_itinerary_html(output_dir)
    
    # Copy the Excel file for download and the index html to output directory
    import shutil
    shutil.copy('content/Guatemala.xlsx', os.path.join(output_dir, 'Guatemala.xlsx'))
    shutil.copy('content/index.html', os.path.join(output_dir, 'index.html'))

    print(f"HTML files generated successfully and saved to '{output_dir}'!")


def entrypoint():
    parser = argparse.ArgumentParser(description='Convert Markdown and Excel files to HTML.')
    parser.add_argument('-o', '--output-dir', default='dist', help='Output directory for generated files (default: "dist")')
    args = parser.parse_args()
    output_dir = args.output_dir
    main(output_dir)
    

if __name__ == "__main__":
    entrypoint()
    