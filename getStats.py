from urllib.request import urlopen
import os


def fetch_and_clean_html(url: str, filename: str = "stat.html") -> str:

    # get the updated html file from the website

    with urlopen(url) as response:
        html = response.read().decode("utf-8")

    # save raw html to file

    script_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(script_dir, filename)

    with open(file_path, "w", encoding="utf-8") as f:
        f.write(html)

    # all points to remove

    removal_steps = [
        {"key": "<!-- HeaderSportsTeamSchema -->", "end": None, "keep": "after"},
        {"key": "<!-- HeaderSportsEventSchema -->", "end": "sr_menus_setupMainNav_button_inline();", "keep": "outside"},
        {"key": "// see sr.menus.js:sr_menus_checkInfoCookie to explain", "end": "<!-- /div.#fs_fs_general_header -->", "keep": "outside"},
        {"key": "    <p><strong>Governing Country:</strong>", "end": "<!-- fs_btf_1 -->", "keep": "outside"},
        {"key": ' 		<div class="footer no_hide_long" id="tfooter_stats_misc_9">', "end": None, "keep": "before"},
    ]

    # run through cleanup steps

    for step in removal_steps:
        with open(file_path, "r", encoding="utf-8") as f:
            lines = f.readlines()

        key_match = next((i for i, line in enumerate(lines) if step["key"] in line), None)
        end_match = (
            next((i for i, line in enumerate(lines) if step["end"] in line), None)
            if step["end"]
            else None
        )

        if key_match is not None:
            if step["keep"] == "after":
                lines_to_keep = lines[key_match:]
            elif step["keep"] == "before":
                lines_to_keep = lines[:key_match]
            elif step["keep"] == "outside" and end_match is not None:
                lines_to_keep = lines[:key_match] + lines[end_match:]
            else:
                continue

            with open(file_path, "w", encoding="utf-8") as f:
                f.writelines(lines_to_keep)

    return file_path



        