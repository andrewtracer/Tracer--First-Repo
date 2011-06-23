bufop q18 lc=.4700; rq18
bufop q18 lc=.4720; rq18
bufop q18 lc=.4800; rq18
bufop q18 lc=.4820; rq18 
bufop q18 lc=.4740; rq18
bufop q18 lc=.4760; rq18
bufop q18 lc=.4780; rq18
bufop q18 lc=.4840; rq18 
bufop q18 lc=.4860; rq18 
bufop q18 lc=.4880; rq18
bufop q18 lc=.4900; rq18
bufop q18 lc=.4920; rq18
bufop q18 lc=.4940; rq18
bufop q18 lc=.4960; rq18
bufop q18 lc=.4980; rq18
bufop q18 lc=.5000; rq18
bufop q18 lc=.5020; rq18
bufop q18 lc=.5040; rq18
bufop q18 lc=.5060; rq18
bufop q18 lc=.5080; rq18
bufop q18 lc=.5100; rq18
bufop q18 lc=.5120; rq18
include mesh2.com
include mesh.com
!SOI: include mesh3.com
bufop q18 lc=1.4900; rq18
bufop q18 lc=1.4920; rq18
bufop q18 lc=1.4940; rq18
bufop q18 lc=1.4960; rq18
bufop q18 lc=1.4980; rq18
bufop q18 lc=1.5000; rq18
bufop q18 lc=1.5020; rq18
bufop q18 lc=1.5040; rq18
bufop q18 lc=1.5060; rq18
bufop q18 lc=1.5080; rq18
bufop q18 lc=1.5100; rq18
bufop q18 lc=1.4800; rq18
bufop q18 lc=1.4820; rq18 *
bufop q18 lc=1.4840; rq18 
bufop q18 lc=1.4860; rq18 
bufop q18 lc=1.4880; rq18
bufop q18 lc=1.5120; rq18
!EOI: include mesh3.com 


