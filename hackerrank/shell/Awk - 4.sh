awk '
    BEGIN {line = 0;}
    {
        line++;
        if (line % 2 == 1)
            printf "%s;", $0;
        else
            print $0;
    }
    END {}
'