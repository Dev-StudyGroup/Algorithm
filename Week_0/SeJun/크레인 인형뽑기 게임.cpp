#include <string>
#include <vector>
#include <stack>

using namespace std;

int solution(vector<vector<int>> board, vector<int> moves) {
    stack<int> st;
    int cnt = 0;
    int answer = 0;


    while (cnt != moves.size()) {
        int index = moves[cnt] - 1;
        int target;
        for (int i = 0; i < board.size(); i++) {
            if (board[i][index] != 0) {
                target = board[i][index];
                if (!st.empty()) {
                    if (st.top() == target) {
                        answer += 2;
                        st.pop();
                    }
                    else {
                        st.push(target);
                    }
                }
                else {
                    st.push(target);
                }
                board[i][index] = 0;
                break;
            }
        }
        cnt++;
    }

    return answer;
}