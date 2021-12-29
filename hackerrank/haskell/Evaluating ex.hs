solve :: Double -> Double
solve x = sum [x**e/(product [1..e]) | e <- [0..9]] -- Insert your code here --

main :: IO ()
main = getContents >>= mapM_ print. map solve. map (read::String->Double). tail. words
