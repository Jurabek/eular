primes = 2:filter f [3,5..]
    where f n = all ((/= 0) . (mod n)) (takeWhile ((<= n) . (^ 2)) primes)

main = putStrLn $ show $ primes !! 10001

