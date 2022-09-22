#include <string>
#include <vector>
#include <algorithm>

using namespace std;

string solution(string new_id) {
    string answer = "";

    vector<char> id;

    //st 1, 2
    for (auto c : new_id) {
        if (c >= 'a' && c <= 'z') id.push_back(c);
        else if (c >= 'A' && c <= 'Z') id.push_back(c + 32);
        else if (c >= '0' && c <= '9') id.push_back(c);
        else if (c == '-' || c == '_' || c == '.') id.push_back(c);
    }

    //st 3
    int idx = 1;
    while (idx < id.size()) {
        if (id[idx - 1] == '.' && id[idx] == '.') {
            id.erase(id.begin() + idx);
            continue;
        }
        idx++;
    }

    //st 4
    if(id.size() > 0) {
    if (id.front() == '.') id.erase(id.begin());
    }

    if(id.size() > 0) {
    if (id.back() == '.') id.erase(id.end() - 1);
    }

    //st 5
    if (id.size() == 0) id.push_back('a');

    //st 6
    if (id.size() >= 16) {
        int idx = 15;
        while (idx < id.size()) {
            id.erase(id.begin() + idx);
        }
        if (id.back() == '.') id.erase(id.end() - 1);
    }

    //st 7
    if (id.size() <= 2) {
        int dumsize = 3 - id.size();
        for (int i = 0; i < dumsize; i++) {
            id.push_back(id[id.size() - 1]);
        }
    }


    for (int i = 0; i < id.size(); i++) answer += id[i];

    return answer;
}