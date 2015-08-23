class Solution {
public:
    bool isAnagram(string s, string t) {
        if (s.size() != t.size()) {
            return false;
        }

        map<char, int> counter;

        for (int i = 0; i < s.size(); ++i) {
            if (!counter.count(s[i])) {
                counter[s[i]] = 0;
            }
            ++counter[s[i]];
        }

        for (int i = 0; i < t.size(); ++i) {
            if (!counter.count(t[i]) || counter[t[i]] == 0) {
                return false;
            }
            --counter[t[i]];
        }

        return true;
    }
};
