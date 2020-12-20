# Tips

## Markdown

- https://www.markdownguide.org/basic-syntax/

## Git

0. `$ git init name.git`

1. `$ git remote -v; git remote add origin https://github.com/ThomasBucaioni/name.git; git remote -v`

2. `$ git pull`

3. `$ git push -u origin master`

## Shell

- `Ctrl-r`, `setopt no_flow_control`, `Ctrl-s`
- `C-e`, `C-a`, `C-r`
- `M-.`
- `M-#` (bash), `bindkey '^[#' pound-insert` (zsh)
- `C-d`, `C-w`
- `C-x`, `C-e`
- `C-u` (bash/zsh), `C-k`, `C-y`
- `cd !$`, `sudo !!`
- `ls | grep | sed 'p;s/a/b/' | xargs -n2 echo`, `mv`
- `sensors | awk '/Core/ {gsub("[+°C]","",$3), a=a+$3} END {print a/4}`
- `for i in $(seq 10); do echo $((a=a+i)) ; done`, `a=1 ; for i in $(seq 10); do echo $((a=a*i)) ; done`, `a=0; b=0; c=1; for i in $(seq 10); do echo "$((a=b)), $((b=c)), $((c=b+a))" ; done`
- `[[ 0 -eq $? ]] && echo true || echo false`
- 

## Emacs

- `M-x M-p`
- `M-x tdoe`
- 

## NeoVim

- Copy-paste with `"+y` and `"+p` registers

## Screen command

- https://www.geeksforgeeks.org/screen-command-in-linux-with-examples/
