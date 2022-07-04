class Solution {
public:
    bool	is_couple(char c1, char c2)
    {
        if ((c1 == '(' && c2 == ')') ||
		    (c1 == '{' && c2 == '}') ||
		    (c1 == '[' && c2 == ']'))
		    return (true);
	    else
		    return (false);
    }

public:
    bool isValid(string s)
    {
        std::stack<char>	steck;
        for (int i = 0; i < s.size(); i++)
        {
            if (!steck.empty() && is_couple(steck.top(), s[i]))
            {
                steck.pop();
            }
            else
            {
                steck.push(s[i]);
            }
        }
        return (steck.empty());
    }
};