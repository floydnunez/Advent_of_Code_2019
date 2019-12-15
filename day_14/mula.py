import pstats
p = pstats.Stats('restats')
p.strip_dirs().sort_stats('time', 'cumulative').print_stats()