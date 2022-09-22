#include <string>
#include <vector>
#include <map>
#include <set>

using namespace std;

vector<string> split(string word, string delim) {
    vector<string> res;
    int pos = 0;
    string part = "";
    while ((pos = word.find(delim)) != string::npos) {
        part = word.substr(0, pos);
        res.push_back(part);
        word.erase(0, pos + delim.length());
    }
    res.push_back(word);
    return res;
}


vector<int> solution(vector<string> id_list, vector<string> report, int k) {
    map<string, set<string>> record;
    map<string, int> result;
    map<int, string> result_idx;


    for (int i = 0; i < id_list.size(); i++) {
        result[id_list[i]] = 0;
        result_idx[i] = id_list[i];
    }


    for (int i = 0; i < report.size(); i++) {
        vector<string> str = split(report[i], " ");
        record[str[1]].insert(str[0]);
    }

    for (auto i = record.begin(); i != record.end(); i++) {
        if (i->second.size() >= k) {
            for (auto n : i->second) result[n]++;
        }
    }
    vector<int> answer;

    for (int i = 0; i < id_list.size(); i++) answer.push_back(result[result_idx[i]]);

    return answer;
}