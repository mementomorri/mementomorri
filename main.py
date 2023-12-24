from datetime import datetime
from zoneinfo import ZoneInfo

import gifos



def main():
    t = gifos.Terminal(750, 500, 15, 15,)
    t.set_fps(15)

    t.gen_text("", 1, count=20)
    t.toggle_show_cursor(False)
    t.gen_text("GIF_OS Modular BIOS v1.0.11", 1)
    t.gen_text("Copyright (C) 2024, \x1b[31mmementomorri Softwares Inc.\x1b[0m", 2)
    t.gen_text("\x1b[94mGitHub Profile ReadMe Terminal, Rev 1011\x1b[0m", 4)
    t.gen_text("mementomorri(me) GIFCPU - 256Hz", 6)
    t.gen_text(
        "Press \x1b[94mF2\x1b[0m to enter SETUP, \x1b[94mESC\x1b[0m to skip Memory Test",
        t.num_rows,
    )
    for i in range(0, 65653*2, 7168):  # 128K Memory
        t.delete_row(7)
        if i < 60000:
            t.gen_text(
                f"Memory Test: {i}", 7, count=2, contin=True
            )  # slow down upto a point
        else:
            t.gen_text(f"Memory Test: {i}", 7, contin=True)
    t.delete_row(7)
    t.gen_text("Memory Test: 128KB OK", 7, count=10, contin=True)
    t.gen_text("", 11, count=10, contin=True)

    t.clear_frame()
    t.gen_text("Initiating Boot Sequence ", 1, contin=True)
    t.gen_typing_text(".....", 1, contin=True)
    t.gen_text("\x1b[96m", 1, count=0, contin=True)  # buffer to be removed
    os_logo_text = "WELCOME..."
    mid_row = (t.num_rows + 1) // 2
    mid_col = (t.num_cols - len(os_logo_text) + 1) // 2
    effect_lines = gifos.effects.text_scramble_effect_lines(
        os_logo_text, 3, include_special=False
    )
    for i in range(len(effect_lines)):
        t.delete_row(mid_row + 1)
        t.gen_text(effect_lines[i], mid_row + 1, mid_col + 1)

    t.clear_frame()
    t.clone_frame(5)
    t.toggle_show_cursor(False)
    t.gen_text("\x1b[93mGIF_OS v1.0.11 (tty1)\x1b[0m", 1, count=5)
    t.gen_text("login: ", 3, count=5)
    t.toggle_show_cursor(True)
    t.gen_typing_text("mementomorri", 3, contin=True)
    t.gen_text("", 4, count=5)
    t.toggle_show_cursor(False)
    t.gen_text("password: ", 4, count=5)
    t.toggle_show_cursor(True)
    t.gen_typing_text("*********", 4, contin=True)
    t.toggle_show_cursor(False)
    time_now = datetime.now(ZoneInfo("Europe/Moscow")).strftime(
        "%a %b %d %I:%M:%S %p %Z %Y"
    )
    t.gen_text(f"Last login: {time_now} on tty1", 6)

    t.gen_prompt(7, count=5)
    prompt_col = t.curr_col
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[91mclea", 7, contin=True)
    t.delete_row(7, prompt_col)  # simulate syntax highlighting
    t.gen_text("\x1b[92mclear\x1b[0m", 7, count=3, contin=True)

    ignore_repos = ["archiso-zfs", "archiso-zfs-archive"]
    git_user_details = gifos.utils.fetch_github_stats("mementomorri", ignore_repos)
    user_age = gifos.utils.calc_age(23, 4, 1998)
    t.clear_frame()
    top_languages = [lang[0] for lang in git_user_details.languages_sorted]
    user_details_lines = f"""
    \x1b[30;101mmementomorri@GitHub\x1b[0m
    --------------
    \x1b[96mOS:     \x1b[93mCentOS/Debian Linux\x1b[0m
    \x1b[96mHost:   \x1b[93mOpen Source Society University
    \x1b[96mKernel: \x1b[93mComputer Science & Engineering
    \x1b[96mUptime: \x1b[93m{user_age.years} years, {user_age.months} months, {user_age.days} days\x1b[0m
    \x1b[96mIDE:    \x1b[93mvim, VSCode, JetBrain\x1b[0m
    
    \x1b[30;101mContact:\x1b[0m
    --------------
    \x1b[96mEmail:      \x1b[93mmementomorimore@gmail.com\x1b[0m
    \x1b[96mTelegram:   \x1b[93mt.me/AlexeyKarsten\x1b[0m
    
    \x1b[30;101mGitHub Stats:\x1b[0m
    --------------
    \x1b[96mUser Rating: \x1b[93m{git_user_details.user_rank.level}\x1b[0m
    \x1b[96mTotal Stars Earned: \x1b[93m{git_user_details.total_stargazers}\x1b[0m
    \x1b[96mTotal Commits (2023): \x1b[93m{git_user_details.total_commits_last_year}\x1b[0m
    \x1b[96mTotal PRs: \x1b[93m{git_user_details.total_pull_requests_made}\x1b[0m
    \x1b[96mMerged PR %: \x1b[93m{git_user_details.pull_requests_merge_percentage}\x1b[0m
    \x1b[96mTotal Contributions: \x1b[93m{git_user_details.total_repo_contributions}\x1b[0m
    \x1b[96mTop Languages: \x1b[93m{', '.join(top_languages[:5])}\x1b[0m
    """
    t.gen_prompt(1)
    prompt_col = t.curr_col
    t.clone_frame(10)
    t.toggle_show_cursor(True)
    t.gen_typing_text("\x1b[91mfetch.s", 1, contin=True)
    t.delete_row(1, prompt_col)
    t.gen_text("\x1b[92mfetch.sh\x1b[0m", 1, contin=True)
    t.gen_typing_text(" -u mementomorri", 1, contin=True)

    t.toggle_show_cursor(False)

    monaLines = r"""
                                             
                                             
                                             
            .         ..          .          
        .        /(((((((((           .      
             ,(((((((((((((((.               
   .  .#,,/((((((((((((((((((((,             
      ###(   ((((((((((((((((((((.           
,          ,(((((((((((((((((((((((          
      @@@@((((((((((((((((((((((((((#@@@@    
      @@@%%%%%%%%%%%%%%%%%%%%%%%%%%%%%@@@.   
      @@%%%%%%%##(((((((((((((##%%%%%%%&@    
   /(((((((((((((((((((((((((((((((((((((((( 
* ./((((((((((((((((((((((((((((((((((((((/*.
      @@@@@   .(@@@@@@@@@@@@@@@&*.   @@@@.   
      @@@@@/       @@@@@@@@@%       @@@@@    
.  (.  @@@@@@@@&&&&&@@@@@@@@&&&&&@@@@@@@(  * 
    .@, @@@@@@@@@@@@@@@/#@@@@@@@@@@@@@@. #&  
   .   @  @@@@@@@@@@@@@@@@@@@@@@@@@@@, (/  . 
             &@@@@@@@@@@@@@@@@@@@@,          
        .         .#&@@@@@@%,         .      
            .                     .          
                                             
           """
    t.gen_text(monaLines, 10)

    t.toggle_show_cursor(True)
    t.gen_text(user_details_lines, 2, 35, count=5, contin=True)
    t.gen_prompt(t.curr_row)
    t.gen_typing_text(
        "\x1b[92m# Have a nice day, felicidades. Thanks for hopping by!",
        t.curr_row,
        contin=True,
    )
    t.save_frame("fetch_details.png")
    t.gen_text("", t.curr_row, count=80, contin=True)

    t.gen_gif()
    image = gifos.utils.upload_imgbb("output.gif", 129600)  # 1.5 days expiration
    readme_file_content = rf"""<div align="justify">
<picture>
    <source media="(prefers-color-scheme: dark)" srcset="{image.url}">
    <source media="(prefers-color-scheme: light)" srcset="{image.url}">
    <img alt="GIF_OS" src="{image.url}">
</picture>

<sub><i>Generated automatically using [x0rzavi/github-readme-terminal](https://github.com/x0rzavi/github-readme-terminal) on {time_now}</i></sub>

</div>

<!-- Image deletion URL: {image.delete_url} -->"""
    with open("README.md", "w") as fp:
        fp.write(readme_file_content)
        print("INFO: README.md file generated")


if __name__ == "__main__":
    main()
