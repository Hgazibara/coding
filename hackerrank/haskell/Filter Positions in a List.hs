f lst = [x | (x,y) <- zip lst [0..(length lst)], odd y] -- Fill up this Function

-- This part deals with the Input and Output and can be used as it is. Do not modify it.
main = do
   inputdata <- getContents
   mapM_ putStrLn $ map show $ f $ map (read :: String -> Int) $ lines inputdata
