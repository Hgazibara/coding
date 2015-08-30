#include <iostream>
#include <string>
#include <utility>
#include <unordered_set>
#include <queue>
using namespace std;

class Solution {
public:
    vector<string> findNeighbours(string word, unordered_set<string>& dict) {
        vector<string> neighbours;
        int n = word.size();

        for (int i = 0; i < n; ++i) {
            string s = word;
            for (char c = 'a'; c <= 'z'; ++c) {
                s[i] = c;
                if (dict.count(s) && this->areNeighbours(word, s)) {
                    neighbours.push_back(s);
                }
            }
        }

        return neighbours;
    }

    int areNeighbours(string word, string other) {
        int n = word.size();
        int changes = 0;

        for (int i = 0; i < n; ++i) {
            if (word[i] != other[i]) {
                ++changes;
            }
            if (changes > 1) {
                return false;
            }
        }

        return true;
    }

    int ladderLength(string beginWord, string endWord, unordered_set<string>& wordDict) {
        wordDict.insert(endWord);

        queue<pair<string, int>> q;
        q.push(make_pair(beginWord, 1));

        queue<pair<string, int>> rq;
        rq.push(make_pair(endWord, 1));

        unordered_set<string> visited_q;
        visited_q.insert(beginWord);

        unordered_set<string> visited_rq;
        visited_rq.insert(endWord);

        int q_level = 1;
        int rq_level = 1;

        while (!q.empty() && !rq.empty()) {
            if (q.size() < rq.size()) {
                while (!q.empty() && q.front().second == q_level) {
                    vector<string> neighbours = this->findNeighbours(q.front().first, wordDict);

                    for (auto &word: neighbours) {
                        if (visited_q.count(word) == 0) {
                            visited_q.insert(word);
                            if (visited_rq.count(word)) {
                                return q.front().second + rq.front().second;
                            }
                            q.push(make_pair(word, q_level + 1));
                        }
                    }
                    q.pop();
                }
                ++q_level;
            } else {
                while (!rq.empty() && rq.front().second == rq_level) {
                    vector<string> neighbours = this->findNeighbours(rq.front().first, wordDict);

                    for (auto &word: neighbours) {
                        if (visited_rq.count(word) == 0) {
                            visited_rq.insert(word);
                            if (visited_q.count(word)) {
                                return rq.front().second + q.front().second;
                            }
                            rq.push(make_pair(word, rq_level + 1));
                        }
                    }
                    rq.pop();
                }
                ++rq_level;
            }
        }

        return 0;
    }
};


int main(void) {
    string a = "a";
    string b = "b";
    string c = "c";

    unordered_set<string> s;

    s.insert(a);
    s.insert(b);
    s.insert(c);

    Solution sol;

    cout << sol.ladderLength(a, c, s) << endl;

    return 0;
}
