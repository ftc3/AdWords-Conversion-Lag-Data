*days to conversion stuff

import delimited using /users/frankcousin/pycharmprojects/conversion_lag_data/dtc.csv, delim(",") varnames(1) clear

gen n = _n

/*
gen date = date("12feb2010", "DMY") // + doy(n-1)
gen date2 = date + n
format date date2 %td
drop date
*/

gen date = date("12feb2010", "DMY") + n
format date %td
gen dow = dow(date) // sunday == 0

cd /users/frankcousin/desktop/protrainings/dayofweek
*save dow.dta, replace
use dow.dta, replace

gen click_est = cpc * conversions
gen imp_est = ipc * conversions

hist conversions, by(dow) freq
hist days2conv, by(dow) freq



* whole period
tabstat conversions days2conv, col(stats) stats(mean p50 p25 p75 sd min max) by(dow)
* last two years
tabstat conversions days2conv if date >=td(13jul2015), col(stats) stats(mean p50 p25 p75 sd min max) by(dow)
tabstat click_est imp_est if date >= td(13jul2015), col(stats) stats(mean p50 p25 p75 sd min max) by(dow)


hist dow if conversions <50 & date >= td(13jul2015), discrete

