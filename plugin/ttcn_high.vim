hi ttcn3_module ctermfg=DarkBlue
hi ttcn3_type ctermfg=Green
hi ttcn3_const ctermfg=DarkGreen
hi ttcn3_template ctermfg=Blue
hi ttcn3_function ctermfg=LightRed
hi ttcn3_signature ctermfg=None
hi ttcn3_testcase ctermfg=Red
hi ttcn3_altstep ctermfg=LightGrey
hi ttcn3_group ctermfg=None
hi ttcn3_modulepar ctermfg=None
hi ttcn3_var ctermfg=Blue
hi ttcn3_timer ctermfg=None
hi ttcn3_port ctermfg=Brown
hi ttcn3_member ctermfg=None
hi ttcn3_enum ctermfg=None

autocmd BufReadPost *.ttcn3 call HighlightTtcn(expand("%"))
