start_time = lubridate::now()
cards = rep(1:13, 4); n = 1e6; losses = 0
for (i in 1:n){
	losses = losses + any(cards == sample(cards))
}
print(lubridate::now() - start_time)
