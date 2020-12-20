# Tips

## Markdown

https://www.markdownguide.org/basic-syntax/

## Git

0. `git init name.git`

1. `$ git remote -v; git remote add origin https://github.com/ThomasBucaioni/name.git; git remote -v`

2. `$ git pull`

3. `$ git push -u origin master`

## Shell

- `Ctrl-r`, `setopt no_flow_control`, `Ctrl-s`
- `C-e`, `C-a`, `C-r`
- `M-.`
- `M-#` (bash)
- `C-d`, `C-w`
- `C-x`, `C-e`
- `C-u` (bash/zsh), `C-k`
- `cd !$`, `sudo !!`
- `ls | grep | sed 'p;s/a/b/' | xargs -n2 echo`, `mv`
- `sensors | awk '/Core/ {gsub("[+°C]","",$3), a=a+$3} END {print a/4}`

## Emacs

- `M-x M-p`
- `M-x tdoe`
- 
