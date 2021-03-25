# Commands

- Line selection
```
plot "<(sed -n '1,10p' file)" using (($1)*1e3):($2*1000) with line lw 3.5 lt rgb "purple" title "my title"
```
- Line style
```
set style line 1 lt rgb "red" lw 1.5 dt 5
set style line 2 lt rgb "orange" lw 1.5 dt 5
set style line 3 lt rgb "yellow" lw 1.5 dt 5
set style line 4 lt rgb "green" lw 1.5 dt 5
set style line 5 lt rgb "cyan" lw 1.5 dt 5
set style line 6 lt rgb "blue" lw 1.5 dt 5
set style line 7 lt rgb "violet" lw 1.5 dt 5

set style line 11 lt rgb "red" lw 1.5 dt 1
set style line 12 lt rgb "orange" lw 1.5 dt 1
set style line 13 lt rgb "yellow" lw 1.5 dt 1
set style line 14 lt rgb "green" lw 1.5 dt 1
set style line 15 lt rgb "cyan" lw 1.5 dt 1
set style line 16 lt rgb "blue" lw 1.5 dt 1
set style line 17 lt rgb "violet" lw 1.5 dt 1
```
- Terminals
```
set terminal x11 size 1300, 900 position 0,0
set term pngcairo size 1300, 900
set term pngcairo dashed # Dashed lines
```
- Encoding
```
set terminal postscript enhanced
set encoding iso_8859_1
set termoption enhanced
set encoding utf8
```
- Labels and title
```
set xlabel "a ({/Symbol m})s
set ylabel "b (ms)"
set title "°ø"
set xrange [16:19.5]
set title "a\nb"
```
- Grid
```
set grid ;
show grid ;
```
- Output
```
set output file.png
```
- Input
```
FILES = system("ls -1 ~/mydir/*data*.dat")
LABEL = system("ls -1 ~/mydir/*data*.dat | sed -e 's/.dat//' -e 's/.*data.*//'")
plot for [i=1:words(FILES)] word(FILES,i) u (($1)*1.668335e-3):($3*1e3) with lines title word(LABEL,i)

```
