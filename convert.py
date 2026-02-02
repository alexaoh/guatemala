#!/usr/bin/env python3
import markdown
import os
import pandas as pd

def convert_md_to_html(md_file, html_file):
    with open(md_file, 'r') as f:
        md_content = f.read()
    html_content = markdown.markdown(md_content, extensions=['tables'])
    with open(html_file, 'w') as f:
        f.write(f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>South First Itinerary Narration</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Roboto:wght@300;400&display=swap');
        body {{ 
            font-family: 'Roboto', sans-serif; 
            margin: 40px; 
            line-height: 1.6; 
            background-color: #f5f5dc; 
            color: #2e2e2e;
        }}
        h1, h2, h3 {{ 
            font-family: 'Cinzel', serif; 
            color: #8b0000; 
        }}
        table {{ 
            border-collapse: collapse; 
            width: 100%; 
            background-color: #fffaf0; 
            border: 2px solid #daa520; 
            margin: 20px 0;
            box-shadow: 0 2px 4px rgba(0,0,0,0.1);
        }}
        th, td {{ 
            border: 1px solid #daa520; 
            padding: 12px; 
            text-align: left; 
            vertical-align: top;
        }}
        th {{ 
            background-color: #daa520; 
            color: #8b0000; 
            font-weight: bold;
            text-transform: uppercase;
            font-size: 0.9em;
        }}
        tr:nth-child(even) {{ background-color: #f9f6f0; }}
        tr:hover {{ background-color: #f0e68c; }}
        a {{ 
            color: #1e90ff; 
            text-decoration: none; 
        }}
        a:hover {{ 
            text-decoration: underline; 
            color: #000080; 
        }}
        nav {{ 
            background-color: #daa520; 
            padding: 10px; 
            border-radius: 5px; 
            margin-bottom: 20px;
        }}
        nav a {{ 
            color: #8b0000; 
            margin: 0 10px; 
            font-weight: bold;
        }}
    </style>
</head>
<body>
    <nav>
        <a href="index.html">Home</a> | 
        <a href="lodging.html">Lodging</a> | 
        <a href="itinerary.html">Itineraries</a> |
        <a href="south_first_itinerary.html">South First Itinerary Narration</a>
    </nav>
    <hr>
    {html_content}
</body>
</html>""")

def create_itinerary_html():
    xl = pd.ExcelFile('Guatemala.xlsx')
    sheets = xl.sheet_names  # ['South first', 'North first']
    
    def sheet_to_html(sheet_name):
        df = pd.read_excel(xl, sheet_name=sheet_name)
        df = df.dropna(subset=['Day'])
        return df.to_html(index=False, classes='table table-striped')
    
    south_html = sheet_to_html('South first')
    north_html = sheet_to_html('North first')
    
    html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Guatemala Itineraries</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Cinzel:wght@400;700&family=Roboto:wght@300;400&display=swap');
        body {{ font-family: 'Roboto', sans-serif; margin: 40px; line-height: 1.6; background-color: #f5f5dc; color: #2e2e2e; }}
        h1, h2, h3 {{ font-family: 'Cinzel', serif; color: #8b0000; }}
        table {{ border-collapse: collapse; width: 100%; background-color: #fffaf0; border: 2px solid #daa520; margin: 20px 0; box-shadow: 0 2px 4px rgba(0,0,0,0.1); }}
        th, td {{ border: 1px solid #daa520; padding: 12px; text-align: left; vertical-align: top; }}
        th {{ background-color: #daa520; color: #8b0000; font-weight: bold; text-transform: uppercase; font-size: 0.9em; }}
        tr:nth-child(even) {{ background-color: #f9f6f0; }}
        tr:hover {{ background-color: #f0e68c; }}
        a {{ color: #1e90ff; text-decoration: none; }}
        a:hover {{ text-decoration: underline; color: #000080; }}
        .tab {{ overflow: hidden; border: 1px solid #daa520; background-color: #daa520; }}
        .tab button {{ background-color: inherit; float: left; border: none; outline: none; cursor: pointer; padding: 14px 16px; transition: 0.3s; color: #8b0000; font-weight: bold; }}
        .tab button:hover {{ background-color: #ffd700; }}
        .tab button.active {{ background-color: #ffd700; }}
        .tabcontent {{ display: none; padding: 6px 12px; border: 1px solid #daa520; border-top: none; background-color: #fffaf0; }}
        nav {{ background-color: #daa520; padding: 10px; border-radius: 5px; margin-bottom: 20px; }}
        nav a {{ color: #8b0000; margin: 0 10px; font-weight: bold; }}
    </style>
</head>
<body>
    <nav>
        <a href="index.html">Home</a> | 
        <a href="lodging.html">Lodging</a> | 
        <a href="itinerary.html">Itineraries</a> |
        <a href="south_first_itinerary.html">South First Itinerary Narration</a>
    </nav>
    <hr>
    <h1>🇬🇹 Guatemala Itineraries</h1>
    <p>Detailed day-by-day itineraries with budget breakdowns. Choose your preferred route:</p>
    
    <div class="tab">
        <button class="tablinks active" onclick="openTab(event, 'South')">South First Itinerary</button>
        <button class="tablinks" onclick="openTab(event, 'North')">North First Itinerary</button>
    </div>

    <div id="South" class="tabcontent" style="display: block;">
        <h2>South First Itinerary</h2>
        {south_html}
    </div>

    <div id="North" class="tabcontent">
        <h2>North First Itinerary</h2>
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
</body>
</html>"""
    with open('itinerary.html', 'w') as f:
        f.write(html_content)

# Convert the files
convert_md_to_html('lodging.md', 'lodging.html')
convert_md_to_html('south_first_itinerary.md', 'south_first_itinerary.html')
create_itinerary_html()

print("HTML files generated successfully!")