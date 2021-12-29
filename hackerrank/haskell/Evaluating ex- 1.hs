fact n = product [1..n]
calcTerm x i = x**i/(fact i)

solve :: Double -> Double
solve x = sum (map (calcTerm x) [0..9]) -- Insert your code here --

main :: IO ()
main = getContents >>= mapM_ print. map solve. map (read::String->Double). tail. words
