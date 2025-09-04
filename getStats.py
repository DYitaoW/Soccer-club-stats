from urllib.request import urlopen
import os

url = "https://fbref.com/en/squads/cff3d9bb/Chelsea-Stats"


# get the updated html file from the website

with urlopen(url) as response:
    html = response.read().decode("utf-8")

script_dir = os.path.dirname(os.path.abspath(__file__))
file_path = os.path.join(script_dir, "stat.html")

with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)

# remove irrelevent data on the html file

key = "<!-- HeaderSportsTeamSchema -->"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines() 

key_match = next((i for i, line in enumerate(lines) if key in line), None)

if key_match is not None:
    lines_to_remove = lines[key_match:]
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(lines_to_remove)

key = "<!-- HeaderSportsEventSchema -->"
end_key = "sr_menus_setupMainNav_button_inline();"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines() 

key_match = next((i for i, line in enumerate(lines) if key in line), None)
end_key_match = next((i for i, line in enumerate(lines) if end_key in line), None)

if key_match & end_key_match is not None:
    lines_to_remove = lines[:key_match] + lines[end_key_match:]
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(lines_to_remove)

key = "// see sr.menus.js:sr_menus_checkInfoCookie to explain"
end_key = "<!-- /div.#fs_fs_general_header -->"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines() 

key_match = next((i for i, line in enumerate(lines) if key in line), None)
end_key_match = next((i for i, line in enumerate(lines) if end_key in line), None)

if key_match & end_key_match is not None:
    lines_to_remove = lines[:key_match] + lines[end_key_match:]
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(lines_to_remove)

key = "    <p><strong>Governing Country:</strong>"
end_key = "<!-- fs_btf_1 -->"

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines() 

key_match = next((i for i, line in enumerate(lines) if key in line), None)
end_key_match = next((i for i, line in enumerate(lines) if end_key in line), None)

if key_match & end_key_match is not None:
    lines_to_remove = lines[:key_match] + lines[end_key_match:]
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(lines_to_remove)

key = ' 		<div class="footer no_hide_long" id="tfooter_stats_misc_9">'

with open(file_path, "r", encoding="utf-8") as f:
    lines = f.readlines() 

key_match = next((i for i, line in enumerate(lines) if key in line), None)

if key_match is not None:
    lines_to_remove = lines[:key_match]
    
    with open(file_path, "w", encoding="utf-8") as f:
        f.writelines(lines_to_remove)



        