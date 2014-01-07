// A little calculator test

#include <boost/algorithm/string.hpp>

using std::cout;
using std::cin;

int main()
{
  cout << "Press 1 to add, 2 to multiply, 3 to subtract, 4 to divide, or 5 to exit: ";

  int input;
  cin >> input;
  std::cin.ignore();

  if (input < 5)
    {
      // Some variable declarations
      std::string numbers_str;
      std::vector<int> numbers_int;
      std::vector<std::string> numbers_vect;
      std::string op_names[] = {"added", "multiplied", "subtracted", "divided"};

      cout << "Enter 2 or more numbers to be " << op_names[input - 1] << ": ";
      std::getline(cin, numbers_str);

      // Splits numbers_str by whitespace, then converts the string vector into an int vector
      boost::split(numbers_vect, numbers_str, boost::is_any_of("\t "));
      std::transform(begin(numbers_vect), end(numbers_vect), std::back_inserter(numbers_int), [](const std::string& val) { return std::stoi(val); });

      // The math part
      if (1 == input)
        {
          int sum = std::accumulate(numbers_int.begin(), numbers_int.end(), 0);
          cout << sum << std::endl;
        }
      else if (2 == input)
        {
          int multiply_ans = std::accumulate(numbers_int.begin(), numbers_int.end(), 1, std::multiplies<int>());
          cout << multiply_ans << std::endl;
        }
      else if (3 == input)
        {
          int subtract_ans = std::accumulate(numbers_int.begin() + 1, numbers_int.end(), numbers_int[0], std::minus<int>());
          cout << subtract_ans << std::endl;
        }
      else if (4 == input)
        {
          int division_ans = std::accumulate(numbers_int.begin() + 1, numbers_int.end(), numbers_int[0], std::divides<int>());
          cout << division_ans << std::endl;
        }
    }
  else if (5 == input)
    {
      return 0;
    }
  else
    {
      cout << "Invalid option \"" << input << "\"" << std::endl;
    }
}
