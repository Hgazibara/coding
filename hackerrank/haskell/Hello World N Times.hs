hello_worlds n = mapM_ putStrLn (replicate n "Hello World") -- Complete this function

-- This part is related to the Input/Output and can be used as it is
-- Do not modify it
main = do
   n <- readLn :: IO Int
   hello_worlds n
