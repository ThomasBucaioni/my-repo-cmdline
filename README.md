# Tips

## Markdown

- https://www.markdownguide.org/basic-syntax/

## Git

### Init

0. `$ git init name.git`
1. `$ git remote -v; git remote add origin https://github.com/ThomasBucaioni/name.git; git remote -v`
2. `$ git pull`
3. `$ git push -u origin master`

### Branch

1. `git checkout master`; 
2. `git branch pr1`; 
2. `git checkout pr1`; 
2. edit files; 
2. `git add somefile1 somefile2`; 
2. `git commit`; 
2. `git push origin pr1`; 
2. `git checkout master`.

### Sync fork

1. `git status`
2. `git remote -v`
2. `git remote add upstream https://github.com/org-repo`
2. `git remote -v`
2. `git fetch upstream`
2. `git checkout master`
2. `git merge upstream/master`

### Drop

1. `git rebase -i HEAD~4`
2. change 'pick' to 'drop'
2. `git push --force`

## Shell

- `Ctrl-r`, `setopt no_flow_control`, `Ctrl-s`
- `C-e`, `C-a`, `C-r`
- `M-.`
- `M-#` (bash), `bindkey '^[#' pound-insert` (zsh)
- `C-d`, `C-w`
- `C-x`, `C-e`
- `C-u` (bash/zsh), `C-k`, `C-y`
- `cd !$`, `sudo !!`, `$1`, `$2`, `$3`, `$@`, `$0`, `$#`, `$*`, `$_`, `$?` ([see](https://devhints.io/bash) [special parameters](https://wiki.bash-hackers.org/syntax/shellvars#special_parameters_and_shell_variables))
- `ls | grep | sed 'p;s/a/b/' | xargs -n2 echo`, `mv`
- `sensors | awk '/Core/ {gsub("[+°C]","",$3), a=a+$3} END {print a/4}`
- `for i in $(seq 10); do echo $((a=a+i)) ; done`, `a=1 ; for i in $(seq 10); do echo $((a=a*i)) ; done`, `a=0; b=0; c=1; for i in $(seq 10); do echo "$((a=b)), $((b=c)), $((c=b+a))" ; done`
- `[[ 0 -eq $? ]] && echo true || echo false`
- `lsblk -f`, `mount -v -t /dev/sdX /mnt`, `lsblk`, `gdisk /dev/sdX (xzyy)`, `sudo dd if=new.iso of=/dev/sdX bs=1M status=progress`, `sudo umount -v /mnt`, `sudo fdisk -l`
- 

## Emacs

- `M-x M-p`
- `M-x tdoe`
- 

## NeoVim

- Copy-paste with `"+y` and `"+p` registers

## Screen command

- https://www.geeksforgeeks.org/screen-command-in-linux-with-examples/
