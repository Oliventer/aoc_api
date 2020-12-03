# aoc_api
Api development for adventofcode

## Endpoints:

+ GET /advents/ - advents list.
+ GET /advents/:advent_id/ - specific advent where :advent_id is some year. 
+ GET /advents/:advent_id/problems/ - problem list for current :advent_id.
+ GET /advents/:advent_id/problems/:problem_id/ - specific problem where :problem_id is a day the problem was published on.
+ GET /advents/:advent_id/problems/last/ - last available problem of the advent.
