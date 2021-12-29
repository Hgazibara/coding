--Only fill up the blanks for the function named len
--Do not modify the structure of the template in any other way
len arr = sum [1 | _ <- arr]

main = do
		inputdata <- getContents
		putStrLn $ show $ len $ map (read :: String -> Int) $ lines inputdata