#include <string>
#include <vector>
#include <stdlib.h>

using namespace std;
int dist[12][2] = { {0,0},{-1,3},{0,3},{1,3},{-1,2},{0,2},{1,2},{-1,1},{0,1},{1,1},{-1,0},{1,0} };

int l = 10, r = 11;

char getdist(int num, string hand) {

    int local_l = abs(dist[num][0] - dist[l][0]) + abs(dist[num][1] - dist[l][1]);
    int local_r = abs(dist[num][0] - dist[r][0]) + abs(dist[num][1] - dist[r][1]);
    if (local_l > local_r) {
        r = num;
        return 'R';
    }
    else if (local_l < local_r) {
        l = num;
        return 'L';
    }
    else {
        if (hand == "right") {
            r = num;
            return 'R';
        }
        else {
            l = num;
            return 'L';
        }
    }
}

string solution(vector<int> numbers, string hand) {
    string answer = "";
    for (int i = 0; i < numbers.size(); i++) {
        int num = numbers[i];
        if (num == 1 || num == 4 || num == 7) {
            l = num;
            answer += 'L';
        }
        else if (num == 3 || num == 6 || num == 9) {
            r = num;
            answer += 'R';
        }
        else {
            answer += getdist(num, hand);
        }
    }
    return answer;
}