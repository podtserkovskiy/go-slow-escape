# go-slow-escape

Slow escape analysis example
```
go build -a -x -work example.com/go-escape/gen_bad
```

Fast escape analysys example
```
go build -a -x -work example.com/go-escape/gen_good
```

Files `good.cpu` and `bad.cpu` contain pprof profiles for both cases
